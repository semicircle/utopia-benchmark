#!/usr/bin/env python3
import datetime
import math
import random
import subprocess
import sys

ROOT = "."
RESLIL = "bin/reslil"

def run(prog, data, timeout=20):
    p = subprocess.run(
        [RESLIL, "run", prog],
        input=data.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
    )
    return p.returncode, p.stdout.decode(), p.stderr.decode()

fails = 0

def check(name, prog, data, expected, timeout=20):
    global fails
    if not data.endswith("\n") and data != "":
        # allow callers to pass exact bytes; most inputs should include newline
        pass
    try:
        code, out, err = run(prog, data, timeout)
    except subprocess.TimeoutExpired:
        fails += 1
        print(f"FAIL {name}: timeout")
        return
    if code != 0 or out != expected:
        fails += 1
        print(f"FAIL {name}: exit {code}")
        print("STDERR:", err)
        print("INPUT:", repr(data[:500]))
        print("EXPECTED:", repr(expected[:500]))
        print("ACTUAL:", repr(out[:500]))
    else:
        print(f"ok {name}")

def digits_expected(n):
    if n == 0:
        return "0 0"
    sign = -1 if n < 0 else 1
    n = abs(n)
    s = 0
    rev = 0
    while n:
        d = n % 10
        s += d
        rev = rev * 10 + d
        n //= 10
    rev *= sign
    return f"{s} {rev}"

def trunc_div(a, b):
    q = abs(a) // abs(b)
    if (a < 0) != (b < 0):
        q = -q
    return q

def trunc_mod(a, b):
    return a - b * trunc_div(a, b)

def rpn_eval(line):
    toks = line.split()
    if not toks:
        return "error"
    stack = []
    for t in toks:
        if t in ["+", "-", "*", "/", "%"]:
            if len(stack) < 2:
                return "error"
            b = stack.pop()
            a = stack.pop()
            if t in ["/", "%"] and b == 0:
                return "error"
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            elif t == "/":
                stack.append(trunc_div(a, b))
            else:
                stack.append(trunc_mod(a, b))
        else:
            if t == "-" or t == "":
                return "error"
            neg = False
            body = t
            if t[0] == "-":
                neg = True
                body = t[1:]
            if body == "" or any(ch < "0" or ch > "9" for ch in body):
                return "error"
            v = int(body)
            if neg:
                v = -v
            stack.append(v)
    if len(stack) != 1:
        return "error"
    return str(stack[0])

def life_step(grid):
    rows = len(grid)
    cols = len(grid[0])
    nxt = []
    for r in range(rows):
        row = []
        for c in range(cols):
            n = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "#":
                        n += 1
            if grid[r][c] == "#" and n in (2, 3):
                row.append("#")
            elif grid[r][c] == "." and n == 3:
                row.append("#")
            else:
                row.append(".")
        nxt.append("".join(row))
    return nxt

def life_run(g, grid):
    for _ in range(g):
        grid = life_step(grid)
    return "\n".join(grid) + "\n"

def words_expected(text):
    import re
    counts = {}
    for w in re.findall(r"[A-Za-z]+", text):
        w = w.lower()
        counts[w] = counts.get(w, 0) + 1
    items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:10]
    return "".join(f"{w} {c}\n" for w, c in items)

def pal_expected(line):
    chars = [c.lower() for c in line if c.isalnum()]
    return "yes" if chars == chars[::-1] else "no"

# hello
check("hello", "solutions/t0-hello.res", "", "Hello, Utopia!\n")

# factorial
for n in range(0, 21):
    check(f"fact {n}", "solutions/t0-factorial.res", f"{n}\n", f"{math.factorial(n)}\n")

# even odd
cases = [
    ("", "even 0\nodd 0\n"),
    ("0\n", "even 1\nodd 0\n"),
    ("1\n", "even 0\nodd 1\n"),
    ("-2\n-3\n4\n5\n0\n-1\n8\n", "even 4\nodd 3\n"),
    ("1000000\n-1000000\n999999\n-999999\n", "even 2\nodd 2\n"),
]
for i, (inp, exp) in enumerate(cases):
    check(f"even {i}", "solutions/t0-even-odd.res", inp, exp)

# day names
days_in = "1\n2\n3\n4\n5\n6\n7\n0\n8\n-1\n100\n"
days_exp = "Monday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nSunday\ninvalid\ninvalid\ninvalid\ninvalid\n"
check("days", "solutions/t0-day-names.res", days_in, days_exp)
check("days empty", "solutions/t0-day-names.res", "", "")

# count
check("count 0", "solutions/t0-count.res", "0\n", "")
check("count 5", "solutions/t0-count.res", "5\n", "1\n2\n3\n4\n5\n")
check("count 1", "solutions/t0-count.res", "1\n", "1\n")

# fizzbuzz
def fizz(n):
    lines = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            lines.append("FizzBuzz")
        elif i % 3 == 0:
            lines.append("Fizz")
        elif i % 5 == 0:
            lines.append("Buzz")
        else:
            lines.append(str(i))
    return "\n".join(lines) + "\n"

check("fizz 1", "solutions/t0-fizzbuzz.res", "1\n", "1\n")
check("fizz 16", "solutions/t0-fizzbuzz.res", "16\n", fizz(16))
check("fizz 30", "solutions/t0-fizzbuzz.res", "30\n", fizz(30))

# reverse
check("rev empty", "solutions/t0-reverse-lines.res", "", "")
check("rev one", "solutions/t0-reverse-lines.res", "only\n", "only\n")
check("rev three", "solutions/t0-reverse-lines.res", "a\nb\nc\n", "c\nb\na\n")
check("rev blanks", "solutions/t0-reverse-lines.res", "a\n\nb\n", "b\n\na\n")
check("rev no final nl", "solutions/t0-reverse-lines.res", "a\nb", "b\na\n")
check("rev spaces", "solutions/t0-reverse-lines.res", "  x \ny\n", "y\n  x \n")

# digits
dig_nums = [123, -4500, 0, 10, 100, -100, -5, 5, 901, -901, 10**15, -10**15, 999999999999999, -10, 11, -11]
dig_in = "".join(f"{n}\n" for n in dig_nums)
dig_exp = "".join(digits_expected(n) + "\n" for n in dig_nums)
check("digits", "solutions/t1-digits.res", dig_in, dig_exp)
check("digits empty", "solutions/t1-digits.res", "", "")

# floordiv
fd_pairs = [(7, 2), (-7, 2), (7, -2), (-7, -2), (1, 1), (-1, -1), (5, 3), (-5, 3), (5, -3), (-5, -3), (0, 5), (0, -5), (10**9, 3), (-10**9, 3), (10**9, -3), (-10**9, -7), (1, -1), (-1, 1), (8, -3), (-8, 3)]
fd_in = "".join(f"{a} {b}\n" for a, b in fd_pairs)
fd_exp = "".join(f"{a // b} {a - b * (a // b)}\n" for a, b in fd_pairs)
check("floordiv", "solutions/t1-floordiv.res", fd_in, fd_exp)

# palindromes
pals = [
    "A man, a plan, a canal: Panama!",
    "racecar",
    "hello",
    "",
    "a",
    "ab",
    "AbBa",
    "12321",
    "123a321",
    "123421",
    "!!!",
    "A1b1a",
    "No 'x' in Nixon",
    "Was it a car or a cat I saw?",
    "Not a palindrome",
    "RaceCar",
]
pal_in = "\n".join(pals) + "\n"
pal_exp = "".join(pal_expected(s) + "\n" for s in pals)
check("pal", "solutions/t1-palindromes.res", pal_in, pal_exp)

# rank
rank_cases = [
    ("1 3 5 7\n5\n4\n1\n7\n0\n8\n3\n",
     "2 found\n2 missing\n0 found\n3 found\n0 missing\n4 missing\n1 missing\n"),
    ("\n5\n", "0 missing\n"),
    ("5\n5\n4\n6\n", "0 found\n0 missing\n1 missing\n"),
    ("1 3 3 3 5\n3\n4\n1\n5\n0\n6\n",
     "1 found\n4 missing\n0 found\n4 found\n0 missing\n5 missing\n"),
    ("-10 -10 -3 0 0 4\n-10\n-3\n-4\n0\n4\n5\n-11\n",
     "0 found\n2 found\n2 missing\n3 found\n5 found\n6 missing\n0 missing\n"),
    ("1 2 3\n", ""),
]
for i, (inp, exp) in enumerate(rank_cases):
    check(f"rank {i}", "solutions/t1-rank.res", inp, exp)

# rotate
def rot_expected(k, items):
    n = len(items)
    if n == 0:
        return ""
    rot = k % n
    # python % is non-negative for positive n, matches floor mod
    start = (n - rot) % n
    out = []
    for i in range(n):
        out.append(items[(start + i) % n])
    return "\n".join(out) + "\n"

rot_cases = [
    (1, ["a", "b", "c", "d"]),
    (-1, ["a", "b", "c", "d"]),
    (0, ["a", "b", "c", "d"]),
    (4, ["a", "b", "c", "d"]),
    (5, ["a", "b", "c", "d"]),
    (-5, ["a", "b", "c", "d"]),
    (2, ["a", "b", "c", "d", "e"]),
    (-2, ["a", "b", "c", "d", "e"]),
    (1000000000, ["a", "b", "c"]),
    (-1000000000, ["a", "b", "c"]),
    (3, ["only"]),
    (-9, ["only"]),
    (1, []),
    (0, ["", "x", ""]),
    (1, ["  spaced  ", "b"]),
]
for i, (k, items) in enumerate(rot_cases):
    inp = str(k) + "\n" + "".join(s + "\n" for s in items)
    check(f"rot {i}", "solutions/t1-rotate.res", inp, rot_expected(k, items))
check("rot no k", "solutions/t1-rotate.res", "", "")

# weekday
names_py = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dates = [
    "2000-01-01", "1970-01-01", "2026-11-18", "0001-01-01", "2000-02-29",
    "1900-01-01", "2024-02-29", "1999-12-31", "2024-01-01", "0004-02-29",
    "0100-02-28", "0100-03-01", "0400-02-29", "0400-03-01", "9999-12-31",
    "2023-01-01", "1980-06-15", "2012-12-21", "0001-12-31", "2020-02-29",
    "0001-02-28", "0001-03-01", "1900-02-28", "1900-03-01", "2024-03-01",
    "1752-09-14", "0999-12-31", "0400-02-28", "2000-12-31", "0004-03-01",
]
rng = random.Random(1)
for _ in range(80):
    y = rng.randint(1, 9999)
    m = rng.randint(1, 12)
    # valid day
    dmax = [0, 31, 29 if (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m]
    d = rng.randint(1, dmax)
    dates.append(f"{y:04d}-{m:02d}-{d:02d}")
wd_in = "".join(d + "\n" for d in dates)
wd_exp_lines = []
for d in dates:
    y, m, dd = map(int, d.split("-"))
    wd_exp_lines.append(names_py[datetime.date(y, m, dd).weekday()])
wd_exp = "\n".join(wd_exp_lines) + "\n"
check("weekday", "solutions/t1-weekday.res", wd_in, wd_exp)

# bignum
def big_line(a, b):
    return f"{a + b} {a * b}"

big_pairs = [
    (0, 0),
    (999, 1),
    (123, 456),
    (0, 12345),
    (12345, 0),
    (100, 100),
    (25, 4),
    (25, 25),
    (999999, 999999),
    (1, 0),
    (2, 3),
]
rng = random.Random(2)
for nlen in (1, 2, 5, 20, 50, 100):
    for _ in range(4):
        if nlen == 1:
            a = rng.randint(0, 9)
            b = rng.randint(0, 9)
        else:
            a = rng.randint(10 ** (nlen - 1), 10 ** nlen - 1)
            b = rng.randint(10 ** (nlen - 1), 10 ** nlen - 1)
        big_pairs.append((a, b))
# mixed lengths
big_pairs.append((10 ** 99, 1))
big_pairs.append((0, 10 ** 50))
big_pairs.append((999, 0))
big_in = "".join(f"{a} {b}\n" for a, b in big_pairs)
big_exp = "".join(big_line(a, b) + "\n" for a, b in big_pairs)
check("bignum", "solutions/t2-bignum.res", big_in, big_exp, timeout=30)

# life
life_cases = []
life_cases.append((1, ["...", "###", "..."]))
life_cases.append((2, ["...", "###", "..."]))
life_cases.append((0, ["##", "##"]))
life_cases.append((3, ["##", "##"]))
life_cases.append((1, ["#"]))
life_cases.append((5, ["#"]))
life_cases.append((2, ["."]))
life_cases.append((0, [".#.", "###", ".#."]))
life_cases.append((4, [".#.", "..#", "###"]))  # glider-ish in 3x3
rng = random.Random(3)
for rows, cols, g in [(1, 1, 0), (1, 5, 3), (5, 1, 2), (4, 6, 7), (8, 8, 10), (20, 20, 30)]:
    grid = []
    for _r in range(rows):
        grid.append("".join(rng.choice(".#") for _c in range(cols)))
    life_cases.append((g, grid))
for i, (g, grid) in enumerate(life_cases):
    inp = str(g) + "\n" + "\n".join(grid) + "\n"
    exp = life_run(g, grid)
    timeout = 30 if (len(grid) * len(grid[0]) * g) > 1000 else 15
    check(f"life {i} {g} {len(grid)}x{len(grid[0])}", "solutions/t2-life.res", inp, exp, timeout=timeout)

# rpn
rpn_lines = [
    "5 1 2 + 4 * + 3 -",
    "-7 2 /",
    "-7 2 %",
    "7 -2 /",
    "7 -2 %",
    "-7 -2 /",
    "-7 -2 %",
    "8 -3 /",
    "8 -3 %",
    "-8 3 /",
    "-8 3 %",
    "   4    5   *  ",
    "0 5 /",
    "0 5 %",
    "-0",
    "42",
    "",
    "   ",
    "+",
    "1 2 3 +",
    "1 0 /",
    "1 0 %",
    "1 +",
    "1 2 ^",
    "1 2 + 3",
    "+ 1 2",
    "1 2 + +",
    "1 2 3 + +",
    "10 3 /",
    "10 3 %",
    "-10 3 /",
    "-10 3 %",
    "10 -3 /",
    "10 -3 %",
    "-10 -3 /",
    "-10 -3 %",
    "007",
    "-007",
    "--1",
    "1-2",
    "+5",
    "4.5",
    "5 1 2 + 4 * + 3 - 0 /",
    "8 3 % 2 +",
    "-15 4 / 2 *",
    "2 3 4 * +",
]
rng = random.Random(4)
for _ in range(40):
    # build a valid expression with small ints
    vals = [rng.randint(-50, 50)]
    expr = [str(vals[0])]
    for _k in range(rng.randint(1, 8)):
        op = rng.choice(["+", "-", "*", "/", "%"])
        b = rng.randint(-20, 20)
        if op in ["/", "%"] and b == 0:
            b = 1
        a = vals.pop()
        vals.append(trunc_mod(a, b) if op == "%" else trunc_div(a, b) if op == "/" else a + b if op == "+" else a - b if op == "-" else a * b)
        expr.append(str(b))
        expr.append(op)
    rpn_lines.append(" ".join(expr))

rpn_in = "\n".join(rpn_lines) + "\n"
rpn_exp = "".join(rpn_eval(line) + "\n" for line in rpn_lines)
check("rpn", "solutions/t2-rpn.res", rpn_in, rpn_exp)
check("rpn empty file", "solutions/t2-rpn.res", "", "")

# wordfreq
wf_cases = [
    "The cat and THE hat.\n",
    "",
    "123 !!!\n",
    "Hello\n",
    "b a a\n",
    "b\na A\n",
    "m l k j i h g f e d c b a z y\n",
    "a a a b b c\n",
    "bb aa aa cc cc\n",
    "The CAT cat the\n",
    "Apple apple BANANA banana banana\n",
    "Don't stop, don't stop!\n",
    "abc123def abc\n",
    "a an and\n",
    "It's a test, it's a TEST!\n",
    "well-known well known\n",
]
# larger mixed text
rng = random.Random(5)
vocab = ["alpha", "beta", "Gamma", "delta", "Echo", "foxtrot", "golf", "hotel", "India", "juliet", "kilo", "Lima", "the", "And", "cat"]
lines = []
for _ in range(200):
    parts = []
    for _w in range(rng.randint(1, 8)):
        w = rng.choice(vocab)
        if rng.random() < 0.3:
            w = w.upper()
        elif rng.random() < 0.3:
            w = w.capitalize()
        parts.append(w)
        if rng.random() < 0.2:
            parts.append(rng.choice([",", ".", "!", "123", "-"]))
    lines.append(" ".join(parts))
wf_cases.append("\n".join(lines) + "\n")

for i, text in enumerate(wf_cases):
    check(f"words {i}", "solutions/t2-wordfreq.res", text, words_expected(text), timeout=30)

print("FAILS", fails)
sys.exit(1 if fails else 0)
