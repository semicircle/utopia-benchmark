#!/usr/bin/env python3
"""Grade solutions to Utopia tasks against their hidden tests.

Usage:
    python3 harness/grade.py --bin WORKSPACE/bin/LANG --tasks tasks --solutions WORKSPACE/solutions
    python3 harness/grade.py --python --solutions DIR      # Python control arm

Each task directory under --tasks holds tests/NN.in (optional) and tests/NN.out.
The solution for task ID is the file in --solutions named ID.<ext>. A test passes
when the program exits with status 0 and its standard output equals NN.out exactly.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path


def find_solution(solutions: Path, task_id: str):
    matches = sorted(p for p in solutions.glob(task_id + ".*") if p.is_file())
    return matches[0] if matches else None


def run_test(command: list, solution: Path, stdin: bytes, timeout: float):
    try:
        proc = subprocess.run(
            command + [str(solution)],
            input=stdin,
            capture_output=True,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return None, b"", b"timeout"
    return proc.returncode, proc.stdout, proc.stderr


def grade(command: list, tasks_dir, solutions, timeout: float = 10.0, only=None):
    """Run every solution against its hidden tests.

    command is the program prefix that runs one solution file, for example
    ["bin/wuksa", "run"] or ["python3"]. only, if given, limits grading to
    those task IDs.
    """
    tasks_dir, solutions = Path(tasks_dir), Path(solutions)
    report = {"tasks": [], "passed_tasks": 0, "total_tasks": 0}
    for task in sorted(p for p in tasks_dir.iterdir() if p.is_dir()):
        if only is not None and task.name not in only:
            continue
        outs = sorted((task / "tests").glob("*.out"))
        if not outs:
            continue
        entry = {"id": task.name, "tests": [], "passed": False}
        solution = find_solution(solutions, task.name)
        if solution is None:
            entry["error"] = "no solution file"
        else:
            for out in outs:
                inp = out.with_suffix(".in")
                stdin = inp.read_bytes() if inp.exists() else b""
                code, stdout, stderr = run_test(command, solution, stdin, timeout)
                ok = code == 0 and stdout == out.read_bytes()
                test = {"name": out.stem, "passed": ok}
                if not ok:
                    test["exit"] = code
                    test["stderr"] = stderr.decode(errors="replace")[-500:]
                    test["stdout_head"] = stdout.decode(errors="replace")[:300]
                entry["tests"].append(test)
            entry["passed"] = all(t["passed"] for t in entry["tests"])
        report["tasks"].append(entry)
        report["total_tasks"] += 1
        report["passed_tasks"] += entry["passed"]
    return report


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--bin", help="the dialect's toolchain binary")
    ap.add_argument("--python", action="store_true", help="grade Python solutions with python3")
    ap.add_argument("--tasks", default="tasks", help="task directory with hidden tests")
    ap.add_argument("--solutions", required=True, help="directory of solution files")
    ap.add_argument("--timeout", type=float, default=10.0, help="seconds per test")
    ap.add_argument("--json", action="store_true", help="print the full report as JSON")
    args = ap.parse_args()
    if args.python == bool(args.bin):
        ap.error("give exactly one of --bin or --python")

    command = ["python3"] if args.python else [args.bin, "run"]
    report = grade(command, args.tasks, args.solutions, args.timeout)
    if args.json:
        json.dump(report, sys.stdout, indent=2)
        print()
    else:
        for t in report["tasks"]:
            n_ok = sum(x["passed"] for x in t["tests"])
            status = "PASS" if t["passed"] else "FAIL"
            detail = t.get("error") or f"{n_ok}/{len(t['tests'])} tests"
            print(f"{status}  {t['id']:<20} {detail}")
            for x in t["tests"]:
                if not x["passed"] and x.get("stderr", "").strip():
                    print(f"      {x['name']}: {x['stderr'].strip().splitlines()[-1]}")
        print(f"\n{report['passed_tasks']}/{report['total_tasks']} tasks passed")
    sys.exit(0 if report["passed_tasks"] == report["total_tasks"] else 1)


if __name__ == "__main__":
    main()
