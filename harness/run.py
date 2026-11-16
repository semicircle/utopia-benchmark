#!/usr/bin/env python3
"""Run an AI model on Utopia tasks and record the result.

Two modes:

  oneshot  The model gets the language reference and every task in a single
           prompt, with no tools. It must write all solutions without running
           anything. Cheap: one model call per seed. Measures pure in-context
           learning: false friends are not caught by a feedback loop.

  agent    The model runs as a Claude Code agent inside a fresh workspace with
           the docs, the tasks and the dialect's toolchain, and may experiment
           as much as it likes. Expensive, but it is the real benchmark.

Each mode has two arms:

  utopia   a generated dialect (seed + semantics)
  python   the same tasks in Python 3: the control arm

Models are driven through the `claude` CLI (`claude -p`), so a Claude
subscription works without an API key. Every run is saved under
results/runs/RUN_ID/: meta.json (scores, usage, process metrics, audit),
the prompt, the model's response or full agent transcript, and the solutions.

Examples:
    python3 harness/run.py oneshot --seeds 1-8 --model claude-opus-5-5
    python3 harness/run.py oneshot --arm python --model claude-opus-5-5
    python3 harness/run.py agent --seeds 42 --model claude-opus-5-5
"""

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from grade import grade  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TASKS = ROOT / "tasks"
RESULTS = ROOT / "results" / "runs"

AGENT_PROMPT = """\
You are taking part in a programming benchmark. This directory is your
workspace. Start by reading README.md.

Solve every task in tasks/ and save each solution where README.md says.

Rules:
- Work only inside this directory.
- Do not use the internet, and do not look anywhere else on this computer
  for the benchmark's source code, hidden tests or reference solutions.
- You may create scratch files here and run the toolchain as often as you
  like. Test your programs before you finish.

When every task is done, end with a short paragraph: which parts of the
language surprised you or tripped you up?
"""

ONESHOT_HEADER = """\
Below is the complete reference for {lang}, a programming language you have
never seen before, followed by {n} programming tasks.

Write a {lang} solution for every task. You cannot run any code, so read the
reference carefully: where {lang} differs from languages you know, follow the
reference, not habit. Programs read standard input and write standard
output, and are graded by comparing their output exactly.

Give each solution in exactly this format:

<solution task="TASK-ID">
...{lang} source code...
</solution>

"""

ONESHOT_HEADER_PY = """\
Below are {n} programming tasks. Write a {lang} solution for every task. You
cannot run any code. Programs read standard input and write standard output,
and are graded by comparing their output exactly.

Give each solution in exactly this format:

<solution task="TASK-ID">
...{lang} source code...
</solution>

"""

PY_README = """\
# Python workspace

Write programs in Python 3.

- Run a program with `python3 FILE.py`.
- Tasks: one file per task in `tasks/`.
- Put your solution to `tasks/ID.md` in `solutions/ID.py`.

Programs read standard input and write standard output. Your solutions are
graded by running them on hidden test inputs and comparing the output
exactly.
"""

ONESHOT_SYSTEM = "You are an expert programmer. Answer carefully and completely."


# ---------------------------------------------------------------- helpers

def parse_seeds(text):
    seeds = []
    for part in text.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-")
            seeds.extend(range(int(a), int(b) + 1))
        elif part:
            seeds.append(int(part))
    return seeds


def build_toolchain(outdir: Path) -> Path:
    exe = outdir / "utopia"
    subprocess.run(["go", "build", "-o", str(exe), "./cmd/utopia"], cwd=ROOT, check=True)
    return exe


def task_ids():
    return sorted(p.name for p in TASKS.iterdir() if (p / "task.md").exists())


def render_py_prompt(task_id):
    text = (TASKS / task_id / "task.md").read_text()
    return text.replace("{{.Lang}}", "Python").replace("{{.Ext}}", "py")


def claude_version():
    try:
        return subprocess.run(["claude", "--version"], capture_output=True, text=True).stdout.strip()
    except OSError:
        return None


def git_commit():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip() or None


# Authentication. With ANTHROPIC_API_KEY set, claude runs in --bare mode (no
# hooks, plugins, CLAUDE.md or memory: a clean evaluation) and reads the key
# through an apiKeyHelper file outside the workspace. The key is removed from
# the environment the model's tools see, and every saved file is scanned and
# redacted, because transcripts are published. Without a key, the CLI's own
# login (a Claude subscription) is used.
AUTH = {"env": None, "settings": None, "secret": None, "dir": None}


def setup_auth():
    key = os.environ.get("ANTHROPIC_API_KEY")
    AUTH["env"] = {k: v for k, v in os.environ.items()
                   if k not in ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN")}
    if key:
        d = Path(tempfile.mkdtemp(prefix="utopia-auth-"))
        kf = d / "key"
        kf.write_text(key)
        kf.chmod(0o600)
        AUTH.update(settings=json.dumps({"apiKeyHelper": f"cat {kf}"}), secret=key, dir=d)


def teardown_auth():
    if AUTH["dir"]:
        shutil.rmtree(AUTH["dir"], ignore_errors=True)


def redact_tree(root: Path):
    """Replace the API key anywhere under root. Returns the number of files changed."""
    secret = AUTH["secret"]
    if not secret:
        return 0
    n = 0
    for p in root.rglob("*"):
        if p.is_file():
            data = p.read_bytes()
            if secret.encode() in data:
                p.write_bytes(data.replace(secret.encode(), b"[REDACTED]"))
                n += 1
    return n


def short_model(model):
    return model.replace("claude-", "").replace("/", "-")


def make_run_id(mode, arm, model, seed, semantics):
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    tag = "py" if arm == "python" else f"s{seed}-{semantics}"
    return f"{stamp}-{mode}-{short_model(model)}-{tag}"


def claude_base(model, effort):
    cmd = [
        "claude", "-p",
        "--model", model,
        "--no-session-persistence",
        "--setting-sources", "project",  # ignore the operator's user settings, hooks and plugins
        "--strict-mcp-config",            # no MCP servers
        "--disable-slash-commands",       # no skills
    ]
    if AUTH["settings"]:
        cmd += ["--bare", "--settings", AUTH["settings"]]
    if effort:
        cmd += ["--effort", effort]
    return cmd


def dialect_info(exe, seed, semantics):
    out = subprocess.run([str(exe), "info", "-seed", str(seed), "-semantics", semantics],
                         capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def make_workspace(exe, arm, seed, semantics, parent: Path):
    """Create a fresh workspace outside the repository. Returns (ws, info, run_cmd)."""
    ws = Path(tempfile.mkdtemp(prefix="utopia-ws-", dir=parent))
    if arm == "python":
        (ws / "tasks").mkdir()
        (ws / "solutions").mkdir()
        (ws / "README.md").write_text(PY_README)
        for tid in task_ids():
            (ws / "tasks" / f"{tid}.md").write_text(render_py_prompt(tid))
        return ws, {"name": "Python", "ext": "py"}, ["python3"]
    shutil.rmtree(ws)
    subprocess.run([str(exe), "gen", "-seed", str(seed), "-semantics", semantics,
                    "-out", str(ws), "-bake"], cwd=ROOT, check=True, capture_output=True)
    info = dialect_info(exe, seed, semantics)
    bins = list((ws / "bin").iterdir())
    return ws, info, [str(bins[0]), "run"]


def summarize_grade(report):
    return {
        "passed": report["passed_tasks"],
        "total": report["total_tasks"],
        "tasks": {t["id"]: t["passed"] for t in report["tasks"]},
    }


def save_run(run_dir: Path, meta, report, solutions_dir: Path, extra_files):
    run_dir.mkdir(parents=True, exist_ok=True)
    if solutions_dir.exists():
        shutil.copytree(solutions_dir, run_dir / "solutions", dirs_exist_ok=True)
    for name, content in extra_files.items():
        (run_dir / name).write_text(content)
    (run_dir / "grade.json").write_text(json.dumps(report, indent=2) + "\n")
    (run_dir / "meta.json").write_text(json.dumps(meta, indent=2) + "\n")
    if redact_tree(run_dir):
        print(f"WARNING: the API key appeared in {run_dir} and was redacted", file=sys.stderr, flush=True)


# ---------------------------------------------------------------- oneshot

SOLUTION_RE = re.compile(r'<solution task="([^"]+)">\n?(.*?)</solution>', re.S)


def oneshot_one(exe, arm, seed, semantics, model, effort, scratch, timeout):
    ws, info, run_cmd = make_workspace(exe, arm, seed, semantics, scratch)
    lang = info["name"]
    ids = task_ids()
    header = ONESHOT_HEADER_PY if arm == "python" else ONESHOT_HEADER
    parts = [header.format(lang=lang, n=len(ids))]
    if arm != "python":
        ref = next((ws / "docs").glob("*.md")).read_text()
        parts.append("# REFERENCE\n\n" + ref + "\n")
    parts.append("# TASKS\n")
    for tid in ids:
        parts.append(f"## Task ID: {tid}\n\n" + (ws / "tasks" / f"{tid}.md").read_text() + "\n")
    prompt = "\n".join(parts)

    t0 = time.time()
    if model == "reference":
        # Self-test: answer with the reference solutions rendered into the dialect.
        sols = [f'<solution task="{tid}">\n' + subprocess.run(
            [str(exe), "render", "-seed", str(seed), "-semantics", semantics, str(TASKS / tid / "solution.canon")],
            capture_output=True, text=True, check=True).stdout + "</solution>" for tid in ids]
        out = {"result": "\n\n".join(sols)}
    else:
        cmd = claude_base(model, effort) + ["--tools", "", "--system-prompt", ONESHOT_SYSTEM,
                                            "--output-format", "json"]
        proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True, cwd=ws,
                              timeout=timeout, env=AUTH["env"])
        try:
            out = json.loads(proc.stdout)
        except json.JSONDecodeError:
            out = {"is_error": True, "result": proc.stdout[-2000:] + proc.stderr[-2000:]}
    elapsed = time.time() - t0
    if out.get("is_error"):
        raise RuntimeError(f"claude failed for seed {seed}: {out.get('result')}")
    response = out.get("result", "")

    sol_dir = ws / "solutions"
    sol_dir.mkdir(exist_ok=True)
    for tid, code in SOLUTION_RE.findall(response):
        tid = tid.strip()
        if tid in ids:
            (sol_dir / f"{tid}.{info['ext']}").write_text(code)
    report = grade(run_cmd, TASKS, sol_dir)

    run_id = make_run_id("oneshot", arm, model, seed, semantics)
    meta = {
        "run_id": run_id, "mode": "oneshot", "arm": arm, "model": model, "effort": effort,
        "seed": None if arm == "python" else seed,
        "semantics": None if arm == "python" else semantics,
        "language": lang, "dialect": None if arm == "python" else info,
        "date": dt.datetime.now().isoformat(timespec="seconds"),
        "duration_s": round(elapsed, 1),
        "score": summarize_grade(report),
        "usage": out.get("usage"), "model_usage": out.get("modelUsage"),
        "cost_usd": out.get("total_cost_usd"),
        "claude_cli": claude_version(), "commit": git_commit(),
    }
    save_run(RESULTS / run_id, meta, report, sol_dir, {"prompt.md": prompt, "response.md": response})
    shutil.rmtree(ws, ignore_errors=True)
    return meta


# ---------------------------------------------------------------- agent

def analyze_transcript(lines, ws: Path, bin_name):
    """Process metrics and an audit of anything touching paths outside the workspace."""
    roots = {str(ws), os.path.realpath(ws)}
    tools, suspicious = {}, []
    runs = failed_runs = 0
    pending = {}
    model = None
    final = None
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
                if name == "Bash" and re.search(r"utopia_benchmark|\.\./\.\.|\bfind\s+/|~/|/Users/|\$HOME|\bmdfind\b", cmd):
                    suspicious.append({"tool": name, "command": cmd[:300]})
                if name in ("WebSearch", "WebFetch"):
                    suspicious.append({"tool": name, "input": json.dumps(inp)[:300]})
            elif block.get("type") == "tool_result" and pending.pop(block.get("tool_use_id"), False):
                content = block.get("content")
                text = content if isinstance(content, str) else json.dumps(content)
                if block.get("is_error") or "error:" in text:
                    failed_runs += 1
    return {
        "model_reported": model,
        "tool_calls": tools,
        "toolchain_runs": runs,
        "toolchain_runs_failed": failed_runs,
        "suspicious": suspicious,
    }, final


def agent_one(exe, arm, seed, semantics, model, effort, scratch, timeout, budget=None):
    ws, info, run_cmd = make_workspace(exe, arm, seed, semantics, scratch)
    bin_name = None if arm == "python" else Path(run_cmd[0]).name
    run_id = make_run_id("agent", arm, model, seed, semantics)
    run_dir = RESULTS / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    transcript_path = run_dir / "transcript.jsonl"

    cmd = claude_base(model, effort) + [
        "--output-format", "stream-json", "--verbose",
        "--dangerously-skip-permissions",
        *(["--max-budget-usd", str(budget)] if budget else []),
        "--disallowedTools", "WebSearch", "WebFetch", "Agent", "Task",
        "--", AGENT_PROMPT,
    ]
    print(f"[{run_id}] workspace {ws}", flush=True)
    t0 = time.time()
    timed_out = False
    with open(transcript_path, "w") as tf:
        proc = subprocess.Popen(cmd, cwd=ws, stdout=tf, stderr=subprocess.PIPE, text=True, env=AUTH["env"])
        try:
            _, err = proc.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            proc.kill()
            _, err = proc.communicate()
            timed_out = True
    elapsed = time.time() - t0

    lines = transcript_path.read_text().splitlines()
    process, final = analyze_transcript(lines, ws, bin_name)
    report = grade(run_cmd, TASKS, ws / "solutions")
    final = final or {}
    meta = {
        "run_id": run_id, "mode": "agent", "arm": arm, "model": model, "effort": effort,
        "seed": None if arm == "python" else seed,
        "semantics": None if arm == "python" else semantics,
        "language": info["name"], "dialect": None if arm == "python" else info,
        "date": dt.datetime.now().isoformat(timespec="seconds"),
        "duration_s": round(elapsed, 1), "timed_out": timed_out,
        "score": summarize_grade(report),
        "process": process,
        "num_turns": final.get("num_turns"),
        "usage": final.get("usage"), "model_usage": final.get("modelUsage"),
        "cost_usd": final.get("total_cost_usd"),
        "final_message": final.get("result"),
        "is_error": final.get("is_error", True),
        "stderr_tail": (err or "")[-1000:],
        "claude_cli": claude_version(), "commit": git_commit(),
    }
    save_run(run_dir, meta, report, ws / "solutions", {"prompt.md": AGENT_PROMPT})
    # keep the agent's scratch files too: they show how it learned
    scratch_dir = run_dir / "workspace"
    for p in ws.rglob("*"):
        rel = p.relative_to(ws)
        if p.is_file() and rel.parts[0] not in ("bin", "docs", "tasks") and p.stat().st_size < 200_000:
            (scratch_dir / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, scratch_dir / rel)
    if redact_tree(run_dir):
        print(f"WARNING: the API key appeared in {run_dir} and was redacted", file=sys.stderr, flush=True)
    shutil.rmtree(ws, ignore_errors=True)
    return meta


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["oneshot", "agent"])
    ap.add_argument("--arm", choices=["utopia", "python"], default="utopia")
    ap.add_argument("--seeds", default="42", help="e.g. 42 or 1-8 or 3,5,9 (ignored for python)")
    ap.add_argument("--semantics", choices=["random", "standard"], default="random")
    ap.add_argument("--model", default="claude-opus-5-5",
                    help='model for claude --model; "reference" answers with the reference solutions (pipeline self-test)')
    ap.add_argument("--effort", default=None, help="passed to claude --effort (default: CLI default)")
    ap.add_argument("--max-budget", type=float, default=15.0,
                    help="agent mode: USD cap per run, passed to claude --max-budget-usd (API key auth)")
    ap.add_argument("--out", default=None, help="results directory (default results/runs)")
    ap.add_argument("--jobs", type=int, default=4, help="parallel runs")
    ap.add_argument("--timeout", type=float, default=None,
                    help="seconds per run (default 900 oneshot, 3600 agent)")
    args = ap.parse_args()

    global RESULTS
    if args.out:
        RESULTS = Path(args.out).resolve()
    seeds = [0] if args.arm == "python" else parse_seeds(args.seeds)
    timeout = args.timeout or (900 if args.mode == "oneshot" else 3600)
    scratch = Path(tempfile.mkdtemp(prefix="utopia-run-"))
    exe = build_toolchain(scratch)
    setup_auth()
    if args.mode == "oneshot":
        fn = oneshot_one
    else:
        def fn(*a):
            return agent_one(*a, budget=args.max_budget if AUTH["secret"] else None)

    results = []
    with cf.ThreadPoolExecutor(max_workers=args.jobs) as pool:
        futs = {pool.submit(fn, exe, args.arm, s, args.semantics, args.model, args.effort, scratch, timeout): s
                for s in seeds}
        for fut in cf.as_completed(futs):
            s = futs[fut]
            try:
                m = fut.result()
            except Exception as e:  # keep going: one failed seed should not lose the others
                print(f"seed {s}: FAILED: {e}", file=sys.stderr, flush=True)
                continue
            results.append(m)
            sc = m["score"]
            extra = ""
            if m["mode"] == "agent":
                p = m["process"]
                extra = f"  runs={p['toolchain_runs']} failed={p['toolchain_runs_failed']} suspicious={len(p['suspicious'])}"
            print(f"{m['run_id']}: {m['language']:<10} {sc['passed']}/{sc['total']}  {m['duration_s']}s{extra}", flush=True)
    shutil.rmtree(scratch, ignore_errors=True)
    teardown_auth()
    if results:
        tot = sum(m["score"]["passed"] for m in results)
        n = sum(m["score"]["total"] for m in results)
        cost = sum(m.get("cost_usd") or 0 for m in results)
        print(f"\noverall {tot}/{n} tasks ({100 * tot / max(n, 1):.0f}%) over {len(results)} runs, cost ${cost:.2f}")


if __name__ == "__main__":
    main()
