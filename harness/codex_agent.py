"""Optional runner: OpenAI's Codex (headless `codex exec`) as the agent scaffold.

This measures Codex with any model your ChatGPT plan offers, billed to the
subscription, so no API key is needed. It uses the Codex engine that ships
inside the ChatGPT desktop app, which shares the app's login (~/.codex), so a
separate install or login is not needed either. Set CODEX_BIN to use another
copy, e.g. the npm `codex`.

Runs are kept apart from your own Codex setup, so they stay comparable:
config.toml, execpolicy rules, hooks, memories, plugins, ChatGPT apps, skills,
browser and computer use, image generation and web search are all switched
off. What is left is Codex's own agent: its system prompt, its shell and file
editing, and its sub-agents. The model and effort are always passed
explicitly, and the model and effort Codex reports for the session are
recorded with the tools and instruction blocks the model was offered, so any
leak shows up in meta.json.

Agent mode runs shell commands in Codex's sandbox (workspace-write): no
network, and no writes outside the workspace and the temp folders (reads are
not restricted). Approvals are off, so a command that needs to leave the
sandbox fails. One-shot mode runs in an empty read-only folder with the code
tool disabled, so anything the model tries to run fails closed.

Codex saves each session to ~/.codex/sessions. The runner copies it into the
run directory (it has the reasoning summaries, which the event stream does
not) and then archives it, so benchmark runs do not fill the app's history.
"""

import json
import os
import re
import shutil
import signal
import subprocess
import tempfile
import time
from pathlib import Path

import llm

APP_BIN = "/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex"
CODEX_HOME = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")

# Features that would bring in the user's own setup, or tools that reach
# outside the workspace.
FEATURES_OFF = ("apps", "plugins", "hooks", "memories", "goals", "skill_search", "tool_suggest",
                "image_generation", "browser_use", "browser_use_external", "in_app_browser", "computer_use")
# One-shot mode also takes away the tools that run code.
FEATURES_OFF_ONESHOT = ("shell_tool", "unified_exec", "code_mode_host", "view_image")

OUTSIDE_ITEMS = {"web_search", "mcp_tool_call"}
OUTSIDE_CMD_RE = re.compile(r"utopia_benchmark|\.\./\.\.|(^|\s)~|/Users/|/home/|\$HOME|\bfind\s+/\s|\bcurl\b|\bwget\b|"
                            r"\bpip3?\s+install\b|\bgit\s+clone\b|\bmdfind\b|\blocate\b|\.codex\b")
SECRET_NAME_RE = re.compile(r"KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL", re.I)
SESSION_ID_RE = re.compile(r"^[0-9a-f-]{36}$")


def binary():
    b = os.environ.get("CODEX_BIN")
    if b:
        return b
    if os.path.exists(APP_BIN):
        return APP_BIN
    return shutil.which("codex") or APP_BIN


def version():
    try:
        return subprocess.run([binary(), "--version"], capture_output=True, text=True, timeout=30).stdout.strip() or None
    except (OSError, subprocess.TimeoutExpired):
        return None


def models():
    """Model slugs the account offers, from Codex's own catalog."""
    try:
        out = subprocess.run([binary(), "debug", "models"], capture_output=True, text=True, timeout=60).stdout
        return [m["slug"] for m in json.loads(out)["models"] if m.get("visibility") == "list"]
    except (OSError, subprocess.TimeoutExpired, ValueError, KeyError, TypeError):
        return []


def check_ready():
    """None if Codex can run, else a message saying what to fix."""
    b = binary()
    try:
        r = subprocess.run([b, "login", "status"], capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired) as e:
        return f"cannot run Codex at {b} ({e}). Install the ChatGPT desktop app, or set CODEX_BIN."
    status = (r.stdout + r.stderr).strip()
    if r.returncode != 0 or "Logged in" not in status:
        return f"Codex is not logged in ({status or 'no output'}). Sign in to Codex in the ChatGPT app."
    return None


def login_secrets():
    """The login's tokens, so they can be redacted from anything saved."""
    try:
        auth = json.loads((CODEX_HOME / "auth.json").read_text())
    except (OSError, ValueError):
        return []
    out = [auth.get("OPENAI_API_KEY")]
    tokens = auth.get("tokens")
    if isinstance(tokens, dict):
        out += [v for k, v in tokens.items() if k.endswith("_token")]
    return [v for v in out if isinstance(v, str) and len(v) >= 16]


def command(ws, model, effort, sandbox, oneshot=False):
    cmd = [binary(), "exec", "--json", "--ignore-user-config", "--ignore-rules", "--skip-git-repo-check",
           "-s", sandbox, "-C", str(ws), "-m", model,
           "-c", 'web_search="disabled"', "-c", "skills.include_instructions=false"]
    if effort:
        cmd += ["-c", f"model_reasoning_effort={effort}"]
    for f in FEATURES_OFF + (FEATURES_OFF_ONESHOT if oneshot else ()):
        cmd += ["--disable", f]
    return cmd + ["-"]  # the prompt comes on stdin


def _env(extra=None):
    # Codex's shell passes its environment on to the model's commands.
    env = {k: v for k, v in os.environ.items() if not SECRET_NAME_RE.search(k)}
    env.update(extra or {})
    return env


def _exec(cmd, cwd, env, prompt, transcript: Path, timeout):
    t0, timed_out = time.time(), False
    with open(transcript, "w") as tf:
        proc = subprocess.Popen(cmd, cwd=cwd, stdin=subprocess.PIPE, stdout=tf, stderr=subprocess.PIPE,
                                text=True, env=env, start_new_session=True)
        try:
            _, err = proc.communicate(prompt, timeout=timeout)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            _, err = proc.communicate()
            timed_out = True
    return round(time.time() - t0, 1), timed_out, err or ""


def _events(path: Path):
    for line in path.read_text().splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(ev, dict):
            yield ev


def _outside(value, roots, ws):
    p = os.path.realpath(os.path.join(ws, os.path.expanduser(value)))
    return not any(p == r or p.startswith(r + os.sep) for r in roots)


def analyze(transcript: Path, ws: Path):
    """Process metrics, usage and an audit of anything reaching outside the workspace."""
    roots = {str(ws), os.path.realpath(ws)}
    tools, suspicious, errors, messages = {}, [], [], []
    thread = None
    usage = {"input_tokens": 0, "cached_input_tokens": 0, "output_tokens": 0, "reasoning_output_tokens": 0}
    turns = 0
    for ev in _events(transcript):
        kind = ev.get("type")
        if kind == "thread.started":
            thread = ev.get("thread_id")
        elif kind == "turn.completed":
            turns += 1
            for k in usage:
                usage[k] += (ev.get("usage") or {}).get(k) or 0
        elif kind in ("turn.failed", "error"):
            errors.append(str(ev.get("error") or ev.get("message"))[:500])
        elif kind == "item.completed":
            item = ev.get("item") or {}
            it = item.get("type")
            if it == "agent_message":
                messages.append(item.get("text") or "")
                continue
            if it in ("reasoning", "todo_list"):
                continue
            if it == "error":
                msg = str(item.get("message"))
                if "code-mode host is disabled" not in msg:  # expected in one-shot mode
                    errors.append(msg[:500])
                continue
            tools[it] = tools.get(it, 0) + 1
            if it in OUTSIDE_ITEMS:
                suspicious.append({"tool": it, "input": json.dumps(item)[:300]})
            elif it == "command_execution":
                cmd = item.get("command") or ""
                if OUTSIDE_CMD_RE.search(cmd):
                    suspicious.append({"tool": it, "command": cmd[:300]})
            elif it == "file_change":
                for ch in item.get("changes") or []:
                    path = ch.get("path") if isinstance(ch, dict) else None
                    if path and _outside(path, roots, str(ws)):
                        suspicious.append({"tool": it, "path": path[:300]})
    return {"thread_id": thread, "turns": turns, "tool_calls": tools, "suspicious": suspicious,
            "errors": errors, "messages": messages, "usage": usage}


def _tool_names(tools, prefix=""):
    out = []
    for t in tools or []:
        if not isinstance(t, dict):
            continue
        if t.get("type") == "namespace":
            out += _tool_names(t.get("tools"), t.get("name", "") + ".")
        else:
            out.append(prefix + (t.get("name") or t.get("type") or "?"))
    return out


def session_file(thread_id):
    if not thread_id or not SESSION_ID_RE.match(thread_id):
        return None
    hits = sorted((CODEX_HOME / "sessions").rglob(f"rollout-*{thread_id}.jsonl"))
    return hits[-1] if hits else None


def describe_session(path: Path):
    """What Codex says it ran: the model, the effort, the tools and the
    instruction blocks the model was offered, and the number of model calls."""
    info = {"model": None, "effort": None, "tools_offered": None, "instructions": [], "model_calls": 0}
    for ev in _events(path):
        p = ev.get("payload") or {}
        if not isinstance(p, dict):
            continue
        t = p.get("type")
        if t == "thread_settings_applied":
            info["model"] = (p.get("thread_settings") or {}).get("model") or info["model"]
        elif ev.get("type") == "turn_context":
            info["model"] = p.get("model") or info["model"]
            info["effort"] = p.get("effort") or info["effort"]
        elif t == "additional_tools" and info["tools_offered"] is None:
            info["tools_offered"] = _tool_names(p.get("tools"))
        elif t == "message" and p.get("role") == "developer":
            for c in p.get("content") or []:
                m = re.match(r"\s*<([a-z_ ]+)>", (c or {}).get("text") or "")
                tag = m.group(1) if m else "system prompt"
                if tag not in info["instructions"]:
                    info["instructions"].append(tag)
        elif t == "token_count" and p.get("info"):
            info["model_calls"] += 1
    return info


def _collect_session(thread_id, run_dir: Path):
    """Copy Codex's own session log into the run, then archive it in Codex."""
    src = session_file(thread_id)
    if not src:
        return None
    shutil.copy2(src, run_dir / "codex_session.jsonl")
    info = describe_session(run_dir / "codex_session.jsonl")
    subprocess.run([binary(), "archive", thread_id], capture_output=True, text=True, timeout=60)
    return info


def _usage(model, a, session, price_in, price_out):
    u = a["usage"]
    if not any(u.values()):
        return None
    acc = llm.Usage(model, price_in, price_out)
    # Codex's input_tokens include the cached ones; keep them apart, as for the other providers.
    acc.add(u["input_tokens"] - u["cached_input_tokens"], u["output_tokens"], u["cached_input_tokens"], 0)
    out = acc.to_dict()
    out["requests"] = (session or {}).get("model_calls") or None
    out["reasoning_output_tokens"] = u["reasoning_output_tokens"]
    return out


def _stop(a, timed_out):
    if timed_out:
        return "timeout"
    if a["turns"] == 0:
        return "error: " + "; ".join(a["errors"])[:300] if a["errors"] else "error"
    return "end_turn"


def toolchain_metrics(trace: Path):
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


def _process(a, session):
    s = session or {}
    return {"model_reported": s.get("model"), "effort_reported": s.get("effort"),
            "model_calls": s.get("model_calls") or None, "tool_calls": a["tool_calls"],
            "tools_offered": s.get("tools_offered"), "instructions": s.get("instructions"),
            "suspicious": a["suspicious"], "errors": a["errors"][:20]}


def run_agent(ws: Path, transcript: Path, prompt, model, effort, timeout, price_in=None, price_out=None):
    ws = ws.resolve()
    tmp = ws / ".tmp"  # inside the workspace, so the sandboxed toolchain can write its trace
    tmp.mkdir(exist_ok=True)
    trace = tmp / "trace.jsonl"
    cli = version()
    seconds, timed_out, err = _exec(command(ws, model, effort, "workspace-write"), ws,
                                    _env({"UTOPIA_TRACE": str(trace)}), prompt, transcript, timeout)
    a = analyze(transcript, ws)
    session = _collect_session(a["thread_id"], transcript.parent)
    process = _process(a, session)
    process.update(toolchain_metrics(trace))
    return {
        "final_text": a["messages"][-1] if a["messages"] else None,
        "stop": _stop(a, timed_out),
        "steps": process["model_calls"],
        "seconds": seconds,
        "usage": _usage(model, a, session, price_in, price_out),
        "process": process,
        "stderr_tail": err[-1000:],
        "codex_cli": cli,
    }


def run_oneshot(run_dir: Path, prompt, model, effort, timeout, price_in=None, price_out=None):
    """One prompt, no working tools, in an empty read-only folder. Returns the
    same shape as llm's oneshot(), plus process details."""
    run_dir.mkdir(parents=True, exist_ok=True)
    transcript = run_dir / "transcript.jsonl"
    cli = version()
    with tempfile.TemporaryDirectory(prefix="utopia-codex-") as d:
        ws = Path(d).resolve()
        seconds, timed_out, err = _exec(command(ws, model, effort, "read-only", oneshot=True), ws, _env(),
                                        prompt, transcript, timeout)
        a = analyze(transcript, ws)
    session = _collect_session(a["thread_id"], run_dir)
    return {
        # Every message, in order: solutions may be split over several, and a
        # later copy of a solution replaces an earlier one when they are extracted.
        "text": "\n\n".join(a["messages"]),
        "stop_reason": _stop(a, timed_out),
        "usage": _usage(model, a, session, price_in, price_out),
        "raw": None,
        "seconds": seconds,
        "process": _process(a, session),
        "stderr_tail": err[-1000:],
        "codex_cli": cli,
    }
