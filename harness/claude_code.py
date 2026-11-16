"""Optional runner: Claude Code (headless `claude -p`) as the agent scaffold.

The default agent runner is the harness's own loop (llm.py), which works with
any provider. This one instead measures Claude Code itself. It authenticates
with the API key the harness was given (in --bare mode: no hooks, plugins,
CLAUDE.md or memory) or, without a key, with the CLI's own login.
"""

import json
import os
import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path


def version():
    try:
        return subprocess.run(["claude", "--version"], capture_output=True, text=True).stdout.strip()
    except OSError:
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


def run_agent(ws: Path, transcript: Path, prompt, model, effort, timeout, budget, api_key, bin_name):
    env = {k: v for k, v in os.environ.items()
           if k not in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN", "OPENAI_API_KEY")}
    cmd = ["claude", "-p", "--model", model, "--no-session-persistence",
           "--setting-sources", "project", "--strict-mcp-config", "--disable-slash-commands",
           "--output-format", "stream-json", "--verbose", "--dangerously-skip-permissions",
           "--disallowedTools", "WebSearch", "WebFetch", "Agent", "Task"]
    keydir = None
    if api_key:
        # The key reaches the CLI through a helper file, never through the
        # environment that the model's shell commands inherit.
        keydir = Path(tempfile.mkdtemp(prefix="utopia-auth-"))
        kf = keydir / "key"
        kf.write_text(api_key)
        kf.chmod(0o600)
        cmd += ["--bare", "--settings", json.dumps({"apiKeyHelper": f"cat {kf}"})]
        if budget:
            cmd += ["--max-budget-usd", str(budget)]
    if effort:
        cmd += ["--effort", effort]
    cmd += ["--", prompt]

    t0, timed_out = time.time(), False
    try:
        with open(transcript, "w") as tf:
            proc = subprocess.Popen(cmd, cwd=ws, stdout=tf, stderr=subprocess.PIPE, text=True, env=env)
            try:
                _, err = proc.communicate(timeout=timeout)
            except subprocess.TimeoutExpired:
                proc.kill()
                _, err = proc.communicate()
                timed_out = True
    finally:
        if keydir:
            shutil.rmtree(keydir, ignore_errors=True)
    process, final = analyze(transcript.read_text().splitlines(), ws, bin_name)
    u = final.get("usage") or {}
    return {
        "final_text": final.get("result"),
        "stop": "timeout" if timed_out else ("error" if final.get("is_error", True) else "end_turn"),
        "steps": final.get("num_turns"),
        "seconds": round(time.time() - t0, 1),
        "usage": {
            "input_tokens": u.get("input_tokens"), "output_tokens": u.get("output_tokens"),
            "cache_read_input_tokens": u.get("cache_read_input_tokens"),
            "cache_creation_input_tokens": u.get("cache_creation_input_tokens"),
            "cost_usd_estimate": final.get("total_cost_usd"),
        },
        "process": process,
        "stderr_tail": (err or "")[-1000:],
        "claude_cli": version(),
    }
