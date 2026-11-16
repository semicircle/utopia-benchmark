#!/usr/bin/env python3
"""Grade saved one-shot runs again, without calling any model.

Re-extracts the solutions from each run's response.md with the current
extractor, grades them with a toolchain built from the current source, and
rewrites solutions/, grade.json and the score in meta.json. Use it after a
grading or extraction fix; the model's answer is never changed.

    python3 harness/regrade.py results/runs/RUN_ID [...]
"""

import datetime as dt
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from grade import grade  # noqa: E402
from run import ROOT, TASKS, extract_solutions, git_commit, task_ids  # noqa: E402


def regrade(run_dir: Path, exe: Path):
    meta = json.loads((run_dir / "meta.json").read_text())
    if meta["mode"] != "oneshot":
        raise SystemExit(f"{run_dir.name}: only one-shot runs can be regraded")
    python = meta["arm"] == "python"
    ext = "py" if python else meta["dialect"]["ext"]
    sol = run_dir / "solutions"
    shutil.rmtree(sol, ignore_errors=True)
    sol.mkdir()
    for tid, code in extract_solutions((run_dir / "response.md").read_text(), task_ids()).items():
        (sol / f"{tid}.{ext}").write_text(code)
    cmd = ["python3"] if python else [str(exe), "run", "-seed", str(meta["seed"]), "-semantics", meta["semantics"]]
    report = grade(cmd, TASKS, sol)
    before = meta["score"]["passed"]
    meta["score"] = {"passed": report["passed_tasks"], "total": report["total_tasks"],
                     "tasks": {t["id"]: t["passed"] for t in report["tasks"]}}
    meta.setdefault("regraded", []).append({"date": dt.datetime.now().isoformat(timespec="seconds"),
                                            "commit": git_commit(), "passed_before": before})
    (run_dir / "grade.json").write_text(json.dumps(report, indent=2) + "\n")
    (run_dir / "meta.json").write_text(json.dumps(meta, indent=2, default=str) + "\n")
    print(f"{run_dir.name}: {before} -> {report['passed_tasks']}/{report['total_tasks']}")


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    with tempfile.TemporaryDirectory(prefix="utopia-regrade-") as d:
        exe = Path(d) / "utopia"
        subprocess.run(["go", "build", "-o", str(exe), "./cmd/utopia"], cwd=ROOT, check=True)
        for arg in sys.argv[1:]:
            regrade(Path(arg).resolve(), exe)


if __name__ == "__main__":
    main()
