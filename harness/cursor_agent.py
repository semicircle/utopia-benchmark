"""Optional runner: Cursor's agent CLI (headless `cursor-agent -p`) as the agent scaffold.

This measures Cursor's agent with any model your Cursor account offers (list
them with `cursor-agent models`), billed to the Cursor subscription, so no
provider API key is needed. It authenticates with the CLI's own login
(`cursor-agent login`) or with CURSOR_API_KEY, which is passed on the command
line and kept out of the environment the model's shell commands inherit.

Cursor still applies your account's user rules and its global configuration;
the workspace itself has no rules files and MCP servers are not auto-approved.

Shell commands run in Cursor's sandbox unless --cursor-sandbox disabled is
given: no network, and no writes outside the workspace and the temp folders
(reads are not restricted). Commands that ask to leave the sandbox are
rejected, since no one is there to approve them, and flagged in the audit.
With the sandbox disabled every command runs unrestricted on the host.

One-shot mode runs in an empty temporary folder in ask mode (read-only, no
shell), with a project permission file that denies every shell command,
file read and write, web fetch and MCP tool, and the sandbox on. Web search
needs an approval that nobody is there to give, so it is rejected. Any tool
call that does happen is counted and flagged.
"""

import json
import os
import re
import signal
import subprocess
import tempfile
import time
from pathlib import Path

import llm

CLI = "cursor-agent"

# Tools that reach outside the workspace by design.
OUTSIDE_TOOLS = {"webSearch", "webFetch", "fetch", "mcp", "task", "computerUse", "recordScreen", "setupVmEnvironment"}
OUTSIDE_CMD_RE = re.compile(r"utopia_benchmark|\.\./\.\.|(^|\s)~|/Users/|/home/|\$HOME|\bfind\s+/\s|\bcurl\b|\bwget\b|"
                            r"\bpip3?\s+install\b|\bgit\s+clone\b|\bmdfind\b|\blocate\b")
# Environment variables never handed to the CLI (its shell tool passes its
# environment on to the model's commands).
SECRET_NAME_RE = re.compile(r"KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL", re.I)


def version():
    try:
        return subprocess.run([CLI, "--version"], capture_output=True, text=True).stdout.strip()
    except OSError:
        return None


def check_ready():
    """None if Cursor's CLI can run, else a message saying what to fix."""
    if os.environ.get("CURSOR_API_KEY"):
        return None
    try:
        r = subprocess.run([CLI, "status"], capture_output=True, text=True, timeout=60, stdin=subprocess.DEVNULL)
    except (OSError, subprocess.TimeoutExpired) as e:
        return f"cannot run {CLI} ({e}). Install Cursor's CLI: https://cursor.com/cli"
    out = r.stdout + r.stderr
    if r.returncode != 0 or "Logged in" not in out:
        return f"Cursor's CLI is not logged in. Run `{CLI} login`."
    return None


def _outside(value, roots, ws):
    p = os.path.realpath(os.path.join(ws, os.path.expanduser(value)))
    return not any(p == r or p.startswith(r + os.sep) for r in roots)


def _tool_bodies(ev):
    """The tool calls in a tool_call event: keys like shellToolCall. The event
    also carries bookkeeping fields (toolCallId, startedAtMs, ...)."""
    tc = ev.get("tool_call")
    if not isinstance(tc, dict):
        return []
    return [(k, v) for k, v in tc.items() if k.endswith("ToolCall") and isinstance(v, dict)]


def compact(path: Path):
    """Merge the thinking stream, one event per fragment, into one event per thought."""
    out, buf = [], None
    for line in path.read_text().splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            ev = None
        if isinstance(ev, dict) and ev.get("type") == "thinking" and ev.get("subtype") == "delta":
            if buf is None:
                buf = {"type": "thinking", "text": "", "timestamp_ms": ev.get("timestamp_ms")}
            buf["text"] += ev.get("text") or ""
            continue
        if isinstance(ev, dict) and ev.get("type") == "thinking" and ev.get("subtype") == "completed":
            continue
        if buf is not None:
            out.append(json.dumps(buf))
            buf = None
        out.append(line)
    if buf is not None:
        out.append(json.dumps(buf))
    path.write_text("\n".join(out) + "\n" if out else "")


def analyze(lines, ws: Path):
    """Process metrics and an audit of anything touching paths outside the workspace."""
    roots = {str(ws), os.path.realpath(ws)}
    tools, suspicious, model_calls = {}, [], set()
    model = final = None
    for line in lines:
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(ev, dict):
            continue
        if ev.get("model_call_id"):
            model_calls.add(ev["model_call_id"])
        kind = ev.get("type")
        if kind == "system" and ev.get("subtype") == "init":
            model = ev.get("model")
        elif kind == "result":
            final = ev
        elif kind == "tool_call" and ev.get("subtype") == "completed":
            # A command that asked to leave the sandbox, e.g. for network access.
            for key, body in _tool_bodies(ev):
                rejected = (body.get("result") or {}).get("rejected")
                if isinstance(rejected, dict):
                    suspicious.append({"tool": key.removesuffix("ToolCall"),
                                       "rejected": str(rejected.get("command") or rejected)[:300]})
        elif kind == "tool_call" and ev.get("subtype") == "started":
            for key, body in _tool_bodies(ev):
                name = key.removesuffix("ToolCall")
                tools[name] = tools.get(name, 0) + 1
                args = body.get("args") or {}
                if not isinstance(args, dict):
                    args = {}
                if name in OUTSIDE_TOOLS:
                    suspicious.append({"tool": name, "input": json.dumps(args)[:300]})
                    continue
                for k, v in args.items():
                    if not isinstance(v, str) or not v:
                        continue
                    if k == "command":
                        if OUTSIDE_CMD_RE.search(v):
                            suspicious.append({"tool": name, "command": v[:300]})
                    elif re.search(r"path|dir|file", k, re.I) and "\n" not in v and _outside(v, roots, str(ws)):
                        suspicious.append({"tool": name, k: v[:300]})
    process = {"model_reported": model, "model_calls": len(model_calls) or None, "tool_calls": tools,
               "suspicious": suspicious}
    return process, final or {}


def toolchain_metrics(trace: Path):
    """Toolchain runs, counted by the toolchain itself however the agent spelled the command."""
    runs = []
    if trace.exists():
        for line in trace.read_text().splitlines():
            try:
                runs.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return {"toolchain_runs": sum(r.get("cmd") == "run" for r in runs),
            "toolchain_runs_failed": sum(r.get("cmd") == "run" and r.get("exit") != 0 for r in runs),
            "toolchain_checks": sum(r.get("cmd") == "check" for r in runs)}


def _exec(cmd, cwd, env, transcript: Path, timeout):
    t0, timed_out = time.time(), False
    with open(transcript, "w") as tf:
        proc = subprocess.Popen(cmd, cwd=cwd, stdin=subprocess.DEVNULL, stdout=tf, stderr=subprocess.PIPE,
                                text=True, env=env, start_new_session=True)
        try:
            _, err = proc.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            _, err = proc.communicate()
            timed_out = True
    compact(transcript)
    return round(time.time() - t0, 1), timed_out, err or ""


def _usage(final, model, process, price_in, price_out):
    u = final.get("usage") or {}
    if not u:
        return None
    acc = llm.Usage(model, price_in, price_out)
    acc.add(u.get("inputTokens"), u.get("outputTokens"), u.get("cacheReadTokens"), u.get("cacheWriteTokens"))
    usage = acc.to_dict()
    usage["requests"] = process["model_calls"]
    return usage


def _stop(final, timed_out):
    if timed_out:
        return "timeout"
    if not final:
        return "error"
    if final.get("is_error", True):
        return "error: " + str(final.get("result") or final.get("subtype") or "")[:300]
    return "end_turn"


def _cmd(model, ws, sandbox, prompt, extra=()):
    cmd = [CLI, "-p", "--output-format", "stream-json", "--model", model, "--workspace", str(ws),
           "--trust", "--sandbox", sandbox, *extra]
    api_key = os.environ.get("CURSOR_API_KEY")
    if api_key:
        cmd += ["--api-key", api_key]
    return cmd + [prompt]


def _env(extra=None):
    env = {k: v for k, v in os.environ.items() if not SECRET_NAME_RE.search(k)}
    env.update(extra or {})
    return env


ONESHOT_PERMISSIONS = {"permissions": {"allow": [], "deny": ["Shell(*)", "Read(**)", "Write(**)", "WebFetch(*)",
                                                             "Mcp(*:*)"]}}


def run_oneshot(run_dir: Path, prompt, model, timeout, price_in=None, price_out=None):
    """One prompt, every tool denied, in an empty temporary folder. Returns the
    same shape as llm's oneshot(), plus process details."""
    run_dir.mkdir(parents=True, exist_ok=True)
    transcript = run_dir / "transcript.jsonl"
    cli_version = version()
    with tempfile.TemporaryDirectory(prefix="utopia-cursor-") as d:
        ws = Path(d).resolve()
        (ws / ".cursor").mkdir()
        (ws / ".cursor" / "cli.json").write_text(json.dumps(ONESHOT_PERMISSIONS))
        cmd = _cmd(model, ws, "enabled", prompt, ["--mode", "ask"])
        seconds, timed_out, err = _exec(cmd, ws, _env(), transcript, timeout)
        lines = transcript.read_text().splitlines()
        process, final = analyze(lines, ws)
    # No tool should run in one-shot mode: every call that did is flagged.
    for name, n in process["tool_calls"].items():
        process["suspicious"].append({"tool": name, "calls": n, "note": "tool call in one-shot mode"})
    segments = []
    for line in lines:
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(ev, dict) and ev.get("type") == "assistant":
            for block in (ev.get("message") or {}).get("content") or []:
                if isinstance(block, dict) and block.get("type") == "text":
                    segments.append(block.get("text") or "")
    return {
        # Cursor's result is the assistant's text segments joined as they streamed.
        "text": final.get("result") or "".join(segments),
        "stop_reason": _stop(final, timed_out),
        "usage": _usage(final, model, process, price_in, price_out),
        "raw": None,
        "seconds": seconds,
        "process": process,
        "stderr_tail": err[-1000:],
        "cursor_cli": cli_version,
    }


def run_agent(ws: Path, transcript: Path, prompt, model, timeout, sandbox="enabled", price_in=None, price_out=None):
    ws = ws.resolve()
    # The trace lives in the workspace so a sandboxed toolchain can still write it.
    tmp = ws / ".tmp"
    tmp.mkdir(exist_ok=True)
    trace = tmp / "trace.jsonl"
    # Headless, nobody can approve a command: with the sandbox disabled, allow
    # them all. (With the sandbox on, --force would also let commands run outside it.)
    cmd = _cmd(model, ws, sandbox, prompt, ["--force"] if sandbox == "disabled" else [])
    cli_version = version()  # before the run: the CLI updates itself in the background
    seconds, timed_out, err = _exec(cmd, ws, _env({"UTOPIA_TRACE": str(trace)}), transcript, timeout)
    process, final = analyze(transcript.read_text().splitlines(), ws)
    process.update(toolchain_metrics(trace))
    return {
        "final_text": final.get("result"),
        "stop": _stop(final, timed_out),
        "steps": process["model_calls"],
        "seconds": seconds,
        "usage": _usage(final, model, process, price_in, price_out),
        "process": process,
        "stderr_tail": err[-1000:],
        "cursor_cli": cli_version,
    }
