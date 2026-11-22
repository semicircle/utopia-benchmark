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


# ---------------------------------------------------------------- T3
#
# Longer programs (150-300 lines) where the dialect's false friends bite in
# many places at once, so a slip anywhere shows. Each has several test files,
# one per kind of input, so a partly right program gets partial credit.

@task("t3-calc")
def calc(rng):
    class Bad(Exception):
        pass

    def small(v):
        if abs(v) >= 2 ** 50:  # keep every intermediate value far inside 64 bits
            raise OverflowError
        return v

    def ev(line):
        toks, i = [], 0
        while i < len(line):
            c = line[i]
            if c == " ":
                i += 1
            elif c.isdigit():
                j = i
                while j < len(line) and line[j].isdigit():
                    j += 1
                toks.append(int(line[i:j]))
                i = j
            elif c in "+-*/%()":
                toks.append(c)
                i += 1
            else:
                return "error"
        pos = 0

        def peek():
            return toks[pos] if pos < len(toks) else None

        def take():
            nonlocal pos
            pos += 1
            return toks[pos - 1]

        def expr():
            v = term()
            while peek() in ("+", "-"):
                op = take()
                w = term()
                v = small(v + w if op == "+" else v - w)
            return v

        def term():
            v = unary()
            while peek() in ("*", "/", "%"):
                op = take()
                w = unary()
                if op == "*":
                    v = small(v * w)
                else:
                    if w == 0:
                        raise Bad
                    q = trunc_div(v, w)
                    v = q if op == "/" else v - w * q
            return v

        def unary():
            if peek() == "-":
                take()
                return -unary()
            return primary()

        def primary():
            t = peek()
            if isinstance(t, int):
                return take()
            if t == "(":
                take()
                v = expr()
                if peek() != ")":
                    raise Bad
                take()
                return v
            raise Bad
        try:
            v = expr()
        except Bad:
            return "error"
        return str(v) if pos == len(toks) else "error"

    def solve(inp):
        return lines(ev(x) for x in inp.splitlines())

    def rand_expr(depth):
        r = rng.random()
        if depth == 0 or r < 0.25:
            return str(rng.randint(0, 30))
        if r < 0.35:
            return "-" + rand_expr(depth - 1)
        if r < 0.5:
            return "(" + rand_expr(depth - 1) + ")"
        sp = rng.choice(["", " ", "  "])
        return rand_expr(depth - 1) + sp + rng.choice("+-*/%") + sp + rand_expr(depth - 1)
    precedence = ["2+3*4", "2*3+4", "10-4-3", "100/10/3", "2*3%4", "7+8%5*2", "1-2+3-4+5",
                  "20/3*3", "2*(3+4)", "(2+3)*(4+5)", "((7))", "3*-2", "-3*2", "--4", "-(2+3)*2",
                  "1+2*3-4/2+5%3", "8-2*3-1"]
    division = ["7/2", "-7/2", "7/-2", "-7/-2", "7%3", "-7%3", "7%-3", "-7%-3", "0/5", "-1/3",
                "-17%5*2", "100/-7%4", "-(7/2)", "(-7)/2"]
    spacing = ["  1 +  2 ", "12   *3", "( 4 )", " -  5", "6 / 2 / 3", "1 2", "+1", "3 + + 4"]
    errors = ["", "   ", "1/0", "5%(3-3)", "(1+2", "1+2)", "()", "2*", "x+1", "1.5+2", "4 ^ 2",
              "(()", "7 % 0 + 1", "-", "3+(4*)"]
    def rand_lines(depth_lo, depth_hi, n):
        out = []
        while len(out) < n:
            e = rand_expr(rng.randint(depth_lo, depth_hi))
            try:
                ev(e)
            except OverflowError:
                continue
            out.append(e)
        return out
    rand1 = rand_lines(2, 4, 40)
    rand2 = rand_lines(4, 6, 40)
    cases = [precedence, division, spacing, errors, rand1, rand2]
    return [(lines(c), solve(lines(c))) for c in cases]


@task("t3-maze")
def maze(rng):
    def solve(inp):
        ls = inp.splitlines()
        h, w = map(int, ls[0].split())
        grid = ls[1:1 + h]
        start = end = None
        for r in range(h):
            for c in range(w):
                if grid[r][c] == "S":
                    start = (r, c)
                if grid[r][c] == "E":
                    end = (r, c)
        dist, ways = {start: 0}, {start: 1}
        queue = [start]
        for cur in queue:
            r, c = cur
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if not (0 <= nr < h and 0 <= nc < w) or grid[nr][nc] == "#":
                    continue
                nxt = (nr, nc)
                if nxt not in dist:
                    dist[nxt] = dist[cur] + 1
                    ways[nxt] = ways[cur]
                    queue.append(nxt)
                elif dist[nxt] == dist[cur] + 1:
                    ways[nxt] += ways[cur]
        if end not in dist:
            return "-1 0\n"
        return f"{dist[end]} {ways[end]}\n"

    def make(h, w, walls):
        cells = [["#" if rng.random() < walls else "." for _ in range(w)] for _ in range(h)]
        spots = rng.sample([(r, c) for r in range(h) for c in range(w)], 2)
        cells[spots[0][0]][spots[0][1]] = "S"
        cells[spots[1][0]][spots[1][1]] = "E"
        return [f"{h} {w}"] + ["".join(row) for row in cells]
    open_room = ["4 5", "S....", ".....", ".....", "....E"]
    edges = ["3 7", "E#...#S", ".#.#.#.", "...#..."]
    blocked = ["3 3", "S#.", "##.", "..E"]
    adjacent = ["1 2", "SE"]
    column = ["5 1", "E", ".", ".", ".", "S"]
    cases = [open_room, edges, blocked, adjacent, column, make(12, 15, 0.2), make(20, 20, 0.3),
             make(25, 25, 0.1), make(18, 9, 0.35)]
    return [(lines(c), solve(lines(c))) for c in cases]


@task("t3-bigdiv")
def bigdiv(rng):
    def solve(inp):
        out = []
        for line in inp.splitlines():
            a, b = map(int, line.split(" "))
            out.append(f"{a // b} {a % b}")
        return lines(out)

    def big(n):
        return str(rng.randint(10 ** (n - 1), 10 ** n - 1)) if n > 1 else str(rng.randint(1, 9))
    small = ["0 7", "7 7", "6 7", "100 7", "1 1", "99 9", "1000 10", "12345 1"]
    edges = ["1000000000000000000000 1", "1000000000000000000000 999999999999999999999",
             "999999999999999999999 1000000000000000000000", "10000000000000000000000000000 3",
             "123456789123456789123456789 123456789", "9223372036854775808 2",
             "18446744073709551616 4294967296"]
    rand1 = [f"{big(rng.randint(1, 30))} {big(rng.randint(1, 15))}" for _ in range(15)]
    rand2 = [f"{big(rng.randint(30, 80))} {big(rng.randint(10, 40))}" for _ in range(15)]
    rand3 = []
    for _ in range(10):
        b = int(big(rng.randint(5, 30)))
        q = int(big(rng.randint(1, 30)))
        rand3.append(f"{b * q + rng.choice([0, 0, b - 1, 1])} {b}")
    cases = [small, edges, rand1, rand2, rand3]
    return [(lines(c), solve(lines(c))) for c in cases]


@task("t3-justify")
def justify(rng):
    def solve(inp):
        ls = inp.splitlines()
        width = int(ls[0])
        words = " ".join(ls[1:]).split()
        out, cur = [], []
        for w in words:
            if cur and len(" ".join(cur + [w])) > width:
                out.append(cur)
                cur = []
            cur.append(w)
        res = []
        for i, line in enumerate(out):
            if len(line) == 1:
                res.append(line[0])
                continue
            gaps = len(line) - 1
            extra = width - sum(map(len, line))
            base, more = extra // gaps, extra % gaps
            s = ""
            for j, w in enumerate(line[:-1]):
                s += w + " " * (base + (1 if j < more else 0))
            res.append(s + line[-1])
        if cur:
            res.append(" ".join(cur))
        return lines(res)
    vocab = ("the of a to in is it that for on with as was by at be this from or an are not but had "
             "lantern harbor copper meadow thistle orbit cinder willow anchorage lighthouse procession "
             "x y z ox elm ivy quartz zephyr archipelago").split()

    def text(n, width):
        ws = [w for w in (rng.choice(vocab) for _ in range(n)) if len(w) <= width]
        out, line = [], []
        for w in ws:
            line.append(w)
            if rng.random() < 0.15:
                out.append(("  " if rng.random() < 0.3 else " ").join(line))
                line = []
        out.append(" ".join(line))
        if rng.random() < 0.3:
            out.insert(rng.randrange(len(out) + 1), "")
        return out
    simple = ["16", "This is an example of text justification."]
    one_word = ["10", "a", "supercalif", "b c"]
    exact = ["11", "hello world hello world"]
    spaces = ["20", "   lots   of    spaces   ", "", "  between     words  "]
    empty = ["30", "", "   "]
    cases = [simple, one_word, exact, spaces, empty,
             ["25"] + text(80, 25), ["12"] + text(60, 12), ["40"] + text(150, 40), ["17"] + text(70, 17)]
    return [(lines(c), solve(lines(c))) for c in cases]


@task("t3-asm")
def asm(rng):
    regs = "abcdefghijklmnopqrstuvwxyz"

    def solve(inp):
        prog = [l.split(" ") for l in inp.splitlines()]
        r = {c: 0 for c in regs}
        out, pc, steps = [], 0, 0

        def val(x):
            return r[x] if x in r else int(x)
        while 0 <= pc < len(prog):
            if steps == 10000:
                out.append("timeout")
                break
            steps += 1
            op, *args = prog[pc]
            if op == "set":
                r[args[0]] = val(args[1])
            elif op == "add":
                r[args[0]] += val(args[1])
            elif op == "sub":
                r[args[0]] -= val(args[1])
            elif op == "mul":
                r[args[0]] *= val(args[1])
            elif op in ("div", "mod"):
                d = val(args[1])
                if d == 0:
                    out.append("error")
                    break
                q = trunc_div(r[args[0]], d)
                r[args[0]] = q if op == "div" else r[args[0]] - d * q
            elif op == "jnz":
                if val(args[0]) != 0:
                    pc += val(args[1])
                    continue
            elif op == "out":
                out.append(str(val(args[0])))
            pc += 1
        return lines(out)
    basics = ["set a 7", "set b -3", "add a b", "out a", "mul a a", "out a", "sub b 10", "out b", "out 42",
              "set c a", "div c 3", "out c", "set d -17", "mod d 5", "out d", "set e -17", "div e 5", "out e",
              "set f 17", "mod f -5", "out f", "out z"]
    loop = ["set n 10", "set a 0", "set b 1", "out a", "set t a", "add t b", "set a b", "set b t",
            "sub n 1", "jnz n -6", "out b"]
    factorial = ["set n 12", "set f 1", "mul f n", "sub n 1", "jnz n -2", "out f"]
    jumps = ["set a 3", "jnz 1 3", "out 111", "out 222", "out a", "set j -2", "sub a 1", "jnz a j", "out 999",
             "jnz 1 100", "out 0"]
    regjump = ["set k 2", "jnz k k", "out 1", "out 2", "set k -1", "jnz 0 k", "out 3"]
    divzero = ["set a 5", "out a", "set b 0", "div a b", "out a"]
    forever = ["set a 1", "add b 1", "jnz a -1", "out b"]
    backward_exit = ["jnz 1 2", "out 5", "set a 9", "out a", "jnz 1 -10", "out 6"]
    collatz = ["set n 27", "set s 0", "set t n", "sub t 1", "jnz t 2", "jnz 1 11", "set p n", "mod p 2",
               "jnz p 4", "div n 2", "add s 1", "jnz 1 -9", "mul n 3", "add n 1", "add s 1", "jnz 1 -13",
               "out s"]
    cases = [basics, loop, factorial, jumps, regjump, divzero, forever, backward_exit, collatz]
    return [(lines(c), solve(lines(c))) for c in cases]


# ---------------------------------------------------------------- T4
#
# Small systems (300-500 lines): an interpreter, a spreadsheet, a regex
# engine. Each test file adds one feature to the ones before (a ladder), so
# a model that gets the core right but slips on a later feature still scores
# partly, and the score falls in steps rather than all at once.

@task("t4-lisp")
def lisp(rng):
    import sys
    sys.setrecursionlimit(20000)

    class Err(Exception):
        pass

    def tokenize(src):
        return src.replace("(", " ( ").replace(")", " ) ").split()

    def is_int(t):
        body = t[1:] if t.startswith("-") else t
        return body.isdigit()

    def parse(toks):
        forms, stack = [], [[]]
        for t in toks:
            if t == "(":
                stack.append([])
            elif t == ")":
                done = stack.pop()
                stack[-1].append(done)
            else:
                stack[-1].append(t)
        return stack[0]

    class Proc:
        def __init__(self, params, body, env):
            self.params, self.body, self.env = params, body, env

    NIL = ()

    class Pair:
        def __init__(self, a, d):
            self.a, self.d = a, d

    def show(v):
        if v is True:
            return "#t"
        if v is False:
            return "#f"
        if isinstance(v, int):
            return str(v)
        if isinstance(v, (Proc, str)):
            return "#<procedure>"
        if v == NIL:
            return "()"
        parts = []
        while isinstance(v, Pair):
            parts.append(show(v.a))
            v = v.d
        tail = "" if v == NIL else " . " + show(v)
        return "(" + " ".join(parts) + tail + ")"

    PRIMS = {"+", "-", "*", "/", "remainder", "=", "<", ">", "not", "cons", "car", "cdr", "list", "null?"}

    def ints(args):
        if any(isinstance(a, bool) or not isinstance(a, int) for a in args):
            raise Err
        return args

    def prim(name, args):
        n = len(args)
        if name == "+":
            return sum(ints(args))
        if name == "*":
            out = 1
            for a in ints(args):
                out *= a
            return out
        if name == "-":
            if n == 1:
                return -ints(args)[0]
            if n == 2:
                a, b = ints(args)
                return a - b
            raise Err
        if name in ("/", "remainder", "=", "<", ">"):
            if n != 2:
                raise Err
            a, b = ints(args)
            if name in ("/", "remainder"):
                if b == 0:
                    raise Err
                q = trunc_div(a, b)
                return q if name == "/" else a - b * q
            return a == b if name == "=" else (a < b if name == "<" else a > b)
        if name == "not":
            if n != 1:
                raise Err
            return args[0] is False
        if name == "cons":
            if n != 2:
                raise Err
            return Pair(args[0], args[1])
        if name in ("car", "cdr"):
            if n != 1 or not isinstance(args[0], Pair):
                raise Err
            return args[0].a if name == "car" else args[0].d
        if name == "list":
            out = NIL
            for a in reversed(args):
                out = Pair(a, out)
            return out
        if name == "null?":
            if n != 1:
                raise Err
            return args[0] == NIL and not isinstance(args[0], Pair)

    def lookup(env, name):
        while env is not None:
            if name in env[0]:
                return env[0][name]
            env = env[1]
        raise Err

    def ev(x, env, depth=0):
        if isinstance(x, str):
            if is_int(x):
                return int(x)
            if x == "#t":
                return True
            if x == "#f":
                return False
            return lookup(env, x)
        if not x:
            raise Err
        head = x[0]
        if head == "quote" or head == "define":
            raise Err  # define only at top level; no quote
        if head == "if":
            if len(x) != 4:
                raise Err
            return ev(x[2] if ev(x[1], env, depth + 1) is not False else x[3], env, depth + 1)
        if head == "lambda":
            if len(x) < 3 or not isinstance(x[1], list) or not all(isinstance(p, str) and not is_int(p) for p in x[1]):
                raise Err
            return Proc(x[1], x[2:], env)
        if head == "let":
            if len(x) < 3 or not isinstance(x[1], list):
                raise Err
            frame = {}
            for b in x[1]:
                if not isinstance(b, list) or len(b) != 2 or not isinstance(b[0], str) or is_int(b[0]):
                    raise Err
                frame[b[0]] = ev(b[1], env, depth + 1)
            v = None
            for e in x[2:]:
                v = ev(e, (frame, env), depth + 1)
            return v
        if head == "begin":
            if len(x) < 2:
                raise Err
            v = None
            for e in x[1:]:
                v = ev(e, env, depth + 1)
            return v
        f = ev(head, env, depth + 1)
        args = [ev(a, env, depth + 1) for a in x[1:]]
        if isinstance(f, str):
            return prim(f, args)
        if not isinstance(f, Proc) or len(args) != len(f.params):
            raise Err
        frame = dict(zip(f.params, args))
        v = None
        for e in f.body:
            v = ev(e, (frame, f.env), depth + 1)
        return v

    def solve(inp):
        glob = {p: p for p in PRIMS}
        env = (glob, None)
        out = []
        for form in parse(tokenize(inp)):
            try:
                if isinstance(form, list) and form and form[0] == "define":
                    if len(form) != 3:
                        raise Err
                    target = form[1]
                    if isinstance(target, list):  # (define (f args) body): one body expression
                        if not target or not all(isinstance(p, str) and not is_int(p) for p in target):
                            raise Err
                        glob[target[0]] = Proc(target[1:], [form[2]], env)
                    elif isinstance(target, str) and not is_int(target):
                        glob[target] = ev(form[2], env)
                    else:
                        raise Err
                else:
                    out.append(show(ev(form, env)))
            except Err:
                out.append("error")
        return lines(out)

    arith = ["(+ 1 2)", "(* 2 3 4)", "(- 10 4)", "(- 5)", "(+)", "(*)", "(/ 7 2)", "(/ -7 2)",
             "(remainder -7 2)", "(+ (* 2 3) (- 10 (/ 9 3)))", "42", "-17", "(< 1 2)", "(> 1 2)",
             "(= 3 3)", "#t", "#f", "(not #f)", "(not 0)"]
    defines = ["(define x 10)", "(define y (* x 2))", "(+ x y)", "(define x 1)", "x", "y",
               "(define (sq n) (* n n))", "(sq 12)", "(sq (sq 3))"]
    conditions = ["(define (abs n) (if (< n 0) (- n) n))", "(abs -5)", "(abs 7)",
                  "(if 0 1 2)", "(if #f 1 2)", "(if (= 1 1) (+ 1 1) undefined-name)",
                  "(define (fact n) (if (< n 2) 1 (* n (fact (- n 1)))))", "(fact 10)", "(fact 20)",
                  "(define (fib n) (if (< n 2) n (+ (fib (- n 1)) (fib (- n 2)))))", "(fib 15)"]
    closures = ["(define (adder k) (lambda (n) (+ n k)))", "(define add5 (adder 5))", "(add5 10)",
                "((adder 3) 4)", "((lambda (a b) (- a b)) 10 3)",
                "(define (compose f g) (lambda (v) (f (g v))))", "((compose add5 (adder 100)) 1)",
                "(define k 1000)", "(add5 1)",
                "(let ((a 2) (b 3)) (* a b))", "(let ((k 7)) (add5 k))",
                "(let ((x 1)) (let ((x 2) (y x)) (+ x y)))", "(begin 1 2 3)",
                "(define (twice f) (lambda (v) (f (f v))))", "((twice (twice add5)) 0)", "add5"]
    lists = ["(cons 1 2)", "(cons 1 (cons 2 (list)))", "(list 1 2 3)", "(list)", "(car (list 4 5))",
             "(cdr (list 4 5))", "(null? (list))", "(null? (list 1))", "(list (list 1 2) (list) 3)",
             "(define (len xs) (if (null? xs) 0 (+ 1 (len (cdr xs)))))", "(len (list 1 2 3 4))",
             "(define (range a b) (if (< a b) (cons a (range (+ a 1) b)) (list)))", "(range 0 10)",
             "(define (map f xs) (if (null? xs) (list) (cons (f (car xs)) (map f (cdr xs)))))",
             "(map (lambda (n) (* n n)) (range 1 6))",
             "(define (filter p xs) (if (null? xs) (list) (if (p (car xs)) (cons (car xs) (filter p (cdr xs))) (filter p (cdr xs)))))",
             "(filter (lambda (n) (= 0 (remainder n 3))) (range 0 20))",
             "(define (foldl f acc xs) (if (null? xs) acc (foldl f (f acc (car xs)) (cdr xs))))",
             "(foldl + 0 (range 1 101))", "(foldl (lambda (acc v) (cons v acc)) (list) (list 1 2 3))",
             "(cons (list 1) 2)", "car"]
    errors = ["(car (list))", "(+ 1 #t)", "(undefined 1)", "(1 2)", "(/ 1 0)", "(remainder 5 0)",
              "((lambda (a) a))", "((lambda (a) a) 1 2)", "(if 1 2)", "(define)", "(cdr 5)", "()",
              "(lambda)", "(let ((1 2)) 3)", "(- 1 2 3)", "(not)", "(define z (car (list)))", "z",
              "(define z 5)", "z", "(begin)", "(= 1 #f)", "(quote a)", "(define (f) (define g 1))", "(f)",
              "(+ 1 2)"]
    ladder = [arith, defines, conditions, closures, lists, errors]
    cases = []
    prefix = []
    for part in ladder:
        cases.append(part if part is arith or part is errors else prefix + part)
        if part is defines or part is conditions:
            prefix = prefix + [p for p in part if p.startswith("(define")]
    multiline = ["(define (count-down n)", "  (if (= n 0)", "      (list)", "      (cons n (count-down (- n 1)))))",
                 "(count-down", "   5)", "  (+  1", "2 )  (* 3 4)"]
    cases.append(multiline)
    return [(lines(c), solve(lines(c))) for c in cases]


@task("t4-sheet")
def sheet(rng):
    import re

    class Syntax(Exception):
        pass

    class Div0(Exception):
        pass

    PRIO = {"#CYCLE": 3, "#ERR": 2, "#DIV0": 1}
    CELL = re.compile(r"[A-Z][1-9][0-9]?\Z")

    def tokenize(s):
        toks, i = [], 0
        while i < len(s):
            c = s[i]
            if c == " ":
                i += 1
            elif c.isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                toks.append(("n", int(s[i:j])))
                i = j
            elif c.isupper():
                j = i
                while j < len(s) and (s[j].isupper() or s[j].isdigit()):
                    j += 1
                toks.append(("w", s[i:j]))
                i = j
            elif c in "+-*/%(),:":
                toks.append((c, None))
                i += 1
            else:
                raise Syntax
        return toks

    def parse(src):
        toks, pos = tokenize(src), 0

        def peek():
            return toks[pos][0] if pos < len(toks) else None

        def take(kind):
            nonlocal pos
            if peek() != kind:
                raise Syntax
            pos += 1
            return toks[pos - 1][1]

        def expr():
            node = term()
            while peek() in ("+", "-"):
                op = peek()
                take(op)
                node = ("bin", op, node, term())
            return node

        def term():
            node = unary()
            while peek() in ("*", "/", "%"):
                op = peek()
                take(op)
                node = ("bin", op, node, unary())
            return node

        def unary():
            if peek() == "-":
                take("-")
                return ("neg", unary())
            return primary()

        def primary():
            k = peek()
            if k == "n":
                return ("num", take("n"))
            if k == "(":
                take("(")
                node = expr()
                take(")")
                return node
            if k == "w":
                word = take("w")
                if word in ("SUM", "MIN", "MAX"):
                    take("(")
                    args = [arg()]
                    while peek() == ",":
                        take(",")
                        args.append(arg())
                    take(")")
                    return ("fn", word, args)
                if not CELL.match(word):
                    raise Syntax
                return ("ref", word)
            raise Syntax

        def arg():
            if peek() == "w" and pos + 1 < len(toks) and toks[pos + 1][0] == ":":
                a = take("w")
                take(":")
                b = take("w")
                if not (CELL.match(a) and CELL.match(b)):
                    raise Syntax
                return ("range", a, b)
            return expr()
        node = expr()
        if pos != len(toks):
            raise Syntax
        return node

    def cells_in(a, b):
        c0, c1 = sorted((a[0], b[0]))
        r0, r1 = sorted((int(a[1:]), int(b[1:])))
        return [chr(c) + str(r) for r in range(r0, r1 + 1) for c in range(ord(c0), ord(c1) + 1)]

    def refs(node, out):
        kind = node[0]
        if kind == "ref":
            out.append(node[1])
        elif kind == "range":
            out.extend(cells_in(node[1], node[2]))
        elif kind == "bin":
            refs(node[2], out)
            refs(node[3], out)
        elif kind == "neg":
            refs(node[1], out)
        elif kind == "fn":
            for a in node[2]:
                refs(a, out)
        return out

    def solve(inp):
        formulas = {}
        for line in inp.splitlines():
            name, src = line.split(" = ", 1)
            formulas[name] = src
        ast = {}
        for name, src in formulas.items():
            try:
                ast[name] = parse(src)
            except Syntax:
                ast[name] = None
        deps = {n: (refs(a, []) if a is not None else []) for n, a in ast.items()}

        def reaches(start, target):
            seen, stack = set(), list(deps[start])
            while stack:
                c = stack.pop()
                if c == target:
                    return True
                if c in seen or c not in deps:
                    continue
                seen.add(c)
                stack.extend(deps[c])
            return False
        on_cycle = {n for n in ast if reaches(n, n)}
        memo = {}

        def value(name):
            if name not in ast:
                return 0
            if name in memo:
                return memo[name]
            if name in on_cycle:
                v = "#CYCLE"
            elif ast[name] is None:
                v = "#ERR"
            else:
                worst = None
                for d in deps[name]:
                    dv = value(d)
                    if isinstance(dv, str) and (worst is None or PRIO[dv] > PRIO[worst]):
                        worst = dv
                if worst:
                    v = worst
                else:
                    try:
                        v = calc(ast[name])
                    except Div0:
                        v = "#DIV0"
            memo[name] = v
            return v

        def calc(node):
            kind = node[0]
            if kind == "num":
                return node[1]
            if kind == "ref":
                return value(node[1])
            if kind == "neg":
                return -calc(node[1])
            if kind == "bin":
                a, b = calc(node[2]), calc(node[3])
                op = node[1]
                if op in "/%":
                    if b == 0:
                        raise Div0
                    q = trunc_div(a, b)
                    return q if op == "/" else a - b * q
                return a + b if op == "+" else a - b if op == "-" else a * b
            vals = []
            for a in node[2]:
                if a[0] == "range":
                    vals.extend(value(c) for c in cells_in(a[1], a[2]))
                else:
                    vals.append(calc(a))
            return sum(vals) if node[1] == "SUM" else min(vals) if node[1] == "MIN" else max(vals)
        order = sorted(ast, key=lambda n: (int(n[1:]), n[0]))
        return lines(f"{n} = {value(n)}" for n in order)

    constants = ["A1 = 5", "B1 = -3", "A2 = 0", "C3 = 12", "B2 = 007"]
    arithmetic = ["A1 = 4", "A2 = A1 * 2 + 1", "A3 = (A1 + A2) * -2", "B1 = A3 / 4", "B2 = A3 % 4",
                  "B3 = -A3 / -7", "C1 = A1 - A2 - A3", "C2 = 2 * 3 + 4 * 5 - 6 / 4", "C3 = Z99 + 1",
                  "D1 = C1 + C2 * (B1 - B2)"]
    functions = ["A1 = 3", "A2 = -1", "A3 = 8", "B1 = 2", "B3 = 5", "C1 = SUM(A1:B3)", "C2 = MIN(A1:A3)",
                 "C3 = MAX(B3:A1)", "D1 = SUM(A1, A3, 10)", "D2 = MAX(A1:A3, 100, -C1)", "D3 = MIN(B2:B2)",
                 "E1 = SUM(A1:A3) * 2 - MAX(A1, B1)", "E2 = SUM(C1:D1)"]
    redefine = ["A1 = 1", "B1 = A1 + 1", "A1 = 10", "C1 = B1 * B1", "B1 = A1 + 5", "C2 = SUM(A1:C1)"]
    div0 = ["A1 = 0", "A2 = 5 / A1", "A3 = A2 + 1", "B1 = 7 % (A1 * 3)", "B2 = SUM(A1:A3)", "B3 = 10 / 3",
            "C1 = -9 / 2", "C2 = MIN(A2, 1)", "C3 = 1 + 2"]
    syntax = ["A1 = 1 +", "A2 = (2", "A3 = 2)", "B1 = 3 $ 4", "B2 = A1 * 2", "B3 = SUM()", "C1 = AB1",
              "C2 = A100", "C3 = FOO(1)", "D1 = SUM(A1:)", "D2 = 4 5", "D3 = A0 + 1", "E1 = 2 * B2 / 0",
              "E2 = MAX(B2, E1)", "E3 = A1:A2", "F1 = 12"]
    cycles = ["A1 = B1 + 1", "B1 = A1 * 2", "C1 = A1 + 5", "C2 = 3", "D1 = D1", "D2 = SUM(D1:D3)",
              "E1 = E2 / 0", "E2 = E3", "E3 = E1", "F1 = C2 + 1", "F2 = SUM(F1:F3)", "G1 = G2 + H1",
              "G2 = 1 / 0", "H1 = (1", "G3 = MAX(G2, H1, 1)"]
    big = []
    names = [chr(c) + str(r) for r in range(1, 9) for c in range(ord("A"), ord("F") + 1)]
    for i, n in enumerate(names):
        earlier = names[:i]
        kind = rng.random()
        if not earlier or kind < 0.2:
            big.append(f"{n} = {rng.randint(-50, 50)}")
        elif kind < 0.45:
            a, b = rng.sample(earlier, 2) if len(earlier) > 1 else (earlier[0], earlier[0])
            big.append(f"{n} = {a} {rng.choice('+-*')} {b} {rng.choice('+-')} {rng.randint(0, 9)}")
        elif kind < 0.65:
            a = rng.choice(earlier)
            big.append(f"{n} = ({a} - {rng.randint(1, 20)}) / {rng.randint(1, 7)}")
        elif kind < 0.85:
            a, b = rng.choice(earlier), rng.choice(earlier)
            big.append(f"{n} = {rng.choice(['SUM', 'MIN', 'MAX'])}({a}:{b}) % {rng.randint(5, 97)}")
        else:
            a = rng.choice(earlier)
            big.append(f"{n} = MAX({a}, {rng.randint(-5, 5)}) - MIN({a}, 0)")
    rng.shuffle(big)
    cases = [constants, arithmetic, functions, redefine, div0, syntax, cycles, big]
    return [(lines(c), solve(lines(c))) for c in cases]


@task("t4-regex")
def regex(rng):
    import re

    class Bad(Exception):
        pass

    def validate(p):
        """Our grammar; raises Bad for a malformed pattern. Returns a Python
        regex with the same meaning."""
        pos = 0

        def peek():
            return p[pos] if pos < len(p) else None

        def alt():
            nonlocal pos
            out = [concat()]
            while peek() == "|":
                pos += 1
                out.append(concat())
            return "|".join(out)

        def concat():
            nonlocal pos
            out = ""
            while peek() is not None and peek() not in "|)":
                a = atom()
                if peek() is not None and peek() in "*+?":
                    a += peek()
                    pos += 1
                out += a
            return out

        def atom():
            nonlocal pos
            c = peek()
            if c == "(":
                pos += 1
                inner = alt()
                if peek() != ")":
                    raise Bad
                pos += 1
                return "(?:" + inner + ")"
            if c == ".":
                pos += 1
                return "."
            if c == "[":
                pos += 1
                neg = ""
                if peek() == "^":
                    neg = "^"
                    pos += 1
                items = ""
                while peek() is not None and peek() != "]":
                    lo = peek()
                    if not lo.isalnum():
                        raise Bad
                    pos += 1
                    if peek() == "-" and pos + 1 < len(p) and p[pos + 1] != "]":
                        hi = p[pos + 1]
                        if not hi.isalnum() or hi < lo:
                            raise Bad
                        pos += 2
                        items += lo + "-" + hi
                    else:
                        items += lo
                if peek() != "]" or not items:
                    raise Bad
                pos += 1
                return "[" + neg + items + "]"
            if c is not None and c.isalnum():
                pos += 1
                return c
            raise Bad
        out = alt()
        if pos != len(p):
            raise Bad
        return out

    def solve(inp):
        out = []
        for line in inp.splitlines():
            pat, text = line.split(" ", 1)
            try:
                rx = validate(pat)
            except Bad:
                out.append("error")
                continue
            out.append("yes" if re.fullmatch(rx, text, re.S) else "no")
        return lines(out)

    literal = ["abc abc", "abc abd", "abc ab", "abc abcd", "a a", "a ", "x9 x9", "1 2", "a.c abc", "a.c a.c",
               "... xyz", "... xy", "a.. a"]
    star = ["a* ", "a* aaaa", "a* aab", "ab*c ac", "ab*c abbbc", "ab+c ac", "ab+c abbc", "ab?c ac", "ab?c abc",
            "ab?c abbc", ".* anything", "a.*b axxxb", "a.*b axxxc", "a*a*a*a*b aaaaaaaaaaaaaaaaaaaaaaaaaaaaaac"]
    groups = ["(ab)* ", "(ab)* ababab", "(ab)* aba", "(ab)+ ", "(a|b)* abba", "(a|b)* abca", "cat|dog dog",
              "cat|dog cow", "a(b|c)d acd", "a(b|c)d aed", "(a|)b b", "a| ", "| ", "(x(y|z)+)? xyzzy",
              "((a)) a", "(a*)* aaa", "() ", "(a|ab)(c|bcd) abcd"]
    classes = ["[abc] b", "[abc] d", "[a-z]+ hello", "[a-z]+ Hello", "[^0-9]* abc", "[^0-9]* ab1",
               "[a-cx-z]* abxyc", "[a-cx-z]* abd", "[0-9]+(x[0-9]+)? 12x34", "[A-Z][a-z]* Utopia",
               "[^a] b", "[^a] a", "[^a] ", "[a-a] a", "[a-zA-Z0-9]+ Mixed123"]
    errors = ["(ab x", "ab) x", "* x", "a** x", "a*+ x", "(*a) x", "|* x", "[abc x", "[] x", "[^] x",
              "[z-a] x", "a-b a-b", "a{2} aa", "a\\b ab", "[a-] a", "[-a] a", "?a a", ") x", "a|*b x"]
    rand = []
    alphabet = "ab"

    def rpat(d):
        r = rng.random()
        if d == 0 or r < 0.3:
            return rng.choice(["a", "b", ".", "[ab]", "[^a]"])
        if r < 0.5:
            return rpat(d - 1) + rpat(d - 1)
        if r < 0.65:
            return "(" + rpat(d - 1) + "|" + rpat(d - 1) + ")"
        return "(" + rpat(d - 1) + ")" + rng.choice("*+?")
    for _ in range(40):
        pat = rpat(rng.randint(2, 4))
        text = "".join(rng.choice(alphabet + "c") for _ in range(rng.randint(0, 8)))
        rand.append(f"{pat} {text}")
    cases = [literal, star, groups, classes, errors, rand]
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
