"""Optional runner: Moonshot's Kimi Code CLI (headless `kimi -p`) as the
scaffold, in agent or one-shot mode.

This measures Kimi Code with any model your Kimi plan offers, billed to the
subscription, so no API key is needed: it uses the CLI's own login
(`kimi login`). KIMI_BIN points at another copy of the CLI.

Runs are kept apart from your own Kimi setup, so they stay comparable. Each
run gets a throwaway HOME and KIMI_CODE_HOME holding a config written for the
run: the model's entry and its provider, copied from your config.toml, and
the effort. Nothing else comes along: no permission rules, plugins, MCP
servers, AGENTS.md (yours or ~/.agents/AGENTS.md), skills (~/.agents/skills
included; --skills-dir points at an empty folder), and no search or fetch
services, so web tools have nothing to call. The login is shared by linking
the credentials folder, so a token refreshed during a run stays valid for you.
The model and effort are always set explicitly, and each run records what
Kimi reports: the model requested on every call, the effort, the tools the
model was offered, the AGENTS.md and skills it saw, and the display name your
Kimi catalog gives the model (Moonshot can repoint an alias such as
kimi-for-coding; the name shows when it did).

Agent mode uses Kimi's own agent prompt and tools, minus the ones that reach
outside the workspace (web search and fetch, agent swarms, cron jobs, goals,
remote towers, MCP). Kimi has no sandbox of its own and runs commands
without asking, so the CLI runs inside a Seatbelt sandbox (sandbox.py):
writes only in the workspace, the run's own Kimi home and the temp folders,
and this repository unreadable. Network is not blocked. One-shot mode offers
the model no tools at all, in an empty folder in the same sandbox.

Kimi's session log (wire.jsonl, with the system prompt, every request and
tool call) is copied into the run as kimi_session.jsonl.
"""

import hashlib
import json
import os
import re
import shutil
import signal
import subprocess
import tempfile
import time
import tomllib
from pathlib import Path

import llm
import sandbox

KIMI_HOME = Path(os.environ.get("KIMI_CODE_HOME") or Path.home() / ".kimi-code")
SHARED = ("credentials", "oauth")  # linked, so refreshed tokens stay in sync
COPIED = ("region", "device_id")

# Tools that reach outside the workspace, or wait for a person.
AGENT_DISALLOWED = ["WebSearch", "FetchURL", "AgentSwarm", "CronCreate", "CronList", "CronDelete", "AskUserQuestion",
                    "NotifyUser", "CreateGoal", "GetGoal", "SetGoalBudget", "UpdateGoal", "TowerInit", "TowerStatus",
                    "TowerTeardown", "Skill", "mcp__*"]
OUTSIDE_TOOLS = {"WebSearch", "FetchURL", "AgentSwarm", "TowerInit"}
OUTSIDE_CMD_RE = re.compile(r"utopia_benchmark|\.\./\.\.|(^|\s)~|/Users/|/home/|\$HOME|\bfind\s+/\s|\bcurl\b|\bwget\b|"
                            r"\bpip3?\s+install\b|\bgit\s+clone\b|\bmdfind\b|\blocate\b|\.kimi-code\b")
SECRET_NAME_RE = re.compile(r"KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL", re.I)

PROFILE = """---
name: {name}
description: {description}
{tools}
---
${{base_prompt}}
"""


def binary():
    return os.environ.get("KIMI_BIN") or shutil.which("kimi") or str(Path.home() / ".kimi-code" / "bin" / "kimi")


def version():
    try:
        return subprocess.run([binary(), "--version"], capture_output=True, text=True, timeout=30).stdout.strip() or None
    except (OSError, subprocess.TimeoutExpired):
        return None


def user_config():
    try:
        return tomllib.loads((KIMI_HOME / "config.toml").read_text())
    except (OSError, tomllib.TOMLDecodeError):
        return {}


def default_model():
    return user_config().get("default_model")


def models():
    return sorted(user_config().get("models", {}))


def check_ready(model=None, effort=None):
    """None if Kimi can run this model and effort, else a message saying what to fix."""
    if not os.path.exists(binary()):
        return f"cannot find the Kimi CLI at {binary()}. Install Kimi Code, or set KIMI_BIN."
    try:
        creds = json.loads((KIMI_HOME / "credentials" / "kimi-code.json").read_text())
    except (OSError, ValueError):
        creds = {}
    if not creds.get("refresh_token") and not creds.get("access_token"):
        return "Kimi is not logged in. Run `kimi login`."
    if model:
        entry = user_config().get("models", {}).get(model)
        if entry is None:
            return f"Kimi has no model {model!r}; your config.toml offers: {', '.join(models()) or 'none'}"
        efforts = entry.get("support_efforts")
        if effort and efforts and effort not in efforts:
            return f"{model} supports effort {', '.join(efforts)}, not {effort!r}"
    return None


def login_secrets():
    try:
        creds = json.loads((KIMI_HOME / "credentials" / "kimi-code.json").read_text())
    except (OSError, ValueError):
        return []
    return [v for k, v in creds.items() if k.endswith("_token") and isinstance(v, str) and len(v) >= 16]


# ---------------------------------------------------------------- the run's own Kimi home

def _toml_value(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return repr(v)
    if isinstance(v, str):
        return json.dumps(v)
    if isinstance(v, list):
        return "[ " + ", ".join(_toml_value(x) for x in v) + " ]"
    raise TypeError(f"cannot write {type(v).__name__} to TOML")


def _toml_table(name, table):
    lines, subs = [f"[{name}]"], []
    for k, v in table.items():
        if isinstance(v, dict):
            subs.append(_toml_table(f"{name}.{json.dumps(k)}" if not re.match(r"^\w+$", k) else f"{name}.{k}", v))
        else:
            lines.append(f"{json.dumps(k) if not re.match(r'^[A-Za-z0-9_-]+$', k) else k} = {_toml_value(v)}")
    return "\n".join(lines) + "\n\n" + "".join(subs)


def make_home(base: Path, model, effort, oneshot):
    """A Kimi home with only the login, this model and its provider. Returns
    (env, profile file, the model's catalog entry)."""
    cfg = user_config()
    entry = dict(cfg.get("models", {}).get(model) or {})
    provider_id = entry.get("provider")
    provider = cfg.get("providers", {}).get(provider_id)
    if not entry or not provider:
        raise RuntimeError(f"model {model!r} or its provider is missing from {KIMI_HOME / 'config.toml'}")
    home = base / "home"
    kh = home / ".kimi-code"
    kh.mkdir(parents=True)
    for name in SHARED:
        if (KIMI_HOME / name).exists():
            (kh / name).symlink_to(KIMI_HOME / name)
    for name in COPIED:
        if (KIMI_HOME / name).is_file():
            shutil.copy2(KIMI_HOME / name, kh / name)
    if effort:
        entry["default_effort"] = effort
    text = (f"default_model = {json.dumps(model)}\n"
            # Never Ask: headless, nobody can approve. One-shot has no tools to approve.
            'default_permission_mode = "auto"\n\n'
            + _toml_table(f"providers.{json.dumps(provider_id)}", provider)
            + _toml_table(f"models.{json.dumps(model)}", entry))
    if effort:
        text += _toml_table("thinking", {"enabled": True, "effort": effort})
    (kh / "config.toml").write_text(text)
    (base / "no-skills").mkdir()
    if oneshot:
        tools = "tools: []"
        name, desc = "utopia-oneshot", "Answers in one message, without tools."
    else:
        tools = "disallowedTools:\n" + "".join(f"  - {json.dumps(t)}\n" for t in AGENT_DISALLOWED).rstrip("\n")
        name, desc = "utopia-agent", "Kimi's default agent, without tools that reach outside the workspace."
    profile = base / f"{name}.md"
    profile.write_text(PROFILE.format(name=name, description=desc, tools=tools))
    env = {k: v for k, v in os.environ.items()
           if not SECRET_NAME_RE.search(k) and not k.startswith(("KIMI_", "CLAUDE", "ANTHROPIC_"))}
    env.update({"HOME": str(home), "KIMI_CODE_HOME": str(kh), "KIMI_CODE_NO_AUTO_UPDATE": "1"})
    return env, profile, entry


def command(model, prompt, profile: Path, skills_dir: Path):
    return [binary(), "-p", prompt, "--output-format", "stream-json", "-m", model,
            "--agent-file", str(profile), "--skills-dir", str(skills_dir)]


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


def wire_files(kimi_home: Path):
    return sorted(kimi_home.glob("sessions/*/session_*/agents/*/wire.jsonl"))


def describe(wires, ws: Path):
    """Process metrics, usage and an audit, from Kimi's session logs."""
    roots = {str(ws), os.path.realpath(ws)}
    info = {"model_requested": [], "effort_reported": None, "profile": None, "tools_offered": None,
            "agents_md": None, "skills_hash": None, "system_prompt_sha256": None, "model_calls": 0,
            "tool_calls": {}, "suspicious": [], "errors": [], "turn_end": None}
    usage = {"input": 0, "output": 0, "cache_read": 0, "cache_write": 0}
    for wire in wires:
        main = wire.parent.name == "main"
        for ev in _events(wire):
            t = ev.get("type")
            if t == "profile.bind" and main:
                info["profile"] = ev.get("profileName")
                info["effort_reported"] = ev.get("thinkingEffort")
                sp = ev.get("systemPrompt") or ""
                info["system_prompt_sha256"] = hashlib.sha256(sp.encode()).hexdigest()[:16]
            elif t == "llm.tools_snapshot" and main and info["tools_offered"] is None:
                info["tools_offered"] = [x.get("name") for x in ev.get("tools") or [] if isinstance(x, dict)]
            elif t == "changeNotifier.snapshot" and main:
                info["agents_md"] = sorted((ev.get("agentsMdFiles") or {}).keys())
                info["skills_hash"] = ev.get("skillsHash")
            elif t == "llm.request":
                info["model_calls"] += 1
                m = ev.get("model")
                if m and m not in info["model_requested"]:
                    info["model_requested"].append(m)
            elif t == "turn.ended" and main:
                info["turn_end"] = ev.get("reason")
            elif t and ("error" in t.lower() or t.endswith(".failed")):
                info["errors"].append(json.dumps(ev)[:500])
            elif t == "context.append_loop_event":
                e = ev.get("event") or {}
                if e.get("type") == "step.end":
                    u = e.get("usage") or {}
                    usage["input"] += u.get("inputOther") or 0
                    usage["output"] += u.get("output") or 0
                    usage["cache_read"] += u.get("inputCacheRead") or 0
                    usage["cache_write"] += u.get("inputCacheCreation") or 0
                elif e.get("type") == "tool.call":
                    name, args = e.get("name") or "?", e.get("args") or {}
                    info["tool_calls"][name] = info["tool_calls"].get(name, 0) + 1
                    if not isinstance(args, dict):
                        args = {}
                    if name in OUTSIDE_TOOLS or name.startswith("mcp__"):
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
    return info, usage


def _messages(transcript: Path):
    out = []
    for ev in _events(transcript):
        if ev.get("role") == "assistant" and isinstance(ev.get("content"), str) and ev["content"]:
            out.append(ev["content"])
    return out


def _collect(kimi_home: Path, run_dir: Path):
    wires = wire_files(kimi_home)
    for w in wires:
        agent = w.parent.name
        shutil.copy2(w, run_dir / ("kimi_session.jsonl" if agent == "main" else f"kimi_session_{agent}.jsonl"))
    return wires


def _usage(model, u, info, price_in, price_out):
    if not any(u.values()):
        return None
    acc = llm.Usage(model, price_in, price_out)
    acc.add(u["input"], u["output"], u["cache_read"], u["cache_write"])
    out = acc.to_dict()
    out["requests"] = info["model_calls"] or None
    return out


def _stop(info, messages, timed_out, code, err):
    if timed_out:
        return "timeout"
    if code != 0 or not messages:
        detail = "; ".join(info["errors"])[:200] or err.strip()[-300:]
        return f"error: {detail}" if detail else "error"
    return "end_turn"


def _process(info, entry, box):
    warn = []
    if info["agents_md"]:
        warn.append(f"AGENTS.md loaded: {info['agents_md']}")
    reported = info["model_requested"][-1] if info["model_requested"] else None
    return {"model_reported": reported, "model_display_name": entry.get("display_name"),
            "effort_reported": info["effort_reported"], "profile": info["profile"],
            "model_calls": info["model_calls"] or None, "tool_calls": info["tool_calls"],
            "tools_offered": info["tools_offered"], "agents_md": info["agents_md"], "skills_hash": info["skills_hash"],
            "system_prompt_sha256": info["system_prompt_sha256"], "suspicious": info["suspicious"],
            "errors": info["errors"][:20], "isolation_warnings": warn, "sandbox": box}


def _api_model(entry, model):
    """Kimi's alias (kimi-code/kimi-for-coding) names the API model kimi-for-coding."""
    return entry.get("model") or model


# ---------------------------------------------------------------- entry points

def run_agent(ws: Path, transcript: Path, prompt, model, effort, timeout, price_in=None, price_out=None):
    ws = ws.resolve()
    tmp = ws / ".tmp"
    tmp.mkdir(exist_ok=True)
    trace = tmp / "trace.jsonl"
    cli = version()
    with tempfile.TemporaryDirectory(prefix="utopia-kimi-") as d:
        base = Path(d).resolve()
        env, profile, entry = make_home(base, model, effort, oneshot=False)
        env["UTOPIA_TRACE"] = str(trace)
        cmd, box = sandbox.wrap(command(model, prompt, profile, base / "no-skills"),
                                writable=[ws, base, *(KIMI_HOME / n for n in SHARED)])
        seconds, timed_out, code, err = _exec(cmd, ws, env, transcript, timeout)
        wires = _collect(base / "home" / ".kimi-code", transcript.parent)
        info, u = describe(wires, ws)
    messages = _messages(transcript)
    process = _process(info, entry, box)
    process.update(toolchain_metrics(trace))
    return {
        "final_text": messages[-1] if messages else None,
        "stop": _stop(info, messages, timed_out, code, err),
        "steps": process["model_calls"],
        "seconds": seconds,
        "usage": _usage(_api_model(entry, model), u, info, price_in, price_out),
        "process": process,
        "stderr_tail": err[-1000:],
        "kimi_cli": cli,
    }


def run_oneshot(run_dir: Path, prompt, model, effort, timeout, price_in=None, price_out=None):
    """One prompt, no tools, in an empty folder. Returns the same shape as
    llm's oneshot(), plus process details."""
    run_dir.mkdir(parents=True, exist_ok=True)
    transcript = run_dir / "transcript.jsonl"
    cli = version()
    with tempfile.TemporaryDirectory(prefix="utopia-kimi-") as d:
        base = Path(d).resolve()
        ws = base / "ws"
        ws.mkdir()
        env, profile, entry = make_home(base, model, effort, oneshot=True)
        cmd, box = sandbox.wrap(command(model, prompt, profile, base / "no-skills"),
                                writable=[ws, base, *(KIMI_HOME / n for n in SHARED)])
        seconds, timed_out, code, err = _exec(cmd, ws, env, transcript, timeout)
        wires = _collect(base / "home" / ".kimi-code", run_dir)
        info, u = describe(wires, ws)
    messages = _messages(transcript)
    process = _process(info, entry, box)
    if info["tools_offered"]:
        process["isolation_warnings"].append(f"tools offered in one-shot mode: {info['tools_offered']}")
    for name, n in info["tool_calls"].items():
        process["suspicious"].append({"tool": name, "calls": n, "note": "tool call in one-shot mode"})
    return {
        "text": "\n\n".join(messages),
        "stop_reason": _stop(info, messages, timed_out, code, err),
        "usage": _usage(_api_model(entry, model), u, info, price_in, price_out),
        "raw": None,
        "seconds": seconds,
        "process": process,
        "stderr_tail": err[-1000:],
        "kimi_cli": cli,
    }


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
