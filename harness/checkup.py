#!/usr/bin/env python3
"""Checkup: has my model got worse? Runs a model on the release's fixed
languages and compares the result with your own earlier runs of the same
setup.

    python3 harness/checkup.py --runner codex --model gpt-6.2-sol --effort high
    python3 harness/checkup.py --runner codex --model gpt-6.2-sol --effort high --no-run   # report only

Every run of the same mode, model, scaffold and effort on the release is one
series. The first checkup records a baseline; later ones are compared with
every earlier run in the series. A single run is noisy (a model that scores
15/17 on average will often score 13 or 17), so the comparison is a
permutation test on per-run scores, within each language: it says how often
a gap this large shows up by chance. A drop only counts when that is rare.

A checkup also runs one brand-new language (--fresh). Its score is reported
apart: a model that keeps doing well on the release's languages but badly on
new ones has learned the release, not the skill.

Runs that ended in an error (logged out, quota or rate limit, no answer)
are kept out of the comparison: they say nothing about the model. After one,
the checkup stops instead of spending the rest of its runs on the same error
(--keep-going to carry on).

--history adds earlier runs kept elsewhere (e.g. results/runs) to the
baseline without writing there. --summary-json writes the result for other
tools (weekly.py).

Any option checkup does not know is passed on to run.py (e.g. --provider,
--base-url, --max-seconds). Runs go one at a time, to stay inside a
subscription's rate limits.
"""

import argparse
import datetime as dt
import itertools
import json
import random
import statistics
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DEFAULT_RUNS = ROOT / "results" / "runs"


def load_runs(*dirs: Path):
    out, seen = [], set()
    for runs_dir in dirs:
        for p in sorted(runs_dir.glob("*/meta.json")):
            try:
                m = json.loads(p.read_text())
            except (OSError, ValueError):
                continue
            if m.get("score") and m["score"].get("total") and m.get("run_id") not in seen:
                seen.add(m.get("run_id"))
                out.append(m)
    return out


def failed(m):
    """Why a run produced no real answer (an error, or a one-shot that timed
    out), else None. Such runs say nothing about the model."""
    stop = str(m.get("stop_reason") if m.get("mode") == "oneshot" else m.get("stop") or "")
    if stop.startswith("error") or (m.get("mode") == "oneshot" and stop == "timeout"):
        return stop + (" | " + m["stderr_tail"][-300:] if m.get("stderr_tail") else "")
    return None


def series_key(m):
    runner = m.get("runner") or "builtin"
    # Cursor's and Antigravity's model names carry the effort, and Gemini CLI takes none; their runs record none.
    effort = None if runner in ("cursor", "gemini", "antigravity") else m.get("effort")
    return (m.get("mode"), m.get("model"), runner, effort)


def same_series(m, key, release):
    return series_key(m) == key and m.get("release") == release


def frac(m):
    """The run's score: the partial score (share of hidden tests passed,
    averaged over tasks) when the run has one, else the share of tasks passed."""
    sc = m["score"]
    return sc["partial"] if "partial" in sc else sc["passed"] / sc["total"]


def drop_test(now, base, rounds=20000, rng=None):
    """One-sided p-value that `now` scores lower than `base` by chance.
    Both are {stratum: [scores]}; labels are shuffled within each stratum
    (exactly when that is cheap). The statistic is the mean over strata of
    mean(base) - mean(now)."""
    strata = [s for s in now if now[s] and base.get(s)]
    if not strata:
        return None, None

    def stat(split):
        return statistics.fmean(statistics.fmean(b) - statistics.fmean(n) for n, b in split)

    observed = stat([(now[s], base[s]) for s in strata])
    pools = [(now[s] + base[s], len(now[s])) for s in strata]
    combos = 1
    for pool, k in pools:
        combos *= len(list(itertools.combinations(range(len(pool)), k))) if len(pool) <= 16 else 10 ** 9
    if combos <= rounds:
        splits = itertools.product(*[itertools.combinations(range(len(pool)), k) for pool, k in pools])
        total = hits = 0
        for choice in splits:
            parts = []
            for (pool, _), idx in zip(pools, choice):
                chosen = set(idx)
                parts.append(([pool[i] for i in idx], [pool[i] for i in range(len(pool)) if i not in chosen]))
            total += 1
            hits += stat(parts) >= observed - 1e-12
        return observed, hits / total
    rng = rng or random.Random(0)
    hits = 0
    for _ in range(rounds):
        parts = []
        for pool, k in pools:
            shuffled = pool[:]
            rng.shuffle(shuffled)
            parts.append((shuffled[:k], shuffled[k:]))
        hits += stat(parts) >= observed - 1e-12
    return observed, (hits + 1) / (rounds + 1)


def task_changes(now, base):
    """Tasks the baseline usually passed that failed now, by language."""
    out = []
    langs = {m["language"] for m in now}
    for lang in sorted(langs):
        b = [m for m in base if m["language"] == lang]
        n = [m for m in now if m["language"] == lang]
        if not b:
            continue
        for tid in sorted(n[0]["score"]["tasks"]):
            b_rate = statistics.fmean(bool(m["score"]["tasks"].get(tid)) for m in b)
            n_rate = statistics.fmean(bool(m["score"]["tasks"].get(tid)) for m in n)
            if b_rate >= 0.75 and n_rate < 0.5:
                out.append(f"{lang}/{tid}: passed in {b_rate:.0%} of earlier runs, {n_rate:.0%} now")
    return out


def bar(x, width=20):
    full = round(x * width)
    return "█" * full + "·" * (width - full)


def run_once(passthrough, extra, runs_dir: Path):
    before = {p.name for p in runs_dir.glob("*")} if runs_dir.exists() else set()
    cmd = [sys.executable, str(HERE / "run.py"), *passthrough, "--jobs", "1", "--out", str(runs_dir), *extra]
    print("$", " ".join(cmd[1:]), flush=True)
    r = subprocess.run(cmd)
    after = {p.name for p in runs_dir.glob("*")} if runs_dir.exists() else set()
    if r.returncode != 0:
        print(f"  (run.py exited with {r.returncode}; keeping whatever finished)", flush=True)
    return sorted(after - before)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mode", choices=["oneshot", "agent"], default="oneshot",
                    help="oneshot (default): one request per language, cheap enough to run often")
    ap.add_argument("--model", required=True)
    ap.add_argument("--runner", default="builtin")
    ap.add_argument("--effort", default="high")
    ap.add_argument("--release", default="v3",
                    help="v3 (default) has the hardest tasks; v1 and v2 are too easy for frontier models to show a decline")
    ap.add_argument("--repeats", type=int, default=2, help="runs of the release per checkup (default 2)")
    ap.add_argument("--fresh", type=int, default=1, help="brand-new languages per checkup (default 1)")
    ap.add_argument("--no-run", action="store_true", help="only report on the runs already saved")
    ap.add_argument("--out", default=None, help="results directory (default results/runs)")
    ap.add_argument("--history", action="append", default=[],
                    help="another results directory whose runs count as history (read only; repeatable)")
    ap.add_argument("--summary-json", default=None, help="also write the summary to this file")
    ap.add_argument("--keep-going", action="store_true", help="do not stop after a run that ended in an error")
    args, rest = ap.parse_known_args()
    runs_dir = Path(args.out).resolve() if args.out else DEFAULT_RUNS
    history = [Path(h).resolve() for h in args.history if Path(h).resolve() != runs_dir]
    effort = args.effort or None
    common = [args.mode, "--model", args.model, "--runner", args.runner, "--effort", args.effort, *rest]

    started = dt.datetime.now().isoformat(timespec="seconds")
    new_ids, fresh_ids, stopped = [], [], None

    def errors_in(ids):
        out = []
        for rid in ids:
            try:
                m = json.loads((runs_dir / rid / "meta.json").read_text())
            except (OSError, ValueError):
                continue
            why = failed(m)
            if why:
                out.append({"run_id": rid, "error": why})
        return out

    if not args.no_run:
        plan = [("release", ["--release", args.release], f"release {args.release}, run {i + 1} of {args.repeats}")
                for i in range(args.repeats)]
        for _ in range(args.fresh):
            seed = random.SystemRandom().randrange(10_000, 1_000_000)
            plan.append(("fresh", ["--seeds", str(seed), "--semantics", "random"], f"new language (seed {seed})"))
        for kind, extra, title in plan:
            print(f"\n== {title}", flush=True)
            ids = run_once(common, extra, runs_dir)
            (new_ids if kind == "release" else fresh_ids).extend(ids)
            errs = errors_in(ids)
            if (errs or not ids) and not args.keep_going:
                stopped = errs[0]["error"] if errs else "run.py saved no run"
                print(f"  Stopping this checkup: {stopped[:300]}", flush=True)
                break
    run_errors = errors_in(new_ids + fresh_ids)
    bad = {e["run_id"] for e in run_errors}
    new_ids = [r for r in new_ids if r not in bad]
    fresh_ids = [r for r in fresh_ids if r not in bad]

    runs = [m for m in load_runs(runs_dir, *history) if not failed(m)]
    # Scaffolds that pick the effort themselves (Cursor) record none: pass --effort '' for them.
    key = series_key({"mode": args.mode, "model": args.model, "runner": args.runner, "effort": effort})
    series = [m for m in runs if same_series(m, key, args.release)]
    series.sort(key=lambda m: m.get("date") or "")
    now = [m for m in series if m["run_id"] in new_ids] if new_ids else []
    if not now and args.no_run and series:
        # Report mode: the latest day's runs against everything before it.
        last_day = series[-1]["date"][:10]
        now = [m for m in series if (m.get("date") or "")[:10] == last_day]
    base = [m for m in series if m not in now]

    label = f"{args.model} {effort or ''} ({args.mode}, runner {args.runner}, release {args.release})".replace("  ", " ")
    print(f"\n==== Checkup: {label}")
    summary = {"date": started, "mode": args.mode, "model": args.model, "runner": args.runner, "effort": effort,
               "release": args.release, "runs": [], "fresh_runs": fresh_ids, "baseline_runs": [],
               "now_mean": None, "base_mean": None, "drop_points": None, "p_value": None,
               "verdict": "no runs", "models_reported": [], "fresh_scores": [], "errors": run_errors,
               "stopped": stopped, "history_dirs": [str(h) for h in history]}
    for e in run_errors:
        print(f"Run {e['run_id']} ended in an error and is left out: {e['error'][:200]}")
    if not series:
        print("No runs of this setup yet.")
        write_summary(args, runs_dir, summary)
        return

    # Which model actually answered.
    wrong = sorted({m.get("model_reported") for m in now if m.get("model_reported")
                    and m["model_reported"] != args.model})
    if wrong:
        print(f"WARNING: the scaffold reports a different model than requested: {', '.join(wrong)}")

    print("\nHistory (each line is one day; per-language mean score):")
    days = {}
    for m in series:
        days.setdefault((m.get("date") or "?")[:10], []).append(m)
    langs = sorted({m["language"] for m in series})
    for day, ms in days.items():
        cells = []
        for lang in langs:
            xs = [frac(m) for m in ms if m["language"] == lang]
            cells.append(f"{lang} {statistics.fmean(xs):4.0%} n={len(xs)}" if xs else f"{lang}   -")
        overall = statistics.fmean(frac(m) for m in ms)
        print(f"  {day}  {bar(overall)} {overall:4.0%}   " + "   ".join(cells))

    verdict, diff, p = ("baseline" if now else "no new runs"), None, None
    if now and base:
        by = lambda ms: {lang: [frac(m) for m in ms if m["language"] == lang] for lang in langs}
        diff, p = drop_test(by(now), by(base))
        if diff is None:
            verdict = "no overlap"
            print("\nThe new runs share no language with the earlier ones; nothing to compare.")
        else:
            n_now, n_base = len(now), len(base)
            print(f"\nNow: {statistics.fmean(frac(m) for m in now):.0%} over {n_now} runs. "
                  f"Before: {statistics.fmean(frac(m) for m in base):.0%} over {n_base} runs.")
            print(f"Change, averaged over languages: {-diff * 100:+.1f} points. "
                  f"Chance of a drop at least this large by luck: p = {p:.3f}")
            if diff > 0 and p < 0.05:
                verdict = "worse"
                print("VERDICT: worse than your earlier runs, and unlikely to be luck.")
            elif diff > 0:
                verdict = "within noise"
                print("VERDICT: a little lower, but within the usual run-to-run noise. "
                      "Run more checkups before concluding anything.")
            else:
                verdict = "no drop"
                print("VERDICT: no sign of a drop.")
            changes = task_changes(now, base)
            if changes:
                print("Tasks that stopped passing:")
                for c in changes:
                    print("  " + c)
            if n_base < 4:
                print(f"(Only {n_base} earlier runs: the comparison gets sharper as the history grows.)")
    elif now:
        print("\nFirst checkup of this setup: these runs are your baseline. Run it again later to compare.")

    fresh = [m for m in runs if m["run_id"] in fresh_ids]
    summary.update({
        "runs": [m["run_id"] for m in now], "baseline_runs": [m["run_id"] for m in base],
        "now_mean": round(statistics.fmean(frac(m) for m in now), 4) if now else None,
        "base_mean": round(statistics.fmean(frac(m) for m in base), 4) if base else None,
        "n_now": len(now), "n_base": len(base),
        "drop_points": None if diff is None else round(diff * 100, 1),
        "p_value": None if p is None else round(p, 4), "verdict": verdict,
        "models_reported": sorted({m.get("model_reported") for m in now if m.get("model_reported")}),
        "fresh_scores": [{"run_id": m["run_id"], "language": m["language"], "seed": m["seed"],
                          "passed": m["score"]["passed"], "total": m["score"]["total"]} for m in fresh],
        "isolation_warnings": sorted({w for m in now + fresh for w in (m.get("process") or {}).get("isolation_warnings") or []}),
        "flagged": sum(len((m.get("process") or {}).get("suspicious") or []) for m in now + fresh),
    })
    for m in fresh:
        print(f"\nNew language {m['language']} (seed {m['seed']}): {m['score']['passed']}/{m['score']['total']}")
    if fresh and now:
        gap = statistics.fmean(frac(m) for m in now) - statistics.fmean(frac(m) for m in fresh)
        if gap > 0.25:
            print("  Much lower than on the release languages. One language is noisy, but if this keeps "
                  "happening the model may have learned the release itself.")

    write_summary(args, runs_dir, summary)


def write_summary(args, runs_dir: Path, summary):
    if args.summary_json:
        Path(args.summary_json).parent.mkdir(parents=True, exist_ok=True)
        Path(args.summary_json).write_text(json.dumps(summary, indent=2) + "\n")
    if args.no_run:
        return
    checkups = runs_dir.parent / "checkups"
    checkups.mkdir(parents=True, exist_ok=True)
    stamp = time.strftime("%Y%m%d-%H%M%S")
    name = f"{stamp}-{args.mode}-{args.runner}-{args.model}-{summary['effort'] or 'default'}.json".replace("/", "-")
    (checkups / name).write_text(json.dumps(summary, indent=2) + "\n")
    print(f"\nSaved {checkups / name}")


if __name__ == "__main__":
    main()
