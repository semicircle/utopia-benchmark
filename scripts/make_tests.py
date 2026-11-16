#!/usr/bin/env python3
"""Generate hidden tests for the T1 and T2 tasks.

Each task here has a reference implementation in Python, independent of its
canonical Utopia solution, and a list of test inputs: hand-written edge cases
plus seeded random ones. Running this script rewrites tasks/ID/tests/NN.in
and NN.out. `go test ./internal/tasks` then checks that every canonical
solution reproduces these outputs in hundreds of generated dialects, so the
two implementations check each other.

    python3 scripts/make_tests.py
"""

import random
import string
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "tasks"
TASKS = {}


def task(name):
    def wrap(fn):
        TASKS[name] = fn
        return fn
    return wrap


def lines(text):
    return "".join(x + "\n" for x in text)


def trunc_div(a, b):
    q = abs(a) // abs(b)
    return q if (a < 0) == (b < 0) else -q


# ---------------------------------------------------------------- T1

@task("t1-digits")
def digits(rng):
    def solve(inp):
        out = []
        for line in inp.splitlines():
            n = int(line)
            s = str(abs(n))
            rev = int(s[::-1])
            if n < 0 and rev != 0:
                rev = -rev
            out.append(f"{sum(map(int, s))} {rev}")
        return lines(out)
    cases = [
        ["123", "-4500", "0", "7", "1000000", "-9"],
        [str(rng.randint(-10**15, 10**15)) for _ in range(30)],
        ["999999999999999", "-100000000000000", "10", "-1", "5"],
        [],
    ]
    return [(lines(c), solve(lines(c))) for c in cases]


@task("t1-floordiv")
def floordiv(rng):
    def solve(inp):
        out = []
        for line in inp.splitlines():
            a, b = map(int, line.split(" "))
            out.append(f"{a // b} {a % b}")
        return lines(out)
    cases = [
        ["7 2", "-7 2", "7 -2", "-7 -2", "6 3", "-6 3", "0 5", "1 7", "-1 7", "1000000000 -3"],
        [f"{rng.randint(-10**9, 10**9)} {rng.choice([-1, 1]) * rng.randint(1, 10**4)}" for _ in range(40)],
        [f"{rng.randint(-100, 100)} {rng.choice([-1, 1]) * rng.randint(1, 9)}" for _ in range(40)],
    ]
    return [(lines(c), solve(lines(c))) for c in cases]


@task("t1-rotate")
def rotate(rng):
    def solve(inp):
        ls = inp.splitlines()
        k, items = int(ls[0]), ls[1:]
        if not items:
            return ""
        s = k % len(items)
        return lines(items[-s:] + items[:-s] if s else items)
    words = ["apple", "bread", "cider", "dates", "eggs", "figs", "grapes", "honey", "ice", "jam"]
    cases = [
        ["1", "a", "b", "c"],
        ["-1", "a", "b", "c"],
        ["0", "x", "y"],
        ["5"],
        ["1000000000"] + words[:7],
        ["-999999999"] + words,
        [str(rng.randint(-50, 50))] + [rng.choice(words) + str(i) for i in range(rng.randint(1, 12))],
        ["3", "only"],
    ]
    return [(lines(c), solve(lines(c))) for c in cases]


@task("t1-palindromes")
def palindromes(rng):
    keep = set(string.ascii_lowercase + string.digits)

    def solve(inp):
        out = []
        for line in inp.splitlines():
            cs = [c for c in line.lower() if c in keep]
            out.append("yes" if cs == cs[::-1] else "no")
        return lines(out)
    cases = [
        ["A man, a plan, a canal: Panama!", "racecar", "Racecar", "hello", "", "!!", "ab", "a",
         "No 'x' in Nixon", "12321", "1231", "Was it a car or a cat I saw?", "Step on no pets.", "abca"],
    ]
    rand = []
    for _ in range(30):
        half = "".join(rng.choice("abcXYZ019 ,.") for _ in range(rng.randint(0, 8)))
        mid = rng.choice(["", "q", "Q", " "])
        s = half + mid + half[::-1]
        if rng.random() < 0.4 and s:
            i = rng.randrange(len(s))
            s = s[:i] + rng.choice("mnp7") + s[i + 1:]
        rand.append(s)
    cases.append(rand)
    return [(lines(c), solve(lines(c))) for c in cases]


@task("t1-rank")
def rank(rng):
    import bisect

    def solve(inp):
        ls = inp.splitlines()
        xs = [int(t) for t in ls[0].split()]
        out = []
        for q in ls[1:]:
            q = int(q)
            k = bisect.bisect_left(xs, q)
            out.append(f"{k} {'found' if k < len(xs) and xs[k] == q else 'missing'}")
        return lines(out)
    big = sorted(rng.randint(-5000, 5000) for _ in range(800))
    cases = [
        ["1 3 5 7", "0", "1", "4", "7", "8", "-3"],
        ["", "5", "-5"],
        ["2 2 2 5 5 9", "2", "5", "9", "10", "1", "3"],
        [" ".join(map(str, big))] + [str(rng.randint(-5200, 5200)) for _ in range(60)] + [str(big[0]), str(big[-1])],
        ["42", "42", "41", "43"],
    ]
    return [(lines(c), solve(lines(c))) for c in cases]


@task("t1-weekday")
def weekday(rng):
    import datetime as dt
    names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def solve(inp):
        out = []
        for line in inp.splitlines():
            y, m, d = map(int, line.split("-"))
            out.append(names[dt.date(y, m, d).weekday()])
        return lines(out)
    fixed = ["2000-01-01", "1970-01-01", "2026-11-16", "1900-03-01", "1600-02-29", "0001-01-01",
             "9999-12-31", "2024-02-29", "1999-12-31", "2100-03-01", "0004-02-29", "1582-10-15"]
    rand = []
    for _ in range(50):
        d = dt.date(1, 1, 1) + dt.timedelta(days=rng.randint(0, 3652058))
        rand.append(f"{d.year:04d}-{d.month:02d}-{d.day:02d}")
    early = [f"{d.year:04d}-{d.month:02d}-{d.day:02d}"
             for d in (dt.date(1, 1, 1) + dt.timedelta(days=rng.randint(0, 800)) for _ in range(20))]
    cases = [fixed, rand, early]
    return [(lines(c), solve(lines(c))) for c in cases]


# ---------------------------------------------------------------- T2

@task("t2-rpn")
def rpn(rng):
    def ev(line):
        st = []
        toks = line.split()
        if not toks:
            return "error"
        for t in toks:
            body = t[1:] if t.startswith("-") else t
            if body and body.isdigit():
                st.append(int(t))
                continue
            if t not in ("+", "-", "*", "/", "%") or len(st) < 2:
                return "error"
            b, a = st.pop(), st.pop()
            if t in ("/", "%") and b == 0:
                return "error"
            st.append({"+": a + b, "-": a - b, "*": a * b,
                       "/": trunc_div(a, b) if b else 0,
                       "%": a - b * trunc_div(a, b) if b else 0}[t])
        return str(st[0]) if len(st) == 1 else "error"

    def solve(inp):
        return lines(ev(x) for x in inp.splitlines())

    def rand_expr(depth):
        if depth == 0 or rng.random() < 0.3:
            return [str(rng.randint(-20, 20))]
        return rand_expr(depth - 1) + rand_expr(depth - 1) + [rng.choice("+-*/%")]
    fixed = ["3 4 +", "5 1 2 + 4 * + 3 -", "7 2 /", "-7 2 /", "7 -2 /", "-7 2 %", "7 -2 %",
             "2 3 4 * +", "10 2 - 3 -", "1 0 /", "5 0 %", "+", "1 2", "", "  4   5  *  ",
             "-3 -4 *", "3 -", "12 x +", "0 3 -", "- 3", "--3 1 +", "100 7 % 3 /"]
    rand = [" ".join(rand_expr(rng.randint(1, 4))) for _ in range(60)]
    return [(lines(fixed), solve(lines(fixed))), (lines(rand), solve(lines(rand)))]


@task("t2-life")
def life(rng):
    def solve(inp):
        ls = inp.splitlines()
        g, grid = int(ls[0]), [[c == "#" for c in row] for row in ls[1:]]
        h, w = len(grid), len(grid[0]) if grid else 0
        for _ in range(g):
            nxt = []
            for r in range(h):
                row = []
                for c in range(w):
                    n = sum(grid[rr][cc] for rr in range(r - 1, r + 2) for cc in range(c - 1, c + 2)
                            if (rr, cc) != (r, c) and 0 <= rr < h and 0 <= cc < w)
                    row.append(n == 3 or (grid[r][c] and n == 2))
                nxt.append(row)
            grid = nxt
        return lines("".join("#" if x else "." for x in row) for row in grid)
    glider = ["6", ".#....", "..#...", "###...", "......", "......", "......"]
    blinker_edge = ["3", "#..", "#..", "#.."]
    edge = ["1", "##", "##"]
    single = ["4", "#"]
    zero = ["0", "#.#", ".#.", "#.#"]
    rand = [str(rng.randint(5, 25))] + ["".join(rng.choice("#..") for _ in range(17)) for _ in range(13)]
    rand2 = [str(rng.randint(1, 10))] + ["".join(rng.choice("#.") for _ in range(9)) for _ in range(20)]
    cases = [glider, blinker_edge, edge, single, zero, rand, rand2]
    return [(lines(c), solve(lines(c))) for c in cases]


@task("t2-bignum")
def bignum(rng):
    def solve(inp):
        out = []
        for line in inp.splitlines():
            a, b = map(int, line.split(" "))
            out.append(f"{a + b} {a * b}")
        return lines(out)

    def big(n):
        return str(rng.randint(10 ** (n - 1), 10 ** n - 1)) if n > 1 else str(rng.randint(0, 9))
    fixed = ["0 0", "1 0", "0 12345", "999 1", "99999999999999999999 1", "12 34",
             "123456789012345678901234567890 987654321098765432109876543210",
             "9223372036854775807 9223372036854775807", "5 5"]
    rand = [f"{big(rng.randint(1, 100))} {big(rng.randint(1, 100))}" for _ in range(25)]
    return [(lines(fixed), solve(lines(fixed))), (lines(rand), solve(lines(rand)))]


@task("t2-wordfreq")
def wordfreq(rng):
    import re

    def solve(inp):
        counts = {}
        for w in re.findall(r"[A-Za-z]+", inp):
            w = w.lower()
            counts[w] = counts.get(w, 0) + 1
        top = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:10]
        return lines(f"{w} {c}" for w, c in top)
    text1 = ["The cat and the hat.", "THE CAT sat; the mat-cat didn't!", "", "a A a b"]
    vocab = ["river", "stone", "light", "garden", "north", "glass", "ember", "quiet", "harbor", "willow",
             "copper", "meadow", "lantern", "thistle", "orbit", "maple", "cinder", "fable", "tide", "crane",
             "a", "an", "of", "to", "in"]
    rand = []
    for _ in range(60):
        ws = [rng.choice(vocab[:rng.randint(5, len(vocab))]) for _ in range(rng.randint(0, 12))]
        ws = [w.upper() if rng.random() < 0.1 else (w.capitalize() if rng.random() < 0.2 else w) for w in ws]
        seps = [rng.choice([" ", " ", ", ", "; ", " -- ", "'", "3", "  "]) for _ in ws]
        rand.append("".join(w + s for w, s in zip(ws, seps)).strip())
    few = ["zeta beta alpha", "beta"]
    empty = ["", "   ", "123 456 !!!"]
    cases = [text1, rand, few, empty]
    return [(lines(c), solve(lines(c))) for c in cases]


def main():
    for name, fn in TASKS.items():
        rng = random.Random(name)
        tests = ROOT / name / "tests"
        tests.mkdir(parents=True, exist_ok=True)
        for p in tests.iterdir():
            p.unlink()
        for i, (inp, out) in enumerate(fn(rng), 1):
            (tests / f"{i:02d}.in").write_text(inp)
            (tests / f"{i:02d}.out").write_text(out)
        print(f"{name}: {i} tests")


if __name__ == "__main__":
    main()
