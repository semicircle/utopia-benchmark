"""Optional runner: OpenCode (headless `opencode run`) as the scaffold, in
agent or one-shot mode.

This measures OpenCode with any model your OpenCode setup can reach: a
provider you logged in to (`opencode auth login`, e.g. the Kimi For Coding
plan as kimi-code-plan-global/...) or OpenCode's own free models (opencode/...,
e.g. opencode/deepseek-v4.1-flash-free), so no API key is set up here.
Models are named provider/model, as `opencode models` lists them; the effort
becomes OpenCode's variant (provider/model#variant). OPENCODE_BIN points at
another copy of the CLI.

Runs are kept apart from your own OpenCode setup, so they stay comparable.
Each run gets a throwaway HOME and XDG folders, so its own config, database
(sessions, saved permissions) and caches, with a private server (--standalone)
instead of your background service. The only thing copied in is the login of
the model's provider (`opencode auth export` piped into `auth import`; these
are API keys, so nothing needs to be refreshed). Nothing else comes along: no
global or project config, AGENTS.md, ~/.claude CLAUDE.md or skills, plugins,
MCP servers, or saved permissions. The run's config is passed in
OPENCODE_CONFIG_CONTENT.

Agent mode uses OpenCode's default agent (build) with its own prompt and
tools, minus the ones that reach outside the workspace or wait for a person
(web fetch and search, subagents, skills, questions, the browser), and with
permissions auto-approved (--auto). OpenCode has no sandbox of its own, so
the CLI runs inside a Seatbelt sandbox (sandbox.py): writes only in the
workspace, the run's own home and the temp folders, and this repository
unreadable. Network is not blocked. One-shot mode uses an agent whose every
permission is denied, in an empty folder in the same sandbox; any tool call
it makes is flagged.

OpenCode's JSON event stream is the run's transcript.jsonl.
"""

import json
import os
import re
import shutil
import signal
import sqlite3
import subprocess
import tempfile
import time
from pathlib import Path

import llm
import sandbox

DATA = Path(os.environ.get("XDG_DATA_HOME") or Path.home() / ".local" / "share") / "opencode"
FREE_PROVIDER = "opencode"  # OpenCode's own models; the free ones need no login

# Permissions that reach outside the workspace, or wait for a person.
AGENT_DENIED = ["webfetch", "websearch", "codesearch", "task", "skill", "question", "browser"]
OUTSIDE_TOOLS = {"webfetch", "websearch", "codesearch", "task", "browser"}
OUTSIDE_CMD_RE = re.compile(r"utopia_benchmark|\.\./\.\.|(^|\s)~|/Users/|/home/|\$HOME|\bfind\s+/\s|\bcurl\b|\bwget\b|"
                            r"\bpip3?\s+install\b|\bgit\s+clone\b|\bmdfind\b|\blocate\b|opencode")
DROP_ENV_RE = re.compile(r"KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL|^OPENCODE_|^XDG_|^CLAUDE|^ANTHROPIC_|^OPENAI_|^KIMI_|"
                         r"^MOONSHOT_|^DEEPSEEK_|^GEMINI_|^GOOGLE_", re.I)


def binary():
    return os.environ.get("OPENCODE_BIN") or shutil.which("opencode") or str(Path.home() / ".opencode" / "bin" / "opencode")


def version():
    try:
        return subprocess.run([binary(), "--version"], capture_output=True, text=True, timeout=60).stdout.strip() or None
    except (OSError, subprocess.TimeoutExpired):
        return None


def provider_of(model):
    return model.split("/", 1)[0] if "/" in model else None


def _credentials():
    """[(integration_id, value dict)] for your active OpenCode logins, read-only."""
    db = DATA / "opencode.db"
    if not db.exists():
        return []
    try:
        con = sqlite3.connect(f"file:{db}?mode=ro", uri=True, timeout=10)
        try:
            rows = con.execute("select integration_id, value from credential where coalesce(active, 1)").fetchall()
        finally:
            con.close()
    except sqlite3.Error:
        return []
    out = []
    for iid, value in rows:
        try:
            out.append((iid, json.loads(value)))
        except (TypeError, ValueError):
            pass
    return out


def check_ready(model=None, effort=None):
    """None if OpenCode can run this model, else a message saying what to fix."""
    if not os.path.exists(binary()):
        return f"cannot find OpenCode at {binary()}. Install it, or set OPENCODE_BIN."
    if model:
        provider = provider_of(model)
        if not provider:
            return f"name the model as provider/model, as `opencode models` lists it (got {model!r})"
        if "#" in model:
            return "pass the variant as the effort, not in the model name"
        if provider != FREE_PROVIDER and provider not in {iid for iid, _ in _credentials()}:
            return f"OpenCode has no login for {provider}. Run `opencode auth login`."
    return None


def login_secrets():
    out = []
    for _, value in _credentials():
        for k, v in value.items():
            if k != "type" and isinstance(v, str) and len(v) >= 16:
                out.append(v)
    return out


# ---------------------------------------------------------------- the run's own OpenCode home

def config(oneshot):
    cfg = {"autoupdate": False, "share": "disabled",
           "permission": {name: "deny" for name in AGENT_DENIED}}
    if oneshot:
        cfg["agent"] = {"utopia-oneshot": {"mode": "primary", "description": "Answers in one message, without tools.",
                                           "permission": {"*": "deny"}}}
    return cfg


def make_home(base: Path, model, oneshot):
    """A home with only this provider's login. Returns the environment."""
    home = base / "home"
    dirs = {"XDG_CONFIG_HOME": home / ".config", "XDG_DATA_HOME": home / ".local" / "share",
            "XDG_CACHE_HOME": home / ".cache", "XDG_STATE_HOME": home / ".local" / "state"}
    for d in dirs.values():
        d.mkdir(parents=True)
    env = {k: v for k, v in os.environ.items() if not DROP_ENV_RE.search(k)}
    env.update({k: str(v) for k, v in dirs.items()})
    env.update({"HOME": str(home), "OPENCODE_CONFIG_CONTENT": json.dumps(config(oneshot)),
                "OPENCODE_DISABLE_AUTOUPDATE": "1", "OPENCODE_DISABLE_CLAUDE_CODE": "1",
                "OPENCODE_DISABLE_CLAUDE_CODE_PROMPT": "1", "OPENCODE_DISABLE_CLAUDE_CODE_SKILLS": "1",
                "OPENCODE_DISABLE_PROJECT_CONFIG": "1", "OPENCODE_CONFIG_PROJECT_DISABLE": "1"})
    provider = provider_of(model)
    if provider != FREE_PROVIDER:
        # The secret goes from one process to the other in memory, never to a file.
        exp = subprocess.run([binary(), "auth", "export", provider, "--standalone"], capture_output=True, text=True,
                             timeout=120, stdin=subprocess.DEVNULL, cwd=Path.home())
        if exp.returncode != 0 or not exp.stdout.strip():
            raise RuntimeError(f"could not export the OpenCode login for {provider}: {exp.stderr.strip()[-300:]}")
        imp = subprocess.run([binary(), "auth", "import", "--standalone"], input=exp.stdout, capture_output=True,
                             text=True, timeout=120, env=env, cwd=base)
        if imp.returncode != 0:
            raise RuntimeError(f"could not import the OpenCode login for {provider}: {imp.stderr.strip()[-300:]}")
    return env


def command(model, effort, prompt, oneshot):
    target = f"{model}#{effort}" if effort else model
    cmd = [binary(), "run", "--standalone", "--format", "json", "--archived", "--title", "utopia",
           "-m", target, "--agent", "utopia-oneshot" if oneshot else "build"]
    if not oneshot:
        cmd.append("--auto")  # headless: nobody can approve; denied permissions stay denied
    return cmd + [prompt]


def _exec(cmd, cwd, env, transcript: Path, timeout):
    t0, timed_out = time.time(), False
    env = {**env, "PWD": str(cwd)}  # OpenCode trusts $PWD over its real working directory
    env.pop("OLDPWD", None)
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
    p = os.path.realpath(os.path.join(ws, os.path.expanduser(value)))
    return not any(p == r or p.startswith(r + os.sep) for r in roots)


def _num(x):
    return x if isinstance(x, (int, float)) else 0


def analyze(transcript: Path, ws: Path):
    """Text, tool calls, usage and an audit, from OpenCode's JSON events."""
    roots = {str(ws), os.path.realpath(ws)}
    info = {"text": [], "models": [], "steps": 0, "tool_calls": {}, "denied": 0, "suspicious": [], "errors": [],
            "reasons": [], "session_id": None, "cost": 0.0}
    usage = {"input": 0, "output": 0, "reasoning": 0, "cache_read": 0, "cache_write": 0}
    texts = {}
    for ev in _events(transcript):
        t = ev.get("type")
        part = ev.get("part") if isinstance(ev.get("part"), dict) else {}
        info["session_id"] = info["session_id"] or ev.get("sessionID") or part.get("sessionID")
        if t == "text" and part.get("text"):
            texts[part.get("id") or len(texts)] = part["text"]  # a part can be re-sent as it grows
        elif t == "step_start":
            info["steps"] += 1
        elif t == "step_finish":
            tok = part.get("tokens") or {}
            cache = tok.get("cache") or {}
            usage["input"] += _num(tok.get("input"))
            usage["output"] += _num(tok.get("output"))
            usage["reasoning"] += _num(tok.get("reasoning"))
            usage["cache_read"] += _num(cache.get("read"))
            usage["cache_write"] += _num(cache.get("write"))
            info["cost"] += _num(part.get("cost"))
            if part.get("reason"):
                info["reasons"].append(part["reason"])
        elif t == "tool_use":
            name = part.get("tool") or "?"
            state = part.get("state") or {}
            args = state.get("input") if isinstance(state.get("input"), dict) else {}
            info["tool_calls"][name] = info["tool_calls"].get(name, 0) + 1
            if state.get("status") == "error" and re.search(r"denied|reject|not allowed", str(state.get("error")), re.I):
                info["denied"] += 1
            if name in OUTSIDE_TOOLS or name.startswith("mcp"):
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
        elif t == "error" or "error" in str(t).lower():
            err = ev.get("error") or part.get("error") or ev
            info["errors"].append(json.dumps(err, default=str)[:500])
        for m in (part.get("modelID"), (ev.get("info") or {}).get("modelID") if isinstance(ev.get("info"), dict) else None):
            if m and m not in info["models"]:
                info["models"].append(m)
    info["text"] = list(texts.values())
    return info, usage


def _finish(model, effort, info, u, timed_out, code, err, box, price_in, price_out):
    text = "\n\n".join(x for x in info["text"] if x)
    if timed_out:
        stop = "timeout"
    elif code != 0 or info["errors"] or not text:
        detail = "; ".join(info["errors"])[:200] or err.strip()[-300:]
        stop = f"error: {detail}" if detail else "error"
    else:
        stop = "end_turn"
    usage = None
    if any(u.values()):
        acc = llm.Usage(model.split("/", 1)[-1], price_in, price_out)
        acc.add(u["input"], u["output"] + u["reasoning"], u["cache_read"], u["cache_write"])
        usage = acc.to_dict()
        usage["requests"] = info["steps"] or None
        usage["reasoning_tokens"] = u["reasoning"] or None
        usage["opencode_cost_usd"] = round(info["cost"], 6) if info["cost"] else None
    warn = []
    wanted = model.split("/", 1)[-1]
    others = [m for m in info["models"] if m != wanted]
    if others:
        warn.append(f"other models answered: {others}")
    process = {"model_reported": (info["models"] or [None])[-1], "models_answered": info["models"] or None,
               "variant": effort, "model_calls": info["steps"] or None, "tool_calls": info["tool_calls"],
               "tool_calls_denied": info["denied"], "finish_reasons": info["reasons"][-5:],
               "suspicious": info["suspicious"], "errors": info["errors"][:20], "isolation_warnings": warn,
               "session_id": info["session_id"], "sandbox": box}
    return text, stop, usage, process


# ---------------------------------------------------------------- entry points

def run_agent(ws: Path, transcript: Path, prompt, model, effort, timeout, price_in=None, price_out=None):
    ws = ws.resolve()
    tmp = ws / ".tmp"
    tmp.mkdir(exist_ok=True)
    trace = tmp / "trace.jsonl"
    cli = version()
    with tempfile.TemporaryDirectory(prefix="utopia-opencode-") as d:
        base = Path(d).resolve()
        env = make_home(base, model, oneshot=False)
        env["UTOPIA_TRACE"] = str(trace)
        cmd, box = sandbox.wrap(command(model, effort, prompt, False), writable=[ws, base])
        seconds, timed_out, code, err = _exec(cmd, ws, env, transcript, timeout)
    info, u = analyze(transcript, ws)
    text, stop, usage, process = _finish(model, effort, info, u, timed_out, code, err, box, price_in, price_out)
    process.update(toolchain_metrics(trace))
    return {"final_text": info["text"][-1] if info["text"] else None, "stop": stop, "steps": process["model_calls"],
            "seconds": seconds, "usage": usage, "process": process, "stderr_tail": err[-1000:], "opencode_cli": cli}


def run_oneshot(run_dir: Path, prompt, model, effort, timeout, price_in=None, price_out=None):
    """One prompt, every permission denied, in an empty folder. Returns the
    same shape as llm's oneshot(), plus process details."""
    run_dir.mkdir(parents=True, exist_ok=True)
    transcript = run_dir / "transcript.jsonl"
    cli = version()
    with tempfile.TemporaryDirectory(prefix="utopia-opencode-") as d:
        base = Path(d).resolve()
        ws = base / "ws"
        ws.mkdir()
        env = make_home(base, model, oneshot=True)
        cmd, box = sandbox.wrap(command(model, effort, prompt, True), writable=[ws, base])
        seconds, timed_out, code, err = _exec(cmd, ws, env, transcript, timeout)
        info, u = analyze(transcript, ws)
    text, stop, usage, process = _finish(model, effort, info, u, timed_out, code, err, box, price_in, price_out)
    for name, n in info["tool_calls"].items():
        process["suspicious"].append({"tool": name, "calls": n, "note": "tool call in one-shot mode"})
    return {"text": text, "stop_reason": stop, "usage": usage, "raw": None, "seconds": seconds, "process": process,
            "stderr_tail": err[-1000:], "opencode_cli": cli}


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
