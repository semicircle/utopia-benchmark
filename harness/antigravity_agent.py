"""Optional runner: Google's Antigravity CLI (headless `agy -p`) as the
scaffold, in agent or one-shot mode. This is how the Gemini models of your
Google subscription are measured: Antigravity is Google's own agent tool for
them, and the Antigravity *app*'s agentapi is not used (it drives the live
app with its own settings).

The CLI is the standalone `agy` binary. It is not on PATH by default; T3 Code
ships a copy, which is found automatically, and ANTIGRAVITY_BIN points at
another one. Sign in once by running it with no arguments. Models are named
as `agy models` lists them, and the names carry the effort (e.g.
gemini-4-neon-high), as Cursor's do, so no separate effort is passed.

Runs are kept apart from your own Antigravity setup, so they stay comparable.
Each run gets a throwaway HOME, so none of ~/.gemini is read: no GEMINI.md,
settings.json, plugins, skills, workflows, MCP servers, sidecars, hooks,
memories or projects, and none of the app's settings (auto-run, no sandbox).
Only the login comes along: the CLI keeps it in the macOS login keychain,
which it finds through $HOME/Library/Keychains, so that folder is linked (the
keychain still guards each item). Session settings are passed with
--settings and never saved. Google Cloud variables and API keys are removed
from the environment, so the run always uses the personal sign-in.

Agent mode uses Antigravity's own agent prompt and tools, with approvals
skipped (nobody is there to give them); explicit deny rules still apply
under that flag. The rules are permission categories, not tool names:
read_url(*) removes the URL reader, url(*) the browser, mcp(*) MCP tools.
Web search (search_web) runs on Google's side, no permission or setting
covers it, so it stays available; every call is flagged in the run's audit.
(The benchmark's languages are generated per seed, so a search cannot find
answers.) The CLI's own terminal sandbox is off; instead the whole CLI runs in
the Seatbelt sandbox (sandbox.py): writes only in the workspace, the run's
own home and the temp folders, and this repository unreadable. Network is not
blocked. One-shot mode denies every permission category, keeps approvals
strict, and runs in an empty folder in the same sandbox; any tool call is
flagged.

The CLI's stream-json output is the run's transcript.jsonl: an init event
(model, tools offered, permission mode), step_update events (agent_response
steps with text deltas and per-step usage; tool steps with name and
parameters) and a result event (status, response, num_turns, usage).
"""

import glob
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

T3_COPIES = str(Path.home() / ".t3" / "tools" / "antigravity-acp" / "*" / "versions" / "*" / "antigravity")
KEYCHAINS = Path.home() / "Library" / "Keychains"

# Deny rules: permission categories. Agent: what reaches outside the workspace.
AGENT_DENY = ["read_url(*)", "url(*)", "mcp(*)"]
ONESHOT_DENY = AGENT_DENY + ["command(*)", "read_file(*)", "write_file(*)"]
# Tools that reach outside the workspace (flagged when called).
OUTSIDE_TOOLS = {"search_web", "read_url_content", "view_content_chunk", "browser_subagent", "open_browser_url",
                 "read_browser_page", "execute_browser_javascript", "call_mcp_tool", "read_resource", "send_message",
                 "search_marketplace", "run_workflow"}
OUTSIDE_PREFIXES = ("browser_", "mcp")
OUTSIDE_CMD_RE = re.compile(r"utopia_benchmark|\.\./\.\.|(^|\s)~|/Users/|/home/|\$HOME|\bfind\s+/\s|\bcurl\b|\bwget\b|"
                            r"\bpip3?\s+install\b|\bgit\s+clone\b|\bmdfind\b|\blocate\b|\.gemini\b")
DROP_ENV_RE = re.compile(r"KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL|^GEMINI_|^GOOGLE_|^CLOUDSDK_|^ANTIGRAVITY_|^AGY_|"
                         r"^CLAUDE|^ANTHROPIC_", re.I)
SIGNED_OUT_RE = re.compile(r"sign in|not signed in|not logged in", re.I)


def binary():
    env = os.environ.get("ANTIGRAVITY_BIN")
    if env:
        return env
    if shutil.which("agy"):
        return shutil.which("agy")
    copies = sorted(glob.glob(T3_COPIES), key=os.path.getmtime)
    return copies[-1] if copies else "agy"


def version():
    try:
        out = subprocess.run([binary(), "--version"], capture_output=True, text=True, timeout=60)
        text = (out.stdout or out.stderr).strip()
        return text.splitlines()[0] if text else None
    except (OSError, subprocess.TimeoutExpired):
        return None


def make_home(base: Path):
    """A home with only the login (the keychain folder, linked). Returns the environment."""
    home = base / "home"
    (home / ".gemini" / "antigravity-cli").mkdir(parents=True)
    if KEYCHAINS.is_dir():
        (home / "Library").mkdir()
        (home / "Library" / "Keychains").symlink_to(KEYCHAINS)
    env = {k: v for k, v in os.environ.items() if not DROP_ENV_RE.search(k)}
    env.update({"HOME": str(home), "PWD": str(base)})
    env.pop("OLDPWD", None)
    return env


def models():
    """The models `agy models` lists from a clean home, or (None, why not)."""
    with tempfile.TemporaryDirectory(prefix="utopia-agy-") as d:
        base = Path(d).resolve()
        env = make_home(base)
        try:
            out = subprocess.run([binary(), "models"], capture_output=True, text=True, timeout=120, env=env, cwd=base,
                                 stdin=subprocess.DEVNULL)
        except (OSError, subprocess.TimeoutExpired) as e:
            return None, f"`agy models` failed: {e}"
    names = [line.split("\t")[0].strip() for line in (out.stdout or "").splitlines() if "\t" in line]
    if out.returncode != 0 or not names:
        return None, ((out.stdout or "") + (out.stderr or "")).strip()[-300:]
    return sorted(set(names)), None


def check_ready(model=None):
    """None if Antigravity can run this model, else a message saying what to fix."""
    if not shutil.which(binary()) and not os.path.exists(binary()):
        return "cannot find the Antigravity CLI (agy). Set ANTIGRAVITY_BIN, or install T3 Code's copy."
    names, why = models()
    if names is None:
        if SIGNED_OUT_RE.search(why or ""):
            return f"the Antigravity CLI is not signed in. Run `{binary()}` once with no arguments and sign in."
        return f"the Antigravity CLI cannot list models: {why}"
    if model and model not in names:
        return f"Antigravity offers no model {model!r}; `agy models` lists: {', '.join(names)}"
    return None


def login_secrets():
    return []  # the login stays in the keychain; no token is ever in a file the run can copy


def settings(oneshot):
    out = {"permissions": {"deny": ONESHOT_DENY if oneshot else AGENT_DENY}, "allowNonWorkspaceAccess": False}
    if oneshot:
        out["toolPermission"] = "strict"  # anything not denied still needs an approval nobody gives
    return out


def command(model, prompt, oneshot, base: Path):
    cmd = [binary(), "-p", prompt, "--output-format", "stream-json", "--model", model,
           "--settings", json.dumps(settings(oneshot)), "--disable-slash-commands", "--new-project",
           "--log-file", str(base / "agy.log")]
    if not oneshot:
        cmd.append("--dangerously-skip-permissions")
    return cmd


def _exec(cmd, cwd, env, transcript: Path, timeout):
    t0, timed_out = time.time(), False
    env = {**env, "PWD": str(cwd)}
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


# ---------------------------------------------------------------- reading what happened

def _events(path: Path):
    for line in path.read_text().splitlines():
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(ev, dict):
            yield ev


def _outside(value, roots, ws):
    if value.startswith("file://"):
        value = value[len("file://"):]
    p = os.path.realpath(os.path.join(ws, os.path.expanduser(value)))
    return not any(p == r or p.startswith(r + os.sep) for r in roots)


def _num(x):
    return x if isinstance(x, (int, float)) else 0


def analyze(transcript: Path, ws: Path):
    roots = {str(ws), os.path.realpath(ws)}
    info = {"model_init": None, "tools_offered": None, "permission_mode": None, "session_id": None,
            "responses": {}, "steps": 0, "tool_calls": {}, "suspicious": [], "errors": [], "result": None}
    seen_tools = set()

    def tool(name, args):
        info["tool_calls"][name] = info["tool_calls"].get(name, 0) + 1
        args = args if isinstance(args, dict) else {}
        if name in OUTSIDE_TOOLS or name.startswith(OUTSIDE_PREFIXES):
            info["suspicious"].append({"tool": name, "input": json.dumps(args)[:300]})
            return
        for k, v in args.items():
            if not isinstance(v, str) or not v:
                continue
            if re.fullmatch(r"(?i)command(_?line)?|cmd", k):
                if OUTSIDE_CMD_RE.search(v):
                    info["suspicious"].append({"tool": name, "command": v[:300]})
            elif re.search(r"path|dir|file|uri", k, re.I) and "\n" not in v and _outside(v, roots, str(ws)):
                info["suspicious"].append({"tool": name, k: v[:300]})

    for ev in _events(transcript):
        kind = ev.get("event")
        if kind == "init":
            init = ev.get("init") or {}
            info["model_init"] = init.get("model")
            info["tools_offered"] = init.get("tools")
            info["permission_mode"] = init.get("permission_mode")
            info["session_id"] = ev.get("conversation_id")
        elif kind == "step_update":
            s = ev.get("step_update") or {}
            idx, state, stype = s.get("step_index"), s.get("state"), s.get("step_type")
            if state not in ("ACTIVE", "DONE", None):
                info["errors"].append(json.dumps({k: v for k, v in s.items() if k != "conversation_id"})[:500])
            if stype == "agent_response":
                if s.get("text_delta"):
                    info["responses"][idx] = info["responses"].get(idx, "") + s["text_delta"]
                if state == "DONE":
                    info["steps"] += 1
            elif stype == "tool" and idx not in seen_tools:
                seen_tools.add(idx)
                ti = s.get("tool_info") or {}
                tool(s.get("tool_name") or ti.get("name") or "?", ti.get("parameters"))
        elif kind == "result":
            info["result"] = ev.get("result") or {}
        elif kind == "error" or "error" in ev:
            info["errors"].append(json.dumps(ev.get("error") or ev, default=str)[:500])
    return info


def _finish(model, info, timed_out, code, err, box, price_in, price_out):
    res = info["result"] or {}
    responses = [t.strip() for _, t in sorted(info["responses"].items()) if t.strip()]
    text = res.get("response") if isinstance(res.get("response"), str) else ""
    text = text.strip() or "\n\n".join(responses)
    if timed_out:
        stop = "timeout"
    elif code != 0 or (res.get("status") or "").upper() != "SUCCESS" or not text:
        detail = "; ".join(info["errors"])[:200] or str(res.get("error") or res.get("status") or "")[:200] \
            or err.strip()[-300:]
        stop = f"error: {detail}" if detail else "error"
    elif info["model_init"] and info["model_init"] != model:
        stop = f"error: model fallback, {model} was requested but {info['model_init']} ran"
    else:
        stop = "end_turn"
    usage = None
    u = res.get("usage") if isinstance(res.get("usage"), dict) else None
    if u and (u.get("input_tokens") is not None or u.get("output_tokens") is not None):
        acc = llm.Usage(model, price_in, price_out)
        # input_tokens excludes cache reads; output_tokens includes thinking.
        acc.add(_num(u.get("input_tokens")), _num(u.get("output_tokens")), _num(u.get("cache_read_tokens")), 0)
        usage = acc.to_dict()
        usage["requests"] = info["steps"] or res.get("num_turns") or None
        usage["thinking_tokens"] = u.get("thinking_tokens")
    warn = []
    searches = info["tool_calls"].get("search_web", 0)
    if searches:
        warn.append(f"search_web called {searches} time(s); it cannot be switched off")
    process = {"model_reported": info["model_init"], "tool_calls": info["tool_calls"],
               "tools_offered": info["tools_offered"], "permission_mode": info["permission_mode"],
               "model_calls": info["steps"] or None, "suspicious": info["suspicious"], "errors": info["errors"][:20],
               "isolation_warnings": warn, "session_id": info["session_id"], "sandbox": box}
    return text, responses, stop, usage, process


# ---------------------------------------------------------------- entry points

def run_agent(ws: Path, transcript: Path, prompt, model, timeout, price_in=None, price_out=None):
    ws = ws.resolve()
    tmp = ws / ".tmp"
    tmp.mkdir(exist_ok=True)
    trace = tmp / "trace.jsonl"
    cli = version()
    with tempfile.TemporaryDirectory(prefix="utopia-agy-") as d:
        base = Path(d).resolve()
        env = make_home(base)
        env["UTOPIA_TRACE"] = str(trace)
        cmd, box = sandbox.wrap(command(model, prompt, False, base), writable=[ws, base])
        seconds, timed_out, code, err = _exec(cmd, ws, env, transcript, timeout)
    info = analyze(transcript, ws)
    text, responses, stop, usage, process = _finish(model, info, timed_out, code, err, box, price_in, price_out)
    process.update(toolchain_metrics(trace))
    return {"final_text": text or (responses[-1] if responses else None), "stop": stop,
            "steps": process["model_calls"], "seconds": seconds, "usage": usage, "process": process,
            "stderr_tail": err[-1000:], "antigravity_cli": cli}


def run_oneshot(run_dir: Path, prompt, model, timeout, price_in=None, price_out=None):
    """One prompt, every permission denied, in an empty folder. Returns the
    same shape as llm's oneshot(), plus process details."""
    run_dir.mkdir(parents=True, exist_ok=True)
    transcript = run_dir / "transcript.jsonl"
    cli = version()
    with tempfile.TemporaryDirectory(prefix="utopia-agy-") as d:
        base = Path(d).resolve()
        ws = base / "ws"
        ws.mkdir()
        env = make_home(base)
        cmd, box = sandbox.wrap(command(model, prompt, True, base), writable=[ws, base])
        seconds, timed_out, code, err = _exec(cmd, ws, env, transcript, timeout)
        info = analyze(transcript, ws)
    text, _, stop, usage, process = _finish(model, info, timed_out, code, err, box, price_in, price_out)
    for name, n in info["tool_calls"].items():
        process["suspicious"].append({"tool": name, "calls": n, "note": "tool call in one-shot mode"})
    return {"text": text, "stop_reason": stop, "usage": usage, "raw": None, "seconds": seconds, "process": process,
            "stderr_tail": err[-1000:], "antigravity_cli": cli}


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
