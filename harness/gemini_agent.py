"""Optional runner: Google's Gemini CLI (headless `gemini -p`) as the
scaffold, in agent or one-shot mode.

This measures Gemini CLI with the models your Google account offers, billed
to your Google subscription through the CLI's "Sign in with Google" login,
so no API key is needed. Sign in once by running `gemini` and choosing it.
GEMINI_BIN points at another copy of the CLI.

Runs are kept apart from your own Gemini setup, so they stay comparable.
Each run gets a throwaway HOME whose ~/.gemini holds only the login (linked)
and a settings file written for the run: no GEMINI.md, extensions, MCP
servers, hooks, skills (the CLI's built-in ones included), subagents,
checkpoints or auto-update, and folder trust off. Nothing from the real
~/.gemini (Antigravity's files included) is read. Google Cloud variables are
removed from the environment, so the run always uses the personal login. The
model is always passed explicitly.

Gemini CLI can quietly switch to another model when the requested one is out
of quota. Every run records the models that actually answered (from the
CLI's own per-model statistics), and a run in which the requested model did
not answer counts as an error, so it never enters a model's history.

Agent mode uses Gemini CLI's own agent prompt and tools, minus web search
and fetch, asking the user, plan mode and MCP resources, with approvals off
(yolo). The CLI's own sandbox is off; instead the whole CLI runs in the
Seatbelt sandbox (sandbox.py): writes only in the workspace, the run's own
home and the temp folders, and this repository unreadable. Network is not
blocked. One-shot mode excludes every tool, keeps approvals on (so anything
that would need one is refused, as nobody is there to give it), and runs in
an empty folder in the same sandbox.

The CLI's session log is copied into the run as gemini_session.json.
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
import sandbox

GEMINI_HOME = Path.home() / ".gemini"
SHARED = ("oauth_creds.json", "google_accounts.json")  # linked: the login

ALL_TOOLS = ["read_file", "read_many_files", "write_file", "replace", "list_directory", "glob", "grep_search",
             "run_shell_command", "web_fetch", "google_web_search", "save_memory", "write_todos", "activate_skill",
             "invoke_agent", "ask_user", "enter_plan_mode", "exit_plan_mode", "complete_task", "get_internal_docs",
             "list_mcp_resources", "read_mcp_resource", "take_snapshot", "update_topic", "tracker_create_task",
             "tracker_update_task", "tracker_get_task", "tracker_list_tasks", "tracker_add_dependency",
             "tracker_visualize"]
AGENT_EXCLUDED = ["web_fetch", "google_web_search", "ask_user", "enter_plan_mode", "exit_plan_mode", "save_memory",
                  "activate_skill", "invoke_agent", "list_mcp_resources", "read_mcp_resource", "take_snapshot"]
OUTSIDE_TOOLS = {"web_fetch", "google_web_search", "invoke_agent", "read_mcp_resource", "take_snapshot"}
OUTSIDE_CMD_RE = re.compile(r"utopia_benchmark|\.\./\.\.|(^|\s)~|/Users/|/home/|\$HOME|\bfind\s+/\s|\bcurl\b|\bwget\b|"
                            r"\bpip3?\s+install\b|\bgit\s+clone\b|\bmdfind\b|\blocate\b|\.gemini\b")
DROP_ENV_RE = re.compile(r"KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL|^GEMINI_|^GOOGLE_|^CLOUDSDK_|^CLAUDE|^ANTHROPIC_", re.I)


def binary():
    return os.environ.get("GEMINI_BIN") or shutil.which("gemini") or "gemini"


def version():
    try:
        return subprocess.run([binary(), "--version"], capture_output=True, text=True, timeout=60).stdout.strip() or None
    except (OSError, subprocess.TimeoutExpired):
        return None


def check_ready():
    """None if Gemini CLI can run, else a message saying what to fix."""
    if not shutil.which(binary()) and not os.path.exists(binary()):
        return "cannot find Gemini CLI. Install it: npm install -g @google/gemini-cli"
    try:
        creds = json.loads((GEMINI_HOME / "oauth_creds.json").read_text())
    except (OSError, ValueError):
        creds = {}
    if not creds.get("refresh_token"):
        return "Gemini CLI is not signed in. Run `gemini` and choose Sign in with Google."
    return None


def login_secrets():
    try:
        creds = json.loads((GEMINI_HOME / "oauth_creds.json").read_text())
    except (OSError, ValueError):
        return []
    return [v for k, v in creds.items() if k.endswith("_token") and isinstance(v, str) and len(v) >= 16]


def settings(model, oneshot):
    return {
        "security": {"auth": {"selectedType": "oauth-personal"}, "folderTrust": {"enabled": False}},
        "general": {"disableAutoUpdate": True, "disableUpdateNag": True, "checkpointing": {"enabled": False}},
        "model": {"name": model},
        "tools": {"sandbox": False, "exclude": ALL_TOOLS if oneshot else AGENT_EXCLUDED},
        "skills": {"enabled": False},
        "hooksConfig": {"enabled": False},
        "experimental": {"enableAgents": False},
        "mcpServers": {},
    }


def make_home(base: Path, model, oneshot):
    home = base / "home"
    gh = home / ".gemini"
    gh.mkdir(parents=True)
    for name in SHARED:
        if (GEMINI_HOME / name).exists():
            (gh / name).symlink_to(GEMINI_HOME / name)
    (gh / "settings.json").write_text(json.dumps(settings(model, oneshot), indent=2))
    env = {k: v for k, v in os.environ.items() if not DROP_ENV_RE.search(k)}
    env.update({"HOME": str(home), "GOOGLE_GENAI_USE_GCA": "true"})
    return env, gh


def command(model, prompt, oneshot):
    return [binary(), "-p", prompt, "-m", model, "-o", "stream-json", "-e", "none", "--skip-trust",
            "--approval-mode", "default" if oneshot else "yolo"]


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
    return round(time.time() - t0, 1), timed_out, proc.returncode, err or ""


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


def _models_used(stats):
    """{model: requests} from the result's statistics, whatever their exact shape."""
    out = {}
    models = (stats or {}).get("models")
    if isinstance(models, dict):
        for name, m in models.items():
            req = None
            if isinstance(m, dict):
                req = (m.get("api") or {}).get("totalRequests") if isinstance(m.get("api"), dict) else None
                req = req if req is not None else m.get("requests") or m.get("total_requests")
            out[name] = req
    elif isinstance(models, list):
        for m in models:
            if isinstance(m, dict) and m.get("model"):
                out[m["model"]] = m.get("requests") or m.get("total_requests")
    return out


def analyze(transcript: Path, ws: Path):
    roots = {str(ws), os.path.realpath(ws)}
    info = {"model_init": None, "session_id": None, "text": [], "tool_calls": {}, "suspicious": [], "errors": [],
            "result": None}
    for ev in _events(transcript):
        t = ev.get("type")
        if t == "init":
            info["model_init"] = ev.get("model")
            info["session_id"] = ev.get("session_id")
        elif t == "message" and ev.get("role") == "assistant":
            info["text"].append(ev.get("content") or "")
        elif t == "tool_use":
            name, args = ev.get("tool_name") or "?", ev.get("parameters") or {}
            info["tool_calls"][name] = info["tool_calls"].get(name, 0) + 1
            if not isinstance(args, dict):
                args = {}
            if name in OUTSIDE_TOOLS or name.startswith("mcp_"):
                info["suspicious"].append({"tool": name, "input": json.dumps(args)[:300]})
                continue
            for k, v in args.items():
                if not isinstance(v, str) or not v:
                    continue
                if k == "command":
                    if OUTSIDE_CMD_RE.search(v):
                        info["suspicious"].append({"tool": name, "command": v[:300]})
                elif re.search(r"path|dir|file", k, re.I) and "\n" not in v and _outside(v, roots, str(ws)):
                    info["suspicious"].append({"tool": name, k: v[:300]})
        elif t == "error":
            info["errors"].append(str(ev.get("message") or ev)[:500])
        elif t == "result":
            info["result"] = ev
    return info


def _collect(gh: Path, run_dir: Path):
    chats = sorted(gh.glob("tmp/*/chats/session-*"))
    for i, c in enumerate(chats):
        shutil.copy2(c, run_dir / ("gemini_session.json" if i == 0 else f"gemini_session_{i}.json"))
    return chats


def _finish(model, info, timed_out, code, err, box, price_in, price_out):
    res = info["result"] or {}
    stats = res.get("stats") or {}
    used = _models_used(stats)
    warn = []
    others = [m for m in used if m != model]
    if others:
        warn.append(f"other models answered too: {others}")
    if timed_out:
        stop = "timeout"
    elif code != 0 or res.get("status") not in (None, "success") or not info["text"]:
        detail = "; ".join(info["errors"])[:200] or str((res.get("error") or {}).get("message") or "") \
            or err.strip()[-300:]
        stop = f"error: {detail}" if detail else "error"
    elif used and model not in used:
        stop = f"error: model fallback, {model} did not answer ({', '.join(used)} did)"
    else:
        stop = "end_turn"
    u = None
    if stats.get("input_tokens") is not None or stats.get("output_tokens") is not None:
        acc = llm.Usage(model, price_in, price_out)
        cached = stats.get("cached") or stats.get("cached_tokens") or 0
        acc.add((stats.get("input_tokens") or 0) - cached, stats.get("output_tokens") or 0, cached, 0)
        u = acc.to_dict()
        u["requests"] = sum(v for v in used.values() if isinstance(v, int)) or None
    process = {"model_reported": (list(used) or [info["model_init"]])[0] if model not in used else model,
               "models_answered": used or None, "model_init": info["model_init"], "tool_calls": info["tool_calls"],
               "suspicious": info["suspicious"], "errors": info["errors"][:20], "isolation_warnings": warn,
               "stats": stats, "sandbox": box}
    return stop, u, process


def run_agent(ws: Path, transcript: Path, prompt, model, timeout, price_in=None, price_out=None):
    ws = ws.resolve()
    tmp = ws / ".tmp"
    tmp.mkdir(exist_ok=True)
    trace = tmp / "trace.jsonl"
    cli = version()
    with tempfile.TemporaryDirectory(prefix="utopia-gemini-") as d:
        base = Path(d).resolve()
        env, gh = make_home(base, model, oneshot=False)
        env["UTOPIA_TRACE"] = str(trace)
        cmd, box = sandbox.wrap(command(model, prompt, False), writable=[ws, base],
                                writable_files=[GEMINI_HOME / n for n in SHARED])
        seconds, timed_out, code, err = _exec(cmd, ws, env, transcript, timeout)
        _collect(gh, transcript.parent)
    info = analyze(transcript, ws)
    stop, usage, process = _finish(model, info, timed_out, code, err, box, price_in, price_out)
    process.update(toolchain_metrics(trace))
    return {"final_text": "".join(info["text"]) or None, "stop": stop, "steps": (usage or {}).get("requests"),
            "seconds": seconds, "usage": usage, "process": process, "stderr_tail": err[-1000:], "gemini_cli": cli}


def run_oneshot(run_dir: Path, prompt, model, timeout, price_in=None, price_out=None):
    """One prompt, every tool excluded, in an empty folder. Returns the same
    shape as llm's oneshot(), plus process details."""
    run_dir.mkdir(parents=True, exist_ok=True)
    transcript = run_dir / "transcript.jsonl"
    cli = version()
    with tempfile.TemporaryDirectory(prefix="utopia-gemini-") as d:
        base = Path(d).resolve()
        ws = base / "ws"
        ws.mkdir()
        env, gh = make_home(base, model, oneshot=True)
        cmd, box = sandbox.wrap(command(model, prompt, True), writable=[ws, base],
                                writable_files=[GEMINI_HOME / n for n in SHARED])
        seconds, timed_out, code, err = _exec(cmd, ws, env, transcript, timeout)
        _collect(gh, run_dir)
        info = analyze(transcript, ws)
    stop, usage, process = _finish(model, info, timed_out, code, err, box, price_in, price_out)
    for name, n in info["tool_calls"].items():
        process["suspicious"].append({"tool": name, "calls": n, "note": "tool call in one-shot mode"})
    return {"text": "".join(info["text"]), "stop_reason": stop, "usage": usage, "raw": None, "seconds": seconds,
            "process": process, "stderr_tail": err[-1000:], "gemini_cli": cli}


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
