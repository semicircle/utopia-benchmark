"""Optional runner: Claude Code (headless `claude -p`) as the scaffold, in
agent or one-shot mode.

The default agent runner is the harness's own loop (llm.py), which works with
any provider. This one instead measures Claude Code itself. It authenticates
with the API key the harness was given (via a key helper file, in --bare
mode) or, without a key, with the CLI's own login (`claude auth login`; the
Claude desktop app's sign-in is separate and does not count).

Runs are kept apart from your own Claude Code setup in both cases:
--safe-mode switches off CLAUDE.md, auto-memory, skills, installed plugins,
hooks, MCP servers, custom agents and output styles; no settings file is
read (--setting-sources ''); slash commands are off. Claude Code's built-in
plugins still load (they are the same for everyone). The environment is
cleaned too: a `claude` started from inside another Claude session would
otherwise inherit that session's variables (ANTHROPIC_BASE_URL among them)
and talk to the model through it. Each run records what Claude Code reports
loading (tools, skills, plugins, MCP servers, memory), and anything that
should not be there is listed under process.isolation_warnings.

Agent mode skips Claude Code's permission prompts, so the whole CLI runs
inside a Seatbelt sandbox (sandbox.py): writes only in the workspace, Claude
Code's own state and the temp folders, and this repository unreadable.
Network is not blocked. One-shot mode offers no tools at all (--tools ''),
anything that would ask permission is refused, and it runs in an empty
temporary folder inside the same sandbox.
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

import sandbox

CLI = "claude"
ISOLATION = ["--safe-mode", "--setting-sources", "", "--strict-mcp-config", "--disable-slash-commands",
             "--no-session-persistence"]
# Variables a parent Claude session (or the desktop app) sets, which would
# change how a child `claude` authenticates or where it sends requests.
INHERITED_RE = re.compile(r"^(CLAUDE|ANTHROPIC_|MCP_|OTEL_)|KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL", re.I)
CLAUDE_HOME = Path(os.environ.get("CLAUDE_CONFIG_DIR") or Path.home() / ".claude")


def clean_env(extra=None):
    env = {k: v for k, v in os.environ.items() if not INHERITED_RE.search(k) or k == "CLAUDE_CONFIG_DIR"}
    env.update(extra or {})
    return env


def check_ready(api_key=None):
    """None if Claude Code can run, else a message saying what to fix."""
    if api_key:
        return None
    try:
        r = subprocess.run([CLI, "auth", "status"], capture_output=True, text=True, timeout=60, env=clean_env())
    except (OSError, subprocess.TimeoutExpired) as e:
        return f"cannot run Claude Code ({e})"
    try:
        st = json.loads(r.stdout)
    except ValueError:
        st = {}
    if not st.get("loggedIn"):
        return "Claude Code is not logged in. Run `claude auth login` (the desktop app's sign-in is separate)."
    return None


def _sandboxed(cmd, ws):
    return sandbox.wrap(cmd, writable=[ws, CLAUDE_HOME], writable_files=[Path.home() / ".claude.json"])


def _auth_args(api_key, keydir):
    """With a key: --bare, and the key reaches the CLI through a helper file,
    never through the environment the model's shell commands inherit."""
    if not api_key:
        return []
    kf = keydir / "key"
    kf.write_text(api_key)
    kf.chmod(0o600)
    return ["--bare", "--settings", json.dumps({"apiKeyHelper": f"cat {kf}"})]


def _exec(cmd, cwd, env, stdin_text, transcript: Path, timeout):
    t0, timed_out = time.time(), False
    with open(transcript, "w") as tf:
        proc = subprocess.Popen(cmd, cwd=cwd, stdin=subprocess.PIPE if stdin_text is not None else subprocess.DEVNULL,
                                stdout=tf, stderr=subprocess.PIPE, text=True, env=env, start_new_session=True)
        try:
            _, err = proc.communicate(stdin_text, timeout=timeout)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            _, err = proc.communicate()
            timed_out = True
    return round(time.time() - t0, 1), timed_out, err or ""


def describe(lines):
    """What Claude Code says it loaded, the models that answered, the text of
    every assistant message, and warnings for anything that should be off."""
    info = {"tools_offered": None, "skills": None, "plugins": None, "mcp_servers": None, "memory": None,
            "models_answered": [], "messages": []}
    for line in lines:
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(ev, dict):
            continue
        if ev.get("type") == "system" and ev.get("subtype") == "init":
            info["tools_offered"] = ev.get("tools")
            info["skills"] = ev.get("skills")
            info["plugins"] = [p.get("source") or p.get("name") for p in ev.get("plugins") or [] if isinstance(p, dict)]
            info["mcp_servers"] = ev.get("mcp_servers")
            info["memory"] = ev.get("memory_paths")
        elif ev.get("type") == "assistant":
            msg = ev.get("message") or {}
            m = msg.get("model")
            if m and m not in info["models_answered"] and not m.startswith("<"):
                info["models_answered"].append(m)
            for block in msg.get("content") or []:
                if isinstance(block, dict) and block.get("type") == "text" and block.get("text"):
                    info["messages"].append(block["text"])
    warn = []
    if info["skills"]:
        warn.append(f"skills loaded: {info['skills']}")
    if info["mcp_servers"]:
        warn.append(f"MCP servers loaded: {info['mcp_servers']}")
    if info["memory"]:
        warn.append(f"memory on: {info['memory']}")
    user_plugins = [p for p in info["plugins"] or [] if not str(p).endswith("@builtin")]
    if user_plugins:
        warn.append(f"user plugins loaded: {user_plugins}")
    info["isolation_warnings"] = warn
    return info


def version():
    try:
        return subprocess.run([CLI, "--version"], capture_output=True, text=True, timeout=60).stdout.strip()
    except (OSError, subprocess.TimeoutExpired):
        return None


def analyze(lines, ws: Path, bin_name):
    """Process metrics and an audit of anything touching paths outside the workspace."""
    roots = {str(ws), os.path.realpath(ws)}
    tools, suspicious = {}, []
    runs = failed_runs = 0
    pending = {}
    model = final = None
    for line in lines:
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "system" and ev.get("subtype") == "init":
            model = ev.get("model")
        if ev.get("type") == "result":
            final = ev
        content = (ev.get("message") or {}).get("content")
        for block in content if isinstance(content, list) else []:
            if block.get("type") == "tool_use":
                name, inp = block.get("name"), block.get("input") or {}
                tools[name] = tools.get(name, 0) + 1
                cmd = inp.get("command", "")
                if name == "Bash" and bin_name and re.search(rf"\b{re.escape(bin_name)}\s+run\b", cmd):
                    runs += 1
                    pending[block.get("id")] = True
                for key in ("file_path", "path", "notebook_path"):
                    p = inp.get(key)
                    if p and os.path.isabs(p) and not any(os.path.realpath(p).startswith(r) or p.startswith(r) for r in roots):
                        suspicious.append({"tool": name, key: p})
                if name == "Bash" and re.search(r"utopia_benchmark|\.\./\.\.|\bfind\s+/|~/|/Users/|/home/|\$HOME|\bmdfind\b", cmd):
                    suspicious.append({"tool": name, "command": cmd[:300]})
                if name in ("WebSearch", "WebFetch"):
                    suspicious.append({"tool": name, "input": json.dumps(inp)[:300]})
            elif block.get("type") == "tool_result" and pending.pop(block.get("tool_use_id"), False):
                c = block.get("content")
                text = c if isinstance(c, str) else json.dumps(c)
                if block.get("is_error") or "error:" in text:
                    failed_runs += 1
    process = {"model_reported": model, "tool_calls": tools, "toolchain_runs": runs,
               "toolchain_runs_failed": failed_runs, "suspicious": suspicious}
    return process, final or {}


def _usage(final):
    u = final.get("usage") or {}
    if not u:
        return None
    return {
        "input_tokens": u.get("input_tokens"), "output_tokens": u.get("output_tokens"),
        "cache_read_input_tokens": u.get("cache_read_input_tokens"),
        "cache_creation_input_tokens": u.get("cache_creation_input_tokens"),
        # What the API would have charged; a subscription is billed by plan.
        "cost_usd_estimate": final.get("total_cost_usd"),
    }


def _stop(final, timed_out):
    if timed_out:
        return "timeout"
    if not final:
        return "error"
    if final.get("is_error", True):
        return "error: " + str(final.get("result") or final.get("subtype") or "")[:300]
    return "end_turn"


def run_agent(ws: Path, transcript: Path, prompt, model, effort, timeout, budget, api_key, bin_name):
    ws = ws.resolve()
    cmd = [CLI, "-p", "--model", model, *ISOLATION,
           "--output-format", "stream-json", "--verbose", "--dangerously-skip-permissions",
           "--disallowedTools", "WebSearch", "WebFetch", "Agent", "Task"]
    keydir = Path(tempfile.mkdtemp(prefix="utopia-auth-")) if api_key else None
    try:
        cmd += _auth_args(api_key, keydir)
        if api_key and budget:
            cmd += ["--max-budget-usd", str(budget)]
        if effort:
            cmd += ["--effort", effort]
        cmd += ["--", prompt]
        cmd, box = _sandboxed(cmd, ws)
        cli = version()
        seconds, timed_out, err = _exec(cmd, ws, clean_env(), None, transcript, timeout)
    finally:
        if keydir:
            shutil.rmtree(keydir, ignore_errors=True)
    lines = transcript.read_text().splitlines()
    process, final = analyze(lines, ws, bin_name)
    info = describe(lines)
    process.update({k: info[k] for k in ("tools_offered", "skills", "plugins", "mcp_servers", "memory",
                                         "models_answered", "isolation_warnings")})
    process["sandbox"] = box
    return {
        "final_text": final.get("result"),
        "stop": _stop(final, timed_out),
        "steps": final.get("num_turns"),
        "seconds": seconds,
        "usage": _usage(final),
        "process": process,
        "stderr_tail": err[-1000:],
        "claude_cli": cli,
    }


def run_oneshot(run_dir: Path, prompt, model, effort, timeout, api_key=None):
    """One prompt, no tools, in an empty temporary folder. Returns the same
    shape as llm's oneshot(), plus process details."""
    run_dir.mkdir(parents=True, exist_ok=True)
    transcript = run_dir / "transcript.jsonl"
    cli = version()
    with tempfile.TemporaryDirectory(prefix="utopia-claude-") as d:
        ws = Path(d).resolve() / "ws"
        ws.mkdir()
        cmd = [CLI, "-p", "--model", model, *ISOLATION, "--tools", "", "--permission-mode", "dontAsk",
               "--permission-prompts", "none", "--output-format", "stream-json", "--verbose"]
        cmd += _auth_args(api_key, Path(d))
        if effort:
            cmd += ["--effort", effort]
        cmd, box = _sandboxed(cmd, ws)
        seconds, timed_out, err = _exec(cmd, ws, clean_env(), prompt, transcript, timeout)
    lines = transcript.read_text().splitlines()
    process, final = analyze(lines, ws, None)
    info = describe(lines)
    if info["tools_offered"]:
        info["isolation_warnings"].append(f"tools offered in one-shot mode: {info['tools_offered']}")
    process.update({k: info[k] for k in ("tools_offered", "skills", "plugins", "mcp_servers", "memory",
                                         "models_answered", "isolation_warnings")})
    process["sandbox"] = box
    process["model_reported"] = (info["models_answered"] or [process.get("model_reported")])[-1]
    text = "\n\n".join(info["messages"]) or final.get("result") or ""
    return {
        "text": text,
        "stop_reason": _stop(final, timed_out),
        "usage": _usage(final),
        "raw": None,
        "seconds": seconds,
        "process": process,
        "stderr_tail": err[-1000:],
        "claude_cli": cli,
    }
