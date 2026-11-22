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
from grade import grade, score_of  # noqa: E402

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
FENCE_RE = re.compile(r"\A\s*```[^\n]*\n(.*?)\n?```\s*\Z", re.S)


def extract_solutions(text, ids):
    """Solutions from a one-shot answer, by task id. A Markdown code fence
    wrapped around the code inside the tag is removed: the benchmark measures
    the language, not the answer format."""
    out = {}
    for tid, code in SOLUTION_RE.findall(text):
        tid = tid.strip()
        if tid in ids:
            m = FENCE_RE.match(code)
            out[tid] = m.group(1) + "\n" if m else code
    return out
DEFAULT_KEY_ENV = {"anthropic": "ANTHROPIC_API_KEY", "openai": "OPENAI_API_KEY"}
SECRET_ENV = ("ANTHROPIC_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CLAUDE_CODE_OAUTH_TOKEN", "OPENAI_API_KEY", "CURSOR_API_KEY")
# Agent scaffolds other than the harness's own loop. They bring their own login.
EXTERNAL_RUNNERS = ("claude-code", "cursor", "codex", "kimi", "gemini", "opencode", "antigravity")
# Runners that can also do one-shot runs.
ONESHOT_RUNNERS = ("builtin", *EXTERNAL_RUNNERS)
# Runners whose run ids carry the effort (Cursor's model names carry it already).
EFFORT_IN_ID = ("codex", "claude-code", "kimi", "opencode")


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


# A release fixes its tasks as well as its languages; set from --release.
RELEASE_TASKS = None


def task_ids():
    ids = sorted(p.name for p in TASKS.iterdir() if (p / "task.md").exists())
    if RELEASE_TASKS is not None:
        ids = [t for t in ids if t in RELEASE_TASKS]
    return ids


def git_commit():
    r = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip() or None


def make_run_id(cfg, mode, seed):
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    model = re.sub(r"[^A-Za-z0-9.-]+", "-", cfg.model.replace("claude-", ""))
    tag = "py" if cfg.arm == "python" else f"s{seed}-{cfg.semantics}"
    if cfg.runner != "builtin":
        mode = f"{mode}-{cfg.runner}"
    if cfg.runner in EFFORT_IN_ID and cfg.effort:
        model += f"-{cfg.effort}"
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
        keep = set(task_ids())
        for p in (self.ws / "tasks").glob("*.md"):
            if p.stem not in keep:
                p.unlink()

    def grade(self):
        """Grade the workspace's solutions with a toolchain built just now, in a
        directory the agent never saw."""
        sol = self.ws / "solutions"
        if self.cfg.arm == "python":
            return grade(["python3"], TASKS, sol, only=set(task_ids()))
        with tempfile.TemporaryDirectory(prefix="utopia-grader-") as d:
            exe = Path(d) / "utopia"
            subprocess.run(["go", "build", "-o", str(exe), "./cmd/utopia"], cwd=ROOT, check=True)
            return grade([str(exe), "run", "-seed", str(self.seed), "-semantics", self.cfg.semantics], TASKS, sol,
                         only=set(task_ids()))

    def reference(self, exe, tid):
        return subprocess.run([str(exe), "render", "-seed", str(self.seed), "-semantics", self.cfg.semantics,
                               str(TASKS / tid / "solution.canon")], capture_output=True, text=True, check=True).stdout

    def cleanup(self):
        shutil.rmtree(self.dir, ignore_errors=True)


def base_meta(cfg, run, mode, run_id):
    return {
        "run_id": run_id, "mode": mode, "arm": cfg.arm,
        "provider": cfg.provider, "base_url": cfg.base_url, "model": cfg.model,
        "runner": cfg.runner if (mode == "agent" or cfg.runner != "builtin") else None,
        "effort": cfg.effort, "thinking": cfg.thinking, "max_tokens": cfg.max_tokens,
        "seed": None if cfg.arm == "python" else run.seed,
        "semantics": None if cfg.arm == "python" else cfg.semantics,
        "release": cfg.release,
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
    meta["score"] = score_of(report)
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


def external_oneshot(cfg, run_dir, prompt):
    """A one-shot answer through a subscription tool, with its tools off."""
    if cfg.runner == "codex":
        import codex_agent
        return codex_agent.run_oneshot(run_dir, prompt, cfg.model, cfg.effort, cfg.max_seconds, cfg.price_in, cfg.price_out)
    if cfg.runner == "claude-code":
        import claude_code
        return claude_code.run_oneshot(run_dir, prompt, cfg.model, cfg.effort, cfg.max_seconds, cfg.api_key)
    if cfg.runner == "cursor":
        import cursor_agent
        return cursor_agent.run_oneshot(run_dir, prompt, cfg.model, cfg.max_seconds, cfg.price_in, cfg.price_out)
    if cfg.runner == "gemini":
        import gemini_agent
        return gemini_agent.run_oneshot(run_dir, prompt, cfg.model, cfg.max_seconds, cfg.price_in, cfg.price_out)
    if cfg.runner == "kimi":
        import kimi_agent
        return kimi_agent.run_oneshot(run_dir, prompt, cfg.model, cfg.effort, cfg.max_seconds, cfg.price_in, cfg.price_out)
    if cfg.runner == "opencode":
        import opencode_agent
        return opencode_agent.run_oneshot(run_dir, prompt, cfg.model, cfg.effort, cfg.max_seconds, cfg.price_in,
                                          cfg.price_out)
    if cfg.runner == "antigravity":
        import antigravity_agent
        return antigravity_agent.run_oneshot(run_dir, prompt, cfg.model, cfg.max_seconds, cfg.price_in, cfg.price_out)
    raise ValueError(cfg.runner)


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
        elif cfg.runner in EXTERNAL_RUNNERS:
            run_id = make_run_id(cfg, "oneshot", seed)
            out = external_oneshot(cfg, RESULTS / run_id, prompt)
        else:
            out = cfg.client().oneshot(ONESHOT_SYSTEM, prompt)
        elapsed = out.pop("seconds", None) or time.time() - t0

        sol = run.ws / "solutions"
        sol.mkdir(exist_ok=True)
        for tid, code in extract_solutions(out["text"], task_ids()).items():
            (sol / f"{tid}.{run.info['ext']}").write_text(code)
        report = run.grade()

        if cfg.runner not in EXTERNAL_RUNNERS or cfg.provider == "reference":
            run_id = make_run_id(cfg, "oneshot", seed)
        meta = base_meta(cfg, run, "oneshot", run_id)
        meta.update({
            "duration_s": round(elapsed, 1), "stop_reason": out["stop_reason"],
            "usage": out["usage"], "cost_usd": (out["usage"] or {}).get("cost_usd_estimate"),
            "model_reported": (out["raw"] or {}).get("model"),
        })
        if "process" in out:
            meta["process"] = out["process"]
            meta["model_reported"] = out["process"].get("model_reported")
        for k in out:
            if k == "stderr_tail" or k.endswith("_cli"):
                meta[k] = out[k]
        files = {"prompt.md": prompt, "response.md": out["text"]}
        if out["raw"]:
            files["response.json"] = json.dumps(out["raw"], indent=2, default=str)
        return finish(cfg, RESULTS / run_id, meta, report, sol, files)
    finally:
        run.cleanup()


# ---------------------------------------------------------------- agent

OUTSIDE_RE = re.compile(r"utopia_benchmark|\.\./\.\.|(^|\s)~|/Users/|/home/|\bfind\s+/\s|\bcurl\b|\bwget\b|"
                        r"\bpip3?\s+install\b|\bgit\s+clone\b|\bmdfind\b|\blocate\b")


class Workspace:
    """Executes the agent's tools, confined to the workspace, and keeps
    process metrics and an audit trail."""

    OUTPUT_LIMIT = 20_000

    def __init__(self, ws: Path, bin_name, trace: Path):
        self.ws = ws.resolve()
        self.trace = trace
        self.bin_name = bin_name
        (self.ws / ".tmp").mkdir(exist_ok=True)
        # A minimal environment: no API keys, HOME is the workspace.
        self.env = {"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(self.ws),
                    "TMPDIR": str(self.ws / ".tmp"), "LANG": "C.UTF-8", "LC_ALL": "C.UTF-8",
                    "UTOPIA_TRACE": str(trace)}
        self.calls = {}
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
        proc = subprocess.Popen(["bash", "-c", command], cwd=self.ws, env=self.env, stdin=subprocess.DEVNULL,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)
        try:
            out, err = proc.communicate(timeout=30)
            status = str(proc.returncode)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            out, err = proc.communicate()
            status = "killed after 30 seconds"
        text = (f"exit status: {status}\n--- stdout ---\n{out.decode('utf-8', 'replace')}"
                f"--- stderr ---\n{err.decode('utf-8', 'replace')}")
        return self._clip(text), status != "0"

    def metrics(self):
        runs = []
        if self.trace.exists():
            for line in self.trace.read_text().splitlines():
                try:
                    runs.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        return {"tool_calls": self.calls,
                "toolchain_runs": sum(r.get("cmd") == "run" for r in runs),
                "toolchain_runs_failed": sum(r.get("cmd") == "run" and r.get("exit") != 0 for r in runs),
                "toolchain_checks": sum(r.get("cmd") == "check" for r in runs),
                "suspicious": self.suspicious}


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
        elif cfg.runner == "cursor":
            import cursor_agent
            out = cursor_agent.run_agent(run.ws, transcript, AGENT_PROMPT, cfg.model, cfg.max_seconds,
                                         cfg.cursor_sandbox, cfg.price_in, cfg.price_out)
            process = out.pop("process")
        elif cfg.runner == "codex":
            import codex_agent
            out = codex_agent.run_agent(run.ws, transcript, AGENT_PROMPT, cfg.model, cfg.effort, cfg.max_seconds,
                                        cfg.price_in, cfg.price_out)
            process = out.pop("process")
        elif cfg.runner == "gemini":
            import gemini_agent
            out = gemini_agent.run_agent(run.ws, transcript, AGENT_PROMPT, cfg.model, cfg.max_seconds,
                                         cfg.price_in, cfg.price_out)
            process = out.pop("process")
        elif cfg.runner == "kimi":
            import kimi_agent
            out = kimi_agent.run_agent(run.ws, transcript, AGENT_PROMPT, cfg.model, cfg.effort, cfg.max_seconds,
                                       cfg.price_in, cfg.price_out)
            process = out.pop("process")
        elif cfg.runner == "opencode":
            import opencode_agent
            out = opencode_agent.run_agent(run.ws, transcript, AGENT_PROMPT, cfg.model, cfg.effort, cfg.max_seconds,
                                           cfg.price_in, cfg.price_out)
            process = out.pop("process")
        elif cfg.runner == "antigravity":
            import antigravity_agent
            out = antigravity_agent.run_agent(run.ws, transcript, AGENT_PROMPT, cfg.model, cfg.max_seconds,
                                              cfg.price_in, cfg.price_out)
            process = out.pop("process")
        else:
            ws = Workspace(run.ws, run.bin_name, run.dir / "trace.jsonl")
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
        if process.get("model_reported"):
            meta["model_reported"] = process["model_reported"]
        for k in out:
            if k == "stderr_tail" or k.endswith("_cli"):
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
        if self.runner in ("cursor", "gemini", "antigravity"):
            # The tool picks the provider, effort and output limit from the model name.
            self.provider, self.base_url = self.runner, None
            self.effort = self.thinking = self.max_tokens = None
        elif self.runner in ("codex", "kimi", "opencode"):
            # Billed to the plan; the tool sets the output limit. Effort is passed on.
            self.provider, self.base_url = self.runner, None
            self.thinking = self.max_tokens = None
            self.max_steps = self.max_cost = None
        if self.provider in DEFAULT_KEY_ENV:
            env = args.api_key_env or DEFAULT_KEY_ENV[self.provider]
            self.api_key = os.environ.get(env)
            if not self.api_key and self.runner not in EXTERNAL_RUNNERS:
                sys.exit(f"error: set {env} (or pass --api-key-env NAME) for provider {self.provider}")
        self.secrets = [os.environ[k] for k in SECRET_ENV if os.environ.get(k)]
        if self.runner == "codex":
            import codex_agent
            self.secrets += codex_agent.login_secrets()
        if self.runner == "kimi":
            import kimi_agent
            self.secrets += kimi_agent.login_secrets()
        if self.runner == "gemini":
            import gemini_agent
            self.secrets += gemini_agent.login_secrets()
        if self.runner == "opencode":
            import opencode_agent
            self.secrets += opencode_agent.login_secrets()
        if self.runner == "antigravity":
            import antigravity_agent
            self.secrets += antigravity_agent.login_secrets()
        if self.api_key and self.api_key not in self.secrets:
            self.secrets.append(self.api_key)

    def client(self):
        return llm.make_client(self.provider, self.model, self.api_key, self.base_url, self.effort,
                               self.thinking, self.max_tokens, self.price_in, self.price_out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["oneshot", "agent"])
    ap.add_argument("--model", default=None,
                    help="default claude-opus-5-5; with --runner cursor, a name from `cursor-agent models`; "
                         "with --runner codex, a model your ChatGPT plan offers (e.g. gpt-6.2-sol)")
    ap.add_argument("--provider", choices=["anthropic", "openai", "reference", "scripted"], default="anthropic",
                    help="reference / scripted: offline self-tests that answer with the reference solutions")
    ap.add_argument("--base-url", default=None, help="API endpoint (default: the provider's official one)")
    ap.add_argument("--api-key-env", default=None,
                    help="environment variable holding the key (default ANTHROPIC_API_KEY / OPENAI_API_KEY)")
    ap.add_argument("--arm", choices=["utopia", "python"], default="utopia")
    ap.add_argument("--seeds", default="42", help="e.g. 42 or 1-8 or 3,5,9 (ignored for python)")
    ap.add_argument("--semantics", choices=["random", "standard"], default="random")
    ap.add_argument("--release", default=None,
                    help="run a published release's fixed languages (e.g. v1); sets --seeds and --semantics")
    ap.add_argument("--effort", default="high",
                    help="anthropic: output_config.effort; openai and codex: reasoning effort ('' to omit)")
    ap.add_argument("--no-thinking", action="store_true", help="anthropic: do not request adaptive thinking")
    ap.add_argument("--max-tokens", type=int, default=32000, help="output tokens per request")
    ap.add_argument("--max-steps", type=int, default=150, help="agent: model requests per run")
    ap.add_argument("--max-cost", type=float, default=10.0, help="agent: estimated USD per run")
    ap.add_argument("--max-seconds", type=float, default=3600,
                    help="wall-clock seconds per run (agent; one-shot through an external runner)")
    ap.add_argument("--price-in", type=float, default=None, help="USD per million input tokens (unlisted models)")
    ap.add_argument("--price-out", type=float, default=None, help="USD per million output tokens (unlisted models)")
    ap.add_argument("--runner", choices=["builtin", *EXTERNAL_RUNNERS], default="builtin",
                    help="scaffold: the harness's own loop (API key), or a subscription tool with its own login: "
                         "headless Claude Code, Cursor's agent CLI, Codex (from the ChatGPT desktop app) or "
                         "Kimi Code, Gemini CLI, OpenCode or the Antigravity CLI. All of them do agent and "
                         "one-shot runs.")
    ap.add_argument("--cursor-sandbox", choices=["enabled", "disabled"], default="enabled",
                    help="cursor: run the agent's shell commands in Cursor's sandbox (no network, "
                         "writes only in the workspace)")
    ap.add_argument("--jobs", type=int, default=4, help="parallel runs")
    ap.add_argument("--out", default=None, help="results directory (default results/runs)")
    args = ap.parse_args()
    args.effort = args.effort or None
    if args.mode == "oneshot" and args.runner not in ONESHOT_RUNNERS:
        sys.exit(f"error: --runner {args.runner} applies to agent mode")
    if args.runner == "codex":
        import codex_agent
        problem = codex_agent.check_ready()
        if problem:
            sys.exit(f"error: {problem}")
        if args.model is None:
            names = ", ".join(codex_agent.models()) or "see `codex debug models`"
            sys.exit(f"error: pass --model with a model Codex offers: {names}")
    if args.runner == "kimi":
        import kimi_agent
        if args.model is None:
            args.model = kimi_agent.default_model()
        problem = kimi_agent.check_ready(args.model, args.effort)
        if problem:
            sys.exit(f"error: {problem}")
    if args.runner == "gemini":
        import gemini_agent
        problem = gemini_agent.check_ready()
        if problem:
            sys.exit(f"error: {problem}")
        if args.model is None:
            sys.exit("error: pass --model with a Gemini model your account offers (gemini --list-models)")
    if args.runner in ("opencode", "antigravity"):
        if args.model is None:
            sys.exit("error: pass --model: provider/model from `opencode models`" if args.runner == "opencode"
                     else "error: pass --model with a name from `agy models` (e.g. gemini-4-argon-high)")
        if args.runner == "opencode":
            import opencode_agent as agent_mod
        else:
            import antigravity_agent as agent_mod
        problem = (agent_mod.check_ready(args.model, args.effort) if args.runner == "opencode"
                   else agent_mod.check_ready(args.model))
        if problem:
            sys.exit(f"error: {problem}")
    if args.runner == "cursor":
        import cursor_agent
        problem = cursor_agent.check_ready()
        if problem:
            sys.exit(f"error: {problem}")
    if args.model is None:
        if args.runner == "cursor":
            sys.exit("error: pass --model with a name from `cursor-agent models`")
        args.model = "claude-opus-5-5"
    if args.release:
        rel_path = ROOT / "releases" / args.release / "release.json"
        if not rel_path.exists():
            sys.exit(f"error: no release {args.release!r} (expected {rel_path})")
        if args.arm != "utopia":
            sys.exit("error: --release applies to the utopia arm")
        rel = json.loads(rel_path.read_text())
        args.seeds = ",".join(str(l["seed"]) for l in rel["languages"])
        args.semantics = rel["semantics"]
        global RELEASE_TASKS
        RELEASE_TASKS = set(rel["tasks"])
        missing = RELEASE_TASKS - set(task_ids())
        if missing:
            sys.exit(f"error: release {args.release} lists tasks that do not exist: {', '.join(sorted(missing))}")
        for k, v in rel.get("protocol", {}).items():  # every model gets the same budget
            setattr(args, k, v)
    if args.provider in ("reference", "scripted"):
        args.model = args.provider

    global RESULTS
    if args.out:
        RESULTS = Path(args.out).resolve()
    cfg = Config(args)
    if cfg.runner == "claude-code":
        import claude_code
        problem = claude_code.check_ready(cfg.api_key)
        if problem:
            sys.exit(f"error: {problem}")
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
