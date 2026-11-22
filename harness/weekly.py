#!/usr/bin/env python3
"""Weekly model checkup: has any model I pay for quietly got worse?

Runs checkup.py for every enabled entry in harness/roster.toml, one at a
time, through each model's own subscription tool (no API keys), and ends with
a status board: printed here, and saved as Markdown, HTML and JSON.

    python3 harness/weekly.py                 # run everything enabled
    python3 harness/weekly.py --dry-run       # who is logged in, what would run
    python3 harness/weekly.py --no-run        # rebuild the board from saved runs
    python3 harness/weekly.py --only kimi     # entries whose runner or model contains "kimi"

Each entry is compared only with its own history: the same tool, model,
effort and mode. Never read the board across rows; different tools add
different prompts and tools.

Before each entry the tool's login is checked. A tool that is logged out, or
whose run hits a quota or rate limit, is "skipped", not a failed checkup, and
its error runs never enter the history.

Results go to a private folder (default results/private/), not results/runs,
which the public site is built from. Earlier runs in results/runs count as
history but are never written to (--history, --no-history).
"""

import argparse
import datetime as dt
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

DEFAULT_OUT = ROOT / "results" / "private"
DEFAULT_HISTORY = ROOT / "results" / "runs"
QUOTA_RE = re.compile(r"rate.?limit|quota|model fallback|usage limit|limit reached|too many requests|\b429\b|insufficient|"
                      r"exceeded|credits|billing|upgrade|resource.?exhausted|overloaded|capacity", re.I)
LOGIN_RE = re.compile(r"not logged in|log ?in\b|login|authenticat|unauthori[sz]ed|\b401\b|\b403\b|expired|sign.?in",
                      re.I)
DEFAULTS = {"release": "v1", "mode": "oneshot", "repeats": 2, "fresh": 1, "max_seconds": 1800, "enabled": True,
            "effort": None}
TOOL_NAMES = {"claude-code": "Claude Code", "codex": "Codex", "cursor": "Cursor", "kimi": "Kimi Code",
              "gemini": "Gemini CLI", "opencode": "OpenCode", "antigravity": "Antigravity CLI"}


def load_roster(path: Path):
    data = tomllib.loads(path.read_text())
    defaults = {**DEFAULTS, **data.get("defaults", {})}
    out = []
    for i, e in enumerate(data.get("entries", [])):
        entry = {**defaults, **e}
        for k in ("runner", "model"):
            if not entry.get(k):
                sys.exit(f"error: {path}: entry {i + 1} has no {k}")
        if entry["runner"] in ("cursor", "gemini", "antigravity"):
            entry["effort"] = None  # Cursor's and Antigravity's model names carry the effort; Gemini CLI takes none
        out.append(entry)
    return out


def label(e):
    return f"{e['model']}" + (f" ({e['effort']})" if e.get("effort") else "")


def slug(e):
    return re.sub(r"[^A-Za-z0-9.-]+", "-", f"{e['runner']}-{e['model']}-{e.get('effort') or 'default'}-{e['mode']}")


def check_ready(e):
    """None if the tool can run, else why not."""
    r = e["runner"]
    try:
        if r == "claude-code":
            import claude_code
            return claude_code.check_ready(os.environ.get("ANTHROPIC_API_KEY"))
        if r == "codex":
            import codex_agent
            return codex_agent.check_ready()
        if r == "cursor":
            import cursor_agent
            return cursor_agent.check_ready()
        if r == "gemini":
            import gemini_agent
            return gemini_agent.check_ready()
        if r == "kimi":
            import kimi_agent
            return kimi_agent.check_ready(e["model"], e.get("effort"))
        if r == "opencode":
            import opencode_agent
            return opencode_agent.check_ready(e["model"], e.get("effort"))
        if r == "antigravity":
            import antigravity_agent
            return antigravity_agent.check_ready(e["model"])
    except Exception as ex:  # a broken tool is a skip, not a crash
        return f"readiness check failed: {ex}"
    return f"unknown runner {r!r}"


def classify(text):
    if LOGIN_RE.search(text or ""):
        return "logged out"
    if QUOTA_RE.search(text or ""):
        return "quota / rate limit"
    return None


def run_entry(e, args, runs_dir: Path, history, logs: Path):
    summary_path = logs / f"{slug(e)}.summary.json"
    summary_path.unlink(missing_ok=True)
    cmd = [sys.executable, str(HERE / "checkup.py"), "--mode", e["mode"], "--model", e["model"],
           "--runner", e["runner"], "--effort", e.get("effort") or "", "--release", e["release"],
           "--repeats", str(e["repeats"]), "--fresh", str(e["fresh"]), "--out", str(runs_dir),
           "--summary-json", str(summary_path), "--max-seconds", str(args.max_seconds or e["max_seconds"])]
    for h in history:
        cmd += ["--history", str(h)]
    if args.no_run:
        cmd.append("--no-run")
    log = logs / f"{slug(e)}.log"
    print("$", " ".join(cmd[1:]), flush=True)
    with open(log, "w") as lf:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, cwd=ROOT,
                                env={**os.environ, "PYTHONUNBUFFERED": "1"})
        for line in proc.stdout:
            sys.stdout.write(line)
            lf.write(line)
        code = proc.wait()
    try:
        summary = json.loads(summary_path.read_text())
    except (OSError, ValueError):
        summary = None
    return code, summary, log


def status_of(e, summary, code, log):
    """The board's view of one entry: ok / skipped / error, and notes."""
    if summary is None:
        tail = log.read_text()[-2000:] if log.exists() else ""
        why = classify(tail)
        return ("skipped", why) if why else ("error", f"checkup exited with {code}; see {log.name}")
    errors = summary.get("errors") or []
    if errors and not summary.get("runs"):
        text = " ".join(x["error"] for x in errors)
        why = classify(text)
        return ("skipped", f"{why}: {errors[0]['error'][:160]}") if why else ("error", errors[0]["error"][:200])
    if summary.get("verdict") in ("no runs", "no new runs"):
        return "error", summary.get("stopped") or "no runs recorded"
    notes = []
    if errors:
        notes.append(f"{len(errors)} run(s) ended in an error and were left out")
    for w in summary.get("isolation_warnings") or []:
        notes.append(f"isolation: {w}")
    if summary.get("flagged"):
        notes.append(f"{summary['flagged']} tool call(s) flagged")
    return "ok", "; ".join(notes)


def pct(x):
    return "–" if x is None else f"{x * 100:.0f}%"


def build_rows(entries, results):
    rows = []
    for e in entries:
        res = results.get(slug(e), {})
        s = res.get("summary") or {}
        fresh = s.get("fresh_scores") or []
        rows.append({
            "model": label(e), "tool": TOOL_NAMES.get(e["runner"], e["runner"]), "mode": e["mode"],
            "status": res.get("status", "disabled" if not e["enabled"] else "not run"),
            "this_week": s.get("now_mean"), "n_now": s.get("n_now"),
            "history": s.get("base_mean"), "n_base": s.get("n_base"),
            "change": None if s.get("drop_points") is None else -s["drop_points"],
            "p": s.get("p_value"),
            "verdict": s.get("verdict") if res.get("status") == "ok" else
                       res.get("status", "disabled" if not e["enabled"] else "not run"),
            "reported": ", ".join(s.get("models_reported") or []) or "–",
            "fresh": ", ".join(f"{f['passed']}/{f['total']}" for f in fresh) or "–",
            "notes": res.get("notes") or "",
        })
    return rows


COLUMNS = [("Model", "model"), ("Tool", "tool"), ("This week", "this_week"), ("History", "history"),
           ("Change", "change"), ("p", "p"), ("Verdict", "verdict"), ("New language", "fresh"),
           ("Model reported", "reported"), ("Notes", "notes")]


def cell(r, key):
    v = r[key]
    if key == "this_week":
        return f"{pct(v)} (n={r['n_now']})" if v is not None else "–"
    if key == "history":
        return f"{pct(v)} (n={r['n_base']})" if v is not None else "–"
    if key == "change":
        return "–" if v is None else f"{v:+.1f} pts"
    if key == "p":
        return "–" if v is None else f"{v:.3f}"
    return str(v) if v not in (None, "") else "–"


def board_text(rows, when):
    lines = [f"Weekly model checkup, {when}", ""]
    table = [[t for t, _ in COLUMNS[:-1]]] + [[cell(r, k) for _, k in COLUMNS[:-1]] for r in rows]
    widths = [max(len(row[i]) for row in table) for i in range(len(table[0]))]
    for j, row in enumerate(table):
        lines.append("  ".join(c.ljust(w) for c, w in zip(row, widths)).rstrip())
        if j == 0:
            lines.append("  ".join("-" * w for w in widths))
    notes = [f"- {r['model']} via {r['tool']}: {r['notes']}" for r in rows if r["notes"]]
    if notes:
        lines += ["", "Notes:", *notes]
    return "\n".join(lines)


def board_markdown(rows, when):
    out = [f"# Weekly model checkup, {when}", "",
           "Each row is compared only with its own history (same tool, model, effort and mode). "
           "Rows are not comparable with each other.", "",
           "| " + " | ".join(t for t, _ in COLUMNS) + " |", "|" + "---|" * len(COLUMNS)]
    for r in rows:
        out.append("| " + " | ".join(cell(r, k).replace("|", "\\|") for _, k in COLUMNS) + " |")
    out += ["", "Verdicts: **worse** (a drop unlikely to be luck, p < 0.05), **within noise** (lower, but "
            "within run-to-run noise), **no drop**, **baseline** (first checkup). **skipped**: the tool was "
            "logged out or out of quota."]
    return "\n".join(out) + "\n"


def board_html(rows, when):
    head = "".join(f"<th>{html.escape(t)}</th>" for t, _ in COLUMNS)
    body = ""
    for r in rows:
        cls = re.sub(r"[^a-z]+", "-", str(r["verdict"]).lower())
        body += f'<tr class="v-{cls}">' + "".join(f"<td>{html.escape(cell(r, k))}</td>" for _, k in COLUMNS) + "</tr>"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Model checkup {html.escape(when)}</title>
<style>
:root {{ --bg:#fff; --fg:#1a1a1a; --mute:#666; --line:#ddd; --bad:#c62828; --warn:#b26a00; --good:#2e7d32; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#141414; --fg:#eee; --mute:#999; --line:#333;
  --bad:#ef5350; --warn:#ffb74d; --good:#81c784; }} }}
body {{ background:var(--bg); color:var(--fg); font:14px/1.45 system-ui, sans-serif; margin:24px 16px; }}
table {{ border-collapse:collapse; width:100%; }} th, td {{ text-align:left; padding:6px 8px;
  border-bottom:1px solid var(--line); vertical-align:top; }} th {{ color:var(--mute); font-weight:600; }}
.wrap {{ overflow-x:auto; }} p {{ color:var(--mute); max-width:70ch; }}
tr.v-worse td:nth-child(7) {{ color:var(--bad); font-weight:700; }}
tr.v-within-noise td:nth-child(7), tr.v-skipped td:nth-child(7), tr.v-error td:nth-child(7) {{ color:var(--warn); }}
tr.v-no-drop td:nth-child(7) {{ color:var(--good); }}
</style></head><body>
<h1>Weekly model checkup</h1><p>{html.escape(when)}. Each row is compared only with its own history
(same tool, model, effort and mode); rows are not comparable with each other.</p>
<div class="wrap"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>
<p>Verdicts: worse = a drop unlikely to be luck (p &lt; 0.05); within noise = lower, but within run-to-run
noise; no drop; baseline = first checkup. Skipped = the tool was logged out or out of quota.</p>
</body></html>
"""


def notify(rows):
    worse = [r["model"] for r in rows if r["verdict"] == "worse"]
    if not worse or sys.platform != "darwin":
        return
    msg = "Worse than before: " + ", ".join(worse)
    subprocess.run(["osascript", "-e", f"display notification {json.dumps(msg)} with title \"Utopia checkup\""],
                   capture_output=True)


LABEL = "com.utopia.weekly-checkup"


def launchd_plist(out: Path, weekday=0, hour=22, minute=0):
    """A LaunchAgent for this machine: Sunday 22:00 by default. launchd runs a
    missed job when the Mac wakes; caffeinate keeps it awake while it runs."""
    py = ROOT / ".venv" / "bin" / "python"
    py = py if py.exists() else Path(sys.executable)
    tools = ["go", "claude", "cursor-agent", "kimi", "gemini", "opencode", "agy", "node", "git"]
    dirs = []
    for t in tools:
        w = shutil.which(t)
        if w and str(Path(w).parent) not in dirs:
            dirs.append(str(Path(w).parent))
    path = ":".join(dirs + ["/usr/local/bin", "/opt/homebrew/bin", "/usr/bin", "/bin", "/usr/sbin", "/sbin"])
    args = ["/usr/bin/caffeinate", "-i", str(py), str(HERE / "weekly.py"), "--notify", "--out", str(out)]
    x = lambda v: html.escape(str(v))
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>{LABEL}</string>
  <key>ProgramArguments</key>
  <array>
{"".join(f"    <string>{x(a)}</string>{chr(10)}" for a in args)}  </array>
  <key>WorkingDirectory</key><string>{x(ROOT)}</string>
  <key>EnvironmentVariables</key>
  <dict>
    <key>PATH</key><string>{x(path)}</string>
    <key>LANG</key><string>en_US.UTF-8</string>
  </dict>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Weekday</key><integer>{weekday}</integer>
    <key>Hour</key><integer>{hour}</integer>
    <key>Minute</key><integer>{minute}</integer>
  </dict>
  <key>StandardOutPath</key><string>{x(out / "weekly.log")}</string>
  <key>StandardErrorPath</key><string>{x(out / "weekly.log")}</string>
  <key>ProcessType</key><string>Background</string>
</dict>
</plist>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--roster", default=str(HERE / "roster.toml"))
    ap.add_argument("--out", default=os.environ.get("UTOPIA_PRIVATE_RESULTS") or str(DEFAULT_OUT),
                    help="private results folder (default results/private; env UTOPIA_PRIVATE_RESULTS)")
    ap.add_argument("--history", action="append", default=None,
                    help="results folder whose runs count as history, read only (default results/runs; repeatable)")
    ap.add_argument("--no-history", action="store_true", help="use only the runs in --out as history")
    ap.add_argument("--only", action="append", default=[], help="run entries whose runner or model contains this")
    ap.add_argument("--dry-run", action="store_true", help="check logins and show the plan; run nothing")
    ap.add_argument("--no-run", action="store_true", help="no new runs; rebuild the board from saved ones")
    ap.add_argument("--max-seconds", type=float, default=None, help="per run (default from the roster)")
    ap.add_argument("--notify", action="store_true", help="macOS notification when a model looks worse")
    ap.add_argument("--print-launchd", action="store_true",
                    help="print a LaunchAgent plist that runs this every Sunday at 22:00, and exit")
    args = ap.parse_args()

    out = Path(args.out).expanduser().resolve()
    if out == DEFAULT_HISTORY.resolve() or out == (ROOT / "results").resolve():
        sys.exit("error: --out must be a private folder, not results/ or results/runs (they are published)")
    if args.print_launchd:
        print(launchd_plist(out), end="")
        return
    runs_dir = out / "runs"
    history = [] if args.no_history else [Path(h).resolve() for h in (args.history or [DEFAULT_HISTORY])]
    entries = load_roster(Path(args.roster))
    if args.only:
        entries = [e for e in entries if any(o in e["runner"] or o in e["model"] for o in args.only)]
    when = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    logs = out / "logs" / stamp
    for d in (runs_dir, logs, out / "status"):
        d.mkdir(parents=True, exist_ok=True)

    lock = out / ".weekly.lock"
    try:
        fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(fd, str(os.getpid()).encode())
        os.close(fd)
    except FileExistsError:
        pid = lock.read_text().strip()
        if pid.isdigit() and subprocess.run(["kill", "-0", pid], capture_output=True).returncode == 0:
            sys.exit(f"error: another weekly checkup is running (pid {pid})")
        lock.write_text(str(os.getpid()))
    try:
        results = {}
        for e in entries:
            if not e["enabled"]:
                continue
            print(f"\n######## {label(e)} via {TOOL_NAMES.get(e['runner'], e['runner'])} ({e['mode']})", flush=True)
            problem = None if args.no_run else check_ready(e)
            if problem:
                print(f"SKIPPED: {problem}", flush=True)
                results[slug(e)] = {"status": "skipped", "notes": problem}
                continue
            if args.dry_run:
                results[slug(e)] = {"status": "ready", "notes": "logged in (dry run)"}
                continue
            code, summary, log = run_entry(e, args, runs_dir, history, logs)
            status, notes = status_of(e, summary, code, log)
            results[slug(e)] = {"status": status, "notes": notes, "summary": summary, "log": str(log)}

        rows = build_rows(entries, results)
        print("\n" + board_text(rows, when), flush=True)
        if args.dry_run:
            return
        status = out / "status"
        (status / f"{stamp}.md").write_text(board_markdown(rows, when))
        (status / f"{stamp}.html").write_text(board_html(rows, when))
        (status / f"{stamp}.json").write_text(json.dumps({"date": when, "rows": rows, "results": results},
                                                         indent=2, default=str) + "\n")
        for ext in ("md", "html", "json"):
            (status / f"latest.{ext}").write_text((status / f"{stamp}.{ext}").read_text())
        print(f"\nStatus board: {status / 'latest.html'}", flush=True)
        if args.notify:
            notify(rows)
    finally:
        lock.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
