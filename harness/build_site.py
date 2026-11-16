#!/usr/bin/env python3
"""Build the static results website from results/runs/*/meta.json.

Usage:
    python3 harness/build_site.py [--out _site] [--include-selftest]

Writes OUT/index.html (all data inlined, works from file://) and copies each
run's prompt, response or transcript and solutions to OUT/runs/RUN_ID/ so the
site is self-contained. Deploy OUT as-is (GitHub Pages, Netlify, any host).
"""

import argparse
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "results" / "runs"
TEMPLATE = Path(__file__).resolve().parent / "site_template.html"

STANDARD = {
    "ArgOrder": "left-to-right", "OperandOrder": "left-to-right", "Div": "toward-zero",
    "IndexBase": 0, "OutOfRange": "error", "CountInclusive": True, "ShortCircuit": True,
    "SwitchFallthrough": False, "ListEqStructural": True, "Prec": "standard",
}

FRIEND_LABELS = {
    "ArgOrder": lambda v: f"arguments evaluated {v}",
    "OperandOrder": lambda v: f"operands evaluated {v}",
    "Div": lambda v: f"division rounds {v}",
    "IndexBase": lambda v: f"indices start at {v}",
    "OutOfRange": lambda v: f"out-of-range index: {v}",
    "CountInclusive": lambda v: "counting loops " + ("include" if v else "exclude") + " the end",
    "ShortCircuit": lambda v: "and/or " + ("short-circuit" if v else "always evaluate both sides"),
    "SwitchFallthrough": lambda v: "switch cases " + ("fall through" if v else "do not fall through"),
    "ListEqStructural": lambda v: "list == compares " + ("contents" if v else "identity"),
    "Prec": lambda v: {"flat-left": "no precedence, left to right",
                       "flat-right": "no precedence, right to left"}.get(v, f"precedence: {v}"),
}

KEEP_FILES = ("prompt.md", "response.md", "transcript.jsonl", "grade.json", "meta.json")


def false_friends(sem):
    if not sem:
        return []
    return [FRIEND_LABELS[k](v) for k, v in sem.items() if k in STANDARD and STANDARD[k] != v]


def total_tokens(usage):
    if not usage:
        return None
    keys = ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")
    return sum(usage.get(k) or 0 for k in keys)


def slim(meta, files):
    d = meta.get("dialect") or {}
    p = meta.get("process") or {}
    u = meta.get("usage") or {}
    return {
        "id": meta["run_id"], "mode": meta["mode"], "arm": meta["arm"], "model": meta["model"],
        "seed": meta.get("seed"), "semantics": meta.get("semantics"), "language": meta.get("language"),
        "date": meta.get("date"), "duration_s": meta.get("duration_s"),
        "passed": meta["score"]["passed"], "total": meta["score"]["total"], "tasks": meta["score"]["tasks"],
        "styles": d.get("styles"), "friends": false_friends(d.get("semantics")),
        "tokens": total_tokens(u), "output_tokens": u.get("output_tokens"),
        "turns": meta.get("num_turns"),
        "runs": p.get("toolchain_runs"), "runs_failed": p.get("toolchain_runs_failed"),
        "suspicious": len(p.get("suspicious") or []),
        "timed_out": meta.get("timed_out", False),
        "final_message": meta.get("final_message"),
        "files": files,
    }


def samples(seeds=(2, 5, 13, 19)):
    """The FizzBuzz reference solution rendered into a few dialects."""
    out = []
    with tempfile.TemporaryDirectory() as tmp:
        exe = Path(tmp) / "utopia"
        subprocess.run(["go", "build", "-o", str(exe), "./cmd/utopia"], cwd=ROOT, check=True)
        canon = ROOT / "tasks" / "t0-fizzbuzz" / "solution.canon"
        out.append({"name": "Canonical (for reference)", "code": canon.read_text()})
        for s in seeds:
            info = json.loads(subprocess.run([str(exe), "info", "-seed", str(s)], capture_output=True,
                                             text=True, check=True).stdout)
            code = subprocess.run([str(exe), "render", "-seed", str(s), str(canon)], capture_output=True,
                                  text=True, check=True).stdout
            out.append({"name": f"{info['name']} (seed {s})", "code": code})
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=str(ROOT / "_site"))
    ap.add_argument("--include-selftest", action="store_true", help='include model "reference" runs')
    args = ap.parse_args()
    out = Path(args.out)
    if out.exists():
        shutil.rmtree(out)
    (out / "runs").mkdir(parents=True)

    runs = []
    for meta_path in sorted(RUNS.glob("*/meta.json")) if RUNS.exists() else []:
        meta = json.loads(meta_path.read_text())
        if meta["model"] == "reference" and not args.include_selftest:
            continue
        src = meta_path.parent
        dst = out / "runs" / src.name
        dst.mkdir()
        files = []
        for name in KEEP_FILES:
            if (src / name).exists():
                shutil.copy2(src / name, dst / name)
                files.append(name)
        for sub in ("solutions", "workspace"):
            if (src / sub).exists():
                shutil.copytree(src / sub, dst / sub)
                files += [f"{sub}/{p.relative_to(src / sub)}" for p in sorted((src / sub).rglob("*")) if p.is_file()]
        runs.append(slim(meta, files))

    notes_path = ROOT / "results" / "notes.md"
    notes = notes_path.read_text() if notes_path.exists() else ""
    data = {"runs": runs, "samples": samples(), "notes": notes}
    page = TEMPLATE.read_text().replace("/*__DATA__*/null", json.dumps(data).replace("</", "<\\/"))
    (out / "index.html").write_text(page)
    (out / ".nojekyll").write_text("")
    print(f"wrote {out / 'index.html'} with {len(runs)} runs")


if __name__ == "__main__":
    main()
