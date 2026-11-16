#!/usr/bin/env python3
"""Run an AI model on Utopia tasks and record the result.

Bring an API key and a model name; any endpoint works:

    export ANTHROPIC_API_KEY=...
    python3 harness/run.py oneshot --seeds 1-8 --model claude-opus-5-5

    export OPENAI_API_KEY=...                 # or any OpenAI-compatible endpoint
    python3 harness/run.py oneshot --provider openai --model gpt-5 \\
        --base-url https://openrouter.ai/api/v1 --api-key-env OPENROUTER_API_KEY

Modes:
  oneshot  The language reference and every task in one prompt, no tools. The
           model must write all solutions without running anything. Cheap
           (one request per seed); measures pure in-context learning.
  agent    The model works in a fresh workspace with the reference, the tasks
           and the language's toolchain, using three tools (run_shell,
           read_file, write_file), until it stops or hits a limit.

Arms:
  utopia   a generated dialect (--seeds, --semantics random|standard)
  python   the same tasks in Python 3: the control arm

Every run is saved to results/runs/RUN_ID/: meta.json (score, usage, cost,
process metrics, audit), the prompt, the response or full transcript, and the
solutions. API keys are read from the environment, never written anywhere,
kept out of the agent's shell environment, and redacted from saved files.

Self-tests that need no key:
    python3 harness/run.py oneshot --provider reference --seeds 1-12 --out /tmp/t
    python3 harness/run.py agent --provider scripted --seeds 1-3 --out /tmp/t
"""

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import llm  # noqa: E402
from grade import grade  # noqa: E402

ROOT = HERE.parent
TASKS = ROOT / "tasks"
RESULTS = ROOT / "results" / "runs"

AGENT_SYSTEM = "You are an expert programmer working autonomously in a sandboxed workspace."

AGENT_PROMPT = """\
You are taking part in a programming benchmark. Your workspace is the current
directory. Start by reading README.md.

Solve every task in tasks/ and save each solution where README.md says.

Rules:
- Work only inside the workspace.
- Do not use the internet, and do not look anywhere else on this computer
  for the benchmark's source code, hidden tests or reference solutions.
- You may create scratch files in the workspace and run the toolchain as
  often as you like. Test your programs before you finish.

When every task is done, end with a short paragraph: which parts of the
language surprised you or tripped you up?
"""

ONESHOT_SYSTEM = "You are an expert programmer. Answer carefully and completely."

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

SOLUTION_RE = re.compile(r'<solution task="([^"]+)">\n?(.*?)</solution>', re.S)
DEFAULT_KEY_ENV = {"anthropic": "ANTHROPIC_API_KEY", "openai": "OPENAI_API_KEY"}
SECRET_ENV = ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN", "OPENAI_API_KEY")


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


def task_ids():
    return sorted(p.name for p in TASKS.iterdir() if (p / "task.md").exists())


def git_commit():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip() or None


def make_run_id(cfg, mode, seed):
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    model = re.sub(r"[^A-Za-z0-9.-]+", "-", cfg.model.replace("claude-", ""))
    tag = "py" if cfg.arm == "python" else f"s{seed}-{cfg.semantics}"
    return f"{stamp}-{mode}-{model}-{tag}"


def redact_tree(root: Path, secrets):
    n = 0
    for p in root.rglob("*"):
        if p.is_file():
            data = p.read_bytes()
            new = data
            for s in secrets:
                new = new.replace(s.encode(), b"[REDACTED]")
            if new != data:
                p.write_bytes(new)
                n += 1
    return n


class Run:
    """A fresh workspace outside the repository. Grading never trusts anything
    the agent could reach: it rebuilds the toolchain after the agent is done."""

    def __init__(self, cfg, exe, seed, scratch: Path):
        self.cfg, self.seed = cfg, seed
        self.dir = Path(tempfile.mkdtemp(prefix="utopia-", dir=scratch))
        self.ws = self.dir / "ws"
        if cfg.arm == "python":
            (self.ws / "tasks").mkdir(parents=True)
            (self.ws / "solutions").mkdir()
            (self.ws / "README.md").write_text(PY_README)
            for tid in task_ids():
                text = (TASKS / tid / "task.md").read_text()
                (self.ws / "tasks" / f"{tid}.md").write_text(text.replace("{{.Lang}}", "Python").replace("{{.Ext}}", "py"))
            self.info = {"name": "Python", "ext": "py"}
            self.bin_name = None
            return
        subprocess.run([str(exe), "gen", "-seed", str(seed), "-semantics", cfg.semantics,
                        "-out", str(self.ws), "-bake"], cwd=ROOT, check=True, capture_output=True)
        self.info = json.loads(subprocess.run(
            [str(exe), "info", "-seed", str(seed), "-semantics", cfg.semantics],
            capture_output=True, text=True, check=True).stdout)
        self.bin_name = next((self.ws / "bin").iterdir()).name

    def grade(self):
        """Grade the workspace's solutions with a toolchain built just now, in a
        directory the agent never saw."""
        sol = self.ws / "solutions"
        if self.cfg.arm == "python":
            return grade(["python3"], TASKS, sol)
        with tempfile.TemporaryDirectory(prefix="utopia-grader-") as d:
            exe = Path(d) / "utopia"
            subprocess.run(["go", "build", "-o", str(exe), "./cmd/utopia"], cwd=ROOT, check=True)
            return grade([str(exe), "run", "-seed", str(self.seed), "-semantics", self.cfg.semantics], TASKS, sol)

    def reference(self, exe, tid):
        return subprocess.run([str(exe), "render", "-seed", str(self.seed), "-semantics", self.cfg.semantics,
                               str(TASKS / tid / "solution.canon")], capture_output=True, text=True, check=True).stdout

    def cleanup(self):
        shutil.rmtree(self.dir, ignore_errors=True)


def base_meta(cfg, run, mode, run_id):
    return {
        "run_id": run_id, "mode": mode, "arm": cfg.arm,
        "provider": cfg.provider, "base_url": cfg.base_url, "model": cfg.model,
        "runner": cfg.runner if mode == "agent" else None,
        "effort": cfg.effort, "thinking": cfg.thinking, "max_tokens": cfg.max_tokens,
        "seed": None if cfg.arm == "python" else run.seed,
        "semantics": None if cfg.arm == "python" else cfg.semantics,
        "language": run.info["name"], "dialect": None if cfg.arm == "python" else run.info,
        "date": dt.datetime.now().isoformat(timespec="seconds"),
        "commit": git_commit(),
    }


def finish(cfg, run_dir: Path, meta, report, solutions: Path, files):
    run_dir.mkdir(parents=True, exist_ok=True)
    if solutions.exists():
        shutil.copytree(solutions, run_dir / "solutions", dirs_exist_ok=True)
    for name, content in files.items():
        (run_dir / name).write_text(content)
    meta["score"] = {"passed": report["passed_tasks"], "total": report["total_tasks"],
                     "tasks": {t["id"]: t["passed"] for t in report["tasks"]}}
    (run_dir / "grade.json").write_text(json.dumps(report, indent=2) + "\n")
    (run_dir / "meta.json").write_text(json.dumps(meta, indent=2, default=str) + "\n")
    if cfg.secrets and redact_tree(run_dir, cfg.secrets):
        print(f"WARNING: an API key appeared in {run_dir} and was redacted", file=sys.stderr, flush=True)
    return meta


# ---------------------------------------------------------------- oneshot

def oneshot_prompt(run):
    ids = task_ids()
    lang = run.info["name"]
    header = ONESHOT_HEADER_PY if run.cfg.arm == "python" else ONESHOT_HEADER
    parts = [header.format(lang=lang, n=len(ids))]
    if run.cfg.arm != "python":
        parts.append("# REFERENCE\n\n" + next((run.ws / "docs").glob("*.md")).read_text() + "\n")
    parts.append("# TASKS\n")
    for tid in ids:
        parts.append(f"## Task ID: {tid}\n\n" + (run.ws / "tasks" / f"{tid}.md").read_text() + "\n")
    return "\n".join(parts)


def oneshot_one(cfg, exe, seed, scratch):
    run = Run(cfg, exe, seed, scratch)
    try:
        prompt = oneshot_prompt(run)
        t0 = time.time()
        if cfg.provider == "reference":
            if cfg.arm == "python":
                raise llm.ProviderError("the reference provider has no Python solutions")
            text = "\n\n".join(f'<solution task="{tid}">\n{run.reference(exe, tid)}</solution>' for tid in task_ids())
            out = {"text": text, "stop_reason": "end_turn", "usage": None, "raw": None}
        else:
            out = cfg.client().oneshot(ONESHOT_SYSTEM, prompt)
        elapsed = time.time() - t0

        sol = run.ws / "solutions"
        sol.mkdir(exist_ok=True)
        for tid, code in SOLUTION_RE.findall(out["text"]):
            if tid.strip() in task_ids():
                (sol / f"{tid.strip()}.{run.info['ext']}").write_text(code)
        report = run.grade()

        run_id = make_run_id(cfg, "oneshot", seed)
        meta = base_meta(cfg, run, "oneshot", run_id)
        meta.update({
            "duration_s": round(elapsed, 1), "stop_reason": out["stop_reason"],
            "usage": out["usage"], "cost_usd": (out["usage"] or {}).get("cost_usd_estimate"),
            "model_reported": (out["raw"] or {}).get("model"),
        })
        files = {"prompt.md": prompt, "response.md": out["text"]}
        if out["raw"]:
            files["response.json"] = json.dumps(out["raw"], indent=2, default=str)
        return finish(cfg, RESULTS / run_id, meta, report, sol, files)
    finally:
        run.cleanup()


# ---------------------------------------------------------------- agent

OUTSIDE_RE = re.compile(r"utopia_benchmark|\.\./|(^|\s)~|/Users/|/home/|\bfind\s+/\s|\bcurl\b|\bwget\b|"
                        r"\bpip3?\s+install\b|\bgit\s+clone\b|\bmdfind\b|\blocate\b")


class Workspace:
    """Executes the agent's tools, confined to the workspace, and keeps
    process metrics and an audit trail."""

    OUTPUT_LIMIT = 20_000

    def __init__(self, ws: Path, bin_name):
        self.ws = ws.resolve()
        self.bin_name = bin_name
        (self.ws / ".tmp").mkdir(exist_ok=True)
        # A minimal environment: no API keys, HOME is the workspace.
        self.env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(self.ws),
                    "TMPDIR": str(self.ws / ".tmp"), "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8"}
        self.calls = {}
        self.toolchain_runs = self.toolchain_failed = 0
        self.suspicious = []

    def _path(self, rel):
        p = (self.ws / rel).resolve()
        if not p.is_relative_to(self.ws):
            self.suspicious.append({"path": str(rel)})
            raise PermissionError(f"{rel} is outside the workspace")
        return p

    def _clip(self, text):
        if len(text) <= self.OUTPUT_LIMIT:
            return text
        half = self.OUTPUT_LIMIT // 2
        return text[:half] + f"\n... [{len(text) - self.OUTPUT_LIMIT} characters omitted] ...\n" + text[-half:]

    def execute(self, name, args):
        self.calls[name] = self.calls.get(name, 0) + 1
        try:
            if not isinstance(args, dict):
                return "error: tool input must be an object", True
            if name == "run_shell":
                return self.run_shell(str(args.get("command", "")))
            if name == "read_file":
                p = self._path(str(args.get("path", "")))
                data = p.read_bytes()[:200_000]
                return self._clip(data.decode("utf-8", errors="replace")), False
            if name == "write_file":
                p = self._path(str(args.get("path", "")))
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(str(args.get("content", "")))
                return f"wrote {p.relative_to(self.ws)} ({len(str(args.get('content', '')))} characters)", False
            return f"error: unknown tool {name}", True
        except (OSError, PermissionError, ValueError) as e:
            return f"error: {e}", True

    def run_shell(self, command):
        if OUTSIDE_RE.search(command):
            self.suspicious.append({"command": command[:300]})
        is_run = bool(self.bin_name and re.search(rf"\b{re.escape(self.bin_name)}\s+run\b", command))
        proc = subprocess.Popen(["bash", "-c", command], cwd=self.ws, env=self.env, stdin=subprocess.DEVNULL,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)
        try:
            out, err = proc.communicate(timeout=30)
            status = str(proc.returncode)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            out, err = proc.communicate()
            status = "killed after 30 seconds"
        if is_run:
            self.toolchain_runs += 1
            if status != "0":
                self.toolchain_failed += 1
        text = (f"exit status: {status}\n--- stdout ---\n{out.decode('utf-8', 'replace')}"
                f"--- stderr ---\n{err.decode('utf-8', 'replace')}")
        return self._clip(text), status != "0"

    def metrics(self):
        return {"tool_calls": self.calls, "toolchain_runs": self.toolchain_runs,
                "toolchain_runs_failed": self.toolchain_failed, "suspicious": self.suspicious}


def scripted_client(run, exe):
    if run.cfg.arm == "python":
        raise llm.ProviderError("the scripted provider has no Python solutions")
    script = [("read_file", {"path": "README.md"})]
    for tid in task_ids():
        path = f"solutions/{tid}.{run.info['ext']}"
        script.append(("write_file", {"path": path, "content": run.reference(exe, tid)}))
        script.append(("run_shell", {"command": f"bin/{run.bin_name} run {path} < /dev/null | head -3"}))
    return llm.ScriptedClient(script, "Scripted self-test: wrote the reference solutions.")


def agent_one(cfg, exe, seed, scratch):
    run = Run(cfg, exe, seed, scratch)
    try:
        run_id = make_run_id(cfg, "agent", seed)
        run_dir = RESULTS / run_id
        run_dir.mkdir(parents=True, exist_ok=True)
        transcript = run_dir / "transcript.jsonl"
        print(f"[{run_id}] started", flush=True)

        if cfg.runner == "claude-code":
            import claude_code
            out = claude_code.run_agent(run.ws, transcript, AGENT_PROMPT, cfg.model, cfg.effort, cfg.max_seconds,
                                        cfg.max_cost, cfg.api_key, run.bin_name)
            process = out.pop("process")
        else:
            ws = Workspace(run.ws, run.bin_name)
            client = scripted_client(run, exe) if cfg.provider == "scripted" else cfg.client()
            limits = llm.Limits(cfg.max_steps, cfg.max_cost, cfg.max_seconds)
            with open(transcript, "w") as tf:
                def log(event):
                    tf.write(json.dumps(event, default=str) + "\n")
                    tf.flush()
                try:
                    out = client.agent(AGENT_SYSTEM, AGENT_PROMPT, llm.TOOLS, ws.execute, limits, log)
                except llm.ProviderError as e:
                    # Keep what the agent wrote so far; the run is recorded as an error.
                    out = {"final_text": None, "stop": f"error: {e}", "steps": None, "usage": None, "seconds": None}
                    log({"type": "error", "message": str(e)})
            process = ws.metrics()

        report = run.grade()
        meta = base_meta(cfg, run, "agent", run_id)
        meta.update({
            "duration_s": out.get("seconds"), "stop": out.get("stop"), "timed_out": out.get("stop") in ("timeout", "max_seconds"),
            "num_turns": out.get("steps"), "usage": out.get("usage"),
            "cost_usd": (out.get("usage") or {}).get("cost_usd_estimate"),
            "process": process, "final_message": out.get("final_text"),
            "limits": {"max_steps": cfg.max_steps, "max_cost": cfg.max_cost, "max_seconds": cfg.max_seconds},
        })
        for k in ("stderr_tail", "claude_cli"):
            if k in out:
                meta[k] = out[k]
        # Keep the agent's own files too: they show how it learned.
        for p in run.ws.rglob("*"):
            rel = p.relative_to(run.ws)
            if p.is_file() and rel.parts[0] not in ("bin", "docs", "tasks", ".tmp") and p.stat().st_size < 200_000:
                (run_dir / "workspace" / rel).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(p, run_dir / "workspace" / rel)
        return finish(cfg, run_dir, meta, report, run.ws / "solutions", {"prompt.md": AGENT_PROMPT})
    finally:
        run.cleanup()


# ---------------------------------------------------------------- main

class Config:
    def __init__(self, args):
        for k, v in vars(args).items():
            setattr(self, k, v)
        self.thinking = not args.no_thinking
        self.api_key = None
        if self.provider in DEFAULT_KEY_ENV:
            env = args.api_key_env or DEFAULT_KEY_ENV[self.provider]
            self.api_key = os.environ.get(env)
            if not self.api_key and not (self.runner == "claude-code" and self.mode == "agent"):
                sys.exit(f"error: set {env} (or pass --api-key-env NAME) for provider {self.provider}")
        self.secrets = [os.environ[k] for k in SECRET_ENV if os.environ.get(k)]
        if self.api_key and self.api_key not in self.secrets:
            self.secrets.append(self.api_key)

    def client(self):
        return llm.make_client(self.provider, self.model, self.api_key, self.base_url, self.effort,
                               self.thinking, self.max_tokens, self.price_in, self.price_out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["oneshot", "agent"])
    ap.add_argument("--model", default="claude-opus-5-5")
    ap.add_argument("--provider", choices=["anthropic", "openai", "reference", "scripted"], default="anthropic",
                    help="reference / scripted: offline self-tests that answer with the reference solutions")
    ap.add_argument("--base-url", default=None, help="API endpoint (default: the provider's official one)")
    ap.add_argument("--api-key-env", default=None,
                    help="environment variable holding the key (default ANTHROPIC_API_KEY / OPENAI_API_KEY)")
    ap.add_argument("--arm", choices=["utopia", "python"], default="utopia")
    ap.add_argument("--seeds", default="42", help="e.g. 42 or 1-8 or 3,5,9 (ignored for python)")
    ap.add_argument("--semantics", choices=["random", "standard"], default="random")
    ap.add_argument("--effort", default="high",
                    help="anthropic: output_config.effort; openai: reasoning_effort ('' to omit)")
    ap.add_argument("--no-thinking", action="store_true", help="anthropic: do not request adaptive thinking")
    ap.add_argument("--max-tokens", type=int, default=32000, help="output tokens per request")
    ap.add_argument("--max-steps", type=int, default=150, help="agent: model requests per run")
    ap.add_argument("--max-cost", type=float, default=10.0, help="agent: estimated USD per run")
    ap.add_argument("--max-seconds", type=float, default=3600, help="agent: wall-clock seconds per run")
    ap.add_argument("--price-in", type=float, default=None, help="USD per million input tokens (unlisted models)")
    ap.add_argument("--price-out", type=float, default=None, help="USD per million output tokens (unlisted models)")
    ap.add_argument("--runner", choices=["builtin", "claude-code"], default="builtin",
                    help="agent scaffold: the harness's own loop, or headless Claude Code")
    ap.add_argument("--jobs", type=int, default=4, help="parallel runs")
    ap.add_argument("--out", default=None, help="results directory (default results/runs)")
    args = ap.parse_args()
    args.effort = args.effort or None
    if args.provider in ("reference", "scripted"):
        args.model = args.provider

    global RESULTS
    if args.out:
        RESULTS = Path(args.out).resolve()
    cfg = Config(args)
    seeds = [0] if cfg.arm == "python" else parse_seeds(cfg.seeds)
    scratch = Path(tempfile.mkdtemp(prefix="utopia-run-"))
    exe = scratch / "utopia"
    subprocess.run(["go", "build", "-o", str(exe), "./cmd/utopia"], cwd=ROOT, check=True)
    fn = oneshot_one if cfg.mode == "oneshot" else agent_one

    results = []
    with cf.ThreadPoolExecutor(max_workers=cfg.jobs) as pool:
        futs = {pool.submit(fn, cfg, exe, s, scratch): s for s in seeds}
        for fut in cf.as_completed(futs):
            s = futs[fut]
            try:
                m = fut.result()
            except Exception as e:  # one failed seed should not lose the others
                print(f"seed {s}: FAILED: {e}", file=sys.stderr, flush=True)
                continue
            results.append(m)
            sc = m["score"]
            cost = m.get("cost_usd")
            extra = f"  ${cost:.3f}" if cost is not None else ""
            if m["mode"] == "agent":
                p = m["process"]
                extra += (f"  steps={m.get('num_turns')} runs={p['toolchain_runs']} failed={p['toolchain_runs_failed']}"
                          f" flagged={len(p['suspicious'])} stop={m.get('stop')}")
            print(f"{m['run_id']}: {m['language']:<10} {sc['passed']}/{sc['total']}  {m['duration_s']}s{extra}", flush=True)
    shutil.rmtree(scratch, ignore_errors=True)
    if results:
        tot = sum(m["score"]["passed"] for m in results)
        n = sum(m["score"]["total"] for m in results)
        cost = sum(m.get("cost_usd") or 0 for m in results)
        print(f"\noverall {tot}/{n} tasks ({100 * tot / max(n, 1):.0f}%) over {len(results)} runs, est. cost ${cost:.2f}")
    if len(results) < len(seeds):
        sys.exit(1)


if __name__ == "__main__":
    main()
