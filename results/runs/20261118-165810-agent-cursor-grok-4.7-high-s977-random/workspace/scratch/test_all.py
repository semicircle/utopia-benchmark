#!/usr/bin/env python3
import datetime
import math
import random
import re
import subprocess
import sys
from collections import Counter

BIN = "bin/dushpek"
SOL = "solutions"
fails = 0


def run(name, data=""):
    if not data.endswith("\n") and data != "":
        data = data + "\n"
    p = subprocess.run(
        [BIN, "run", f"{SOL}/{name}.dus"],
        input=data,
        text=True,
        capture_output=True,
    )
    if p.returncode != 0:
        return f"EXIT {p.returncode}\nSTDOUT:\n{p.stdout}\nSTDERR:\n{p.stderr}"
    return p.stdout


def check(name, data, expected, label=None):
    global fails
    got = run(name, data)
    if not expected.endswith("\n") and expected != "":
        expected = expected + "\n"
    if expected == "" and data == "":
        # run() won't add newline to empty data; expected empty stays empty
        pass
    if got != expected:
        fails += 1
        lab = label or name
        print(f"FAIL {lab}")
        print("DATA:", repr(data[:300]))
        print("EXPECTED:", repr(expected[:500]))
        print("GOT:", repr(got[:500]))
        print("---")


def check_raw(name, data, expected, label=None):
    """data and expected used exactly, no added newline."""
    global fails
    p = subprocess.run(
        [BIN, "run", f"{SOL}/{name}.dus"],
        input=data,
        text=True,
        capture_output=True,
    )
    got = p.stdout if p.returncode == 0 else f"EXIT {p.returncode}\n{p.stdout}\n{p.stderr}"
    if got != expected:
        fails += 1
        lab = label or name
        print(f"FAIL {lab}")
        print("DATA:", repr(data[:400]))
        print("EXPECTED:", repr(expected[:600]))
        print("GOT:", repr(got[:600]))
        print("---")


# hello
check_raw("t0-hello", "", "Hello, Utopia!\n", "hello")

# factorial
for n in range(0, 21):
    check_raw("t0-factorial", f"{n}\n", f"{math.factorial(n)}\n", f"fact {n}")

# count
check_raw("t0-count", "0\n", "", "count 0")
check_raw("t0-count", "1\n", "1\n", "count 1")
check_raw("t0-count", "5\n", "1\n2\n3\n4\n5\n", "count 5")

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

for n in [1, 2, 3, 5, 15, 16, 100]:
    check_raw("t0-fizzbuzz", f"{n}\n", fizz(n), f"fizz {n}")

# even odd
def evenodd(nums):
    e = sum(1 for x in nums if x % 2 == 0)
    o = len(nums) - e
    return f"even {e}\nodd {o}\n"

check_raw("t0-even-odd", "", evenodd([]), "eo empty")
check_raw("t0-even-odd", "1\n2\n-3\n-4\n0\n", evenodd([1, 2, -3, -4, 0]), "eo mix")
check_raw("t0-even-odd", "-1\n-2\n1000000\n-1000000\n", evenodd([-1, -2, 1000000, -1000000]), "eo big")

# day names
names = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
inp = "\n".join(str(x) for x in [1, 2, 3, 4, 5, 6, 7, 0, 8, -1, 9, 100]) + "\n"
exp = "\n".join(names.get(x, "invalid") for x in [1, 2, 3, 4, 5, 6, 7, 0, 8, -1, 9, 100]) + "\n"
check_raw("t0-day-names", inp, exp, "days")
check_raw("t0-day-names", "", "", "days empty")

# reverse lines
check_raw("t0-reverse-lines", "", "", "rev empty")
check_raw("t0-reverse-lines", "only\n", "only\n", "rev one")
check_raw("t0-reverse-lines", "a\nb\nc\n", "c\nb\na\n", "rev three")
check_raw("t0-reverse-lines", "a\n\nb\n", "b\n\na\n", "rev blank")
check_raw("t0-reverse-lines", "  x  \ny\n", "y\n  x  \n", "rev spaces")
check_raw("t0-reverse-lines", "no nl", "no nl\n", "rev no final nl")

# floordiv
def fd_line(a, b):
    q, r = divmod(a, b)
    return f"{q} {r}"

pairs = [
    (7, 2), (-7, 2), (7, -2), (-7, -2),
    (8, 2), (-8, 2), (8, -2), (-8, -2),
    (5, 3), (-5, 3), (5, -3), (-5, -3),
    (1, 1), (-1, 1), (1, -1), (-1, -1),
    (0, 1), (0, -5), (10**9, 3), (-10**9, 3),
    (10**9, -1), (-10**9, -1), (10**9, 10**9),
    (-10**9, 999999999), (1, -999999999),
    (-1, 2), (1, 2), (-3, 2), (3, -2),
]
text = "\n".join(f"{a} {b}" for a, b in pairs) + "\n"
exp = "\n".join(fd_line(a, b) for a, b in pairs) + "\n"
check_raw("t1-floordiv", text, exp, "floordiv")
check_raw("t1-floordiv", "", "", "floordiv empty")

# digits
def dig(n):
    s = str(abs(n))
    sm = sum(int(c) for c in s)
    rev = int(s[::-1])
    if n < 0:
        rev = -rev
    return f"{sm} {rev}"

nums = [123, -4500, 0, -5, 10, 100, -100, 999, 20, -20, 10**15, -10**15,
        10**15 - 1, -(10**15 - 1), 1000000000000000, 7, -7, 11, 101, -1010]
text = "\n".join(str(n) for n in nums) + "\n"
exp = "\n".join(dig(n) for n in nums) + "\n"
check_raw("t1-digits", text, exp, "digits")

# weekday
dates = [
    (2000, 1, 1), (1970, 1, 1), (1, 1, 1), (1, 3, 1), (4, 2, 29),
    (1900, 2, 28), (1900, 3, 1), (2000, 2, 29), (2000, 3, 1),
    (2024, 2, 29), (2024, 1, 1), (9999, 12, 31), (1582, 10, 15),
    (2023, 11, 18), (1999, 12, 31), (2004, 2, 29), (1900, 1, 1),
    (400, 2, 29), (100, 3, 1), (99, 12, 31),
]
lines = [f"{y:04d}-{m:02d}-{d:02d}" for y, m, d in dates]
exp_lines = [datetime.date(y, m, d).strftime("%A") for y, m, d in dates]
check_raw("t1-weekday", "\n".join(lines) + "\n", "\n".join(exp_lines) + "\n", "weekday")
# many random dates
random.seed(1)
more = []
for _ in range(200):
    y = random.randint(1, 9999)
    m = random.randint(1, 12)
    # valid day
    for dtry in range(31, 0, -1):
        try:
            datetime.date(y, m, dtry)
            more.append((y, m, dtry))
            break
        except ValueError:
            pass
lines = [f"{y:04d}-{m:02d}-{d:02d}" for y, m, d in more]
exp_lines = [datetime.date(y, m, d).strftime("%A") for y, m, d in more]
check_raw("t1-weekday", "\n".join(lines) + "\n", "\n".join(exp_lines) + "\n", "weekday random")

# rotate
def rotate(k, items):
    if not items:
        return ""
    k %= len(items)
    if k < 0:
        k += len(items)
    # python % already non-negative if len>0
    rot = items[-k:] + items[:-k] if k else items
    return "\n".join(rot) + "\n"

check_raw("t1-rotate", "1\n", "", "rot none")
check_raw("t1-rotate", "0\na\nb\nc\n", rotate(0, ["a", "b", "c"]), "rot 0")
check_raw("t1-rotate", "1\na\nb\nc\nd\n", rotate(1, ["a", "b", "c", "d"]), "rot 1")
check_raw("t1-rotate", "-1\na\nb\nc\nd\n", rotate(-1, ["a", "b", "c", "d"]), "rot -1")
check_raw("t1-rotate", "4\na\nb\nc\nd\n", rotate(4, ["a", "b", "c", "d"]), "rot n")
check_raw("t1-rotate", "-4\na\nb\nc\nd\n", rotate(-4, ["a", "b", "c", "d"]), "rot -n")
check_raw("t1-rotate", "5\na\nb\nc\nd\n", rotate(5, ["a", "b", "c", "d"]), "rot n+1")
check_raw("t1-rotate", "-5\na\nb\nc\nd\n", rotate(-5, ["a", "b", "c", "d"]), "rot -n-1")
check_raw("t1-rotate", "1000000000\na\nb\nc\n", rotate(1000000000, ["a", "b", "c"]), "rot big")
check_raw("t1-rotate", "-1000000000\na\nb\nc\n", rotate(-1000000000, ["a", "b", "c"]), "rot -big")
check_raw("t1-rotate", "2\n\nhello\n  x\n", rotate(2, ["", "hello", "  x"]), "rot blanks")
check_raw("t1-rotate", "0\nonly\n", "only\n", "rot one")
check_raw("t1-rotate", "7\nonly\n", "only\n", "rot one k")
check_raw("t1-rotate", "-3\nonly\n", "only\n", "rot one neg")

# rank
def rank_out(nums, queries):
    lines = []
    for q in queries:
        smaller = sum(1 for x in nums if x < q)
        status = "found" if q in nums else "missing"
        lines.append(f"{smaller} {status}")
    return "\n".join(lines) + ("\n" if lines else "")

check_raw("t1-rank", "1 3 5 7\n5\n4\n1\n8\n0\n3\n7\n", rank_out([1, 3, 5, 7], [5, 4, 1, 8, 0, 3, 7]), "rank ex")
check_raw("t1-rank", "1 3 3 5\n3\n4\n1\n2\n5\n0\n", rank_out([1, 3, 3, 5], [3, 4, 1, 2, 5, 0]), "rank dups")
check_raw("t1-rank", "\n1\n0\n", rank_out([], [1, 0]), "rank empty nums")
check_raw("t1-rank", "-5 -5 -1 0 2\n-5\n-4\n2\n3\n-6\n", rank_out([-5, -5, -1, 0, 2], [-5, -4, 2, 3, -6]), "rank neg")
check_raw("t1-rank", "42\n", "", "rank no queries")
check_raw("t1-rank", "", "", "rank no input")
check_raw("t1-rank", "1 1 1 1\n1\n2\n0\n", rank_out([1, 1, 1, 1], [1, 2, 0]), "rank all same")

# palindromes
def is_pal_line(s):
    t = re.sub(r"[^A-Za-z0-9]", "", s).lower()
    return "yes" if t == t[::-1] else "no"

pals = [
    "A man, a plan, a canal: Panama!",
    "race a car",
    "",
    ".,!",
    "a",
    "ab",
    "Aa",
    "No 'x' in Nixon",
    "12321",
    "123a321",
    "12 21",
    "a.",
    "ab",
    "Aba",
    "abc",
    "0",
    "10",
    "11",
    "Was it a rat I saw?",
    "Not a palindrome",
    "A1b2B1a",
    "A1b2b1A",
    "---",
    "x",
    "xyx",
    "xyYx",
    "xyZy",
]
check_raw("t1-palindromes", "\n".join(pals) + "\n", "\n".join(is_pal_line(s) for s in pals) + "\n", "pals")
check_raw("t1-palindromes", "", "", "pals empty")
check_raw("t1-palindromes", "\n\n", "yes\nyes\n", "pals blank lines")

# life
def life_step(grid):
    rows = len(grid)
    cols = len(grid[0])
    new = []
    for r in range(rows):
        row = []
        for c in range(cols):
            nbs = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "#":
                        nbs += 1
            if grid[r][c] == "#":
                row.append("#" if nbs in (2, 3) else ".")
            else:
                row.append("#" if nbs == 3 else ".")
        new.append("".join(row))
    return new

def life_run(g, grid):
    for _ in range(g):
        grid = life_step(grid)
    return "\n".join(grid) + "\n"

def life_input(g, grid):
    return str(g) + "\n" + "\n".join(grid) + "\n"

blink = ["...", "###", "..."]
check_raw("t2-life", life_input(0, blink), life_run(0, blink), "life g0")
check_raw("t2-life", life_input(1, blink), life_run(1, blink), "life blink1")
check_raw("t2-life", life_input(2, blink), life_run(2, blink), "life blink2")
check_raw("t2-life", life_input(3, blink), life_run(3, blink), "life blink3")
block = ["##", "##"]
check_raw("t2-life", life_input(5, block), life_run(5, block), "life block")
single = ["#"]
check_raw("t2-life", life_input(1, single), life_run(1, single), "life single")
# glider-ish
glider = [
    "......",
    "..#...",
    "...#..",
    ".###..",
    "......",
    "......",
]
check_raw("t2-life", life_input(4, glider), life_run(4, glider), "life glider")
random.seed(2)
for trial, (R, C, G) in enumerate([(5, 5, 3), (8, 3, 6), (20, 20, 30), (1, 5, 2), (4, 1, 4)]):
    grid = []
    for _r in range(R):
        grid.append("".join("#" if random.random() < 0.3 else "." for _c in range(C)))
    check_raw("t2-life", life_input(G, grid), life_run(G, grid), f"life rand {trial} {R}x{C} g{G}")

# rpn
def trunc_div(a, b):
    q = abs(a) // abs(b)
    if (a < 0) != (b < 0):
        q = -q
    return q

def rpn_eval(line):
    toks = line.split()
    if not toks:
        return "error"
    stack = []
    for t in toks:
        if re.fullmatch(r"-?\d+", t) and not (t.startswith("-") and len(t) == 1):
            # "-?" allows "-" alone? fullmatch -?\d+ does NOT match "-" because \d+ needs a digit.
            # It also doesn't match "+" . Good.
            # It DOES match "00" and "-0". Spec allows digits. OK.
            stack.append(int(t))
        elif t in {"+", "-", "*", "/", "%"}:
            if len(stack) < 2:
                return "error"
            b = stack.pop()
            a = stack.pop()
            if t in {"/", "%"} and b == 0:
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
                stack.append(a - b * trunc_div(a, b))
        else:
            return "error"
    if len(stack) != 1:
        return "error"
    return str(stack[0])

rpn_lines = [
    "5 1 2 + 4 * + 3 -",
    "-7 2 /",
    "-7 2 %",
    "7 -2 /",
    "7 -2 %",
    "-7 -2 /",
    "-7 -2 %",
    "5 2 /",
    "5 2 %",
    "-5 2 /",
    "-5 2 %",
    "5 -2 /",
    "5 -2 %",
    "-5 -2 /",
    "-5 -2 %",
    "4 2 /",
    "1",
    "1 2",
    "+",
    "1 0 /",
    "1 0 %",
    "1 2 + 3",
    "2 3 -",
    "3 2 -",
    "5   1 +",
    "  5 1 +",
    "",
    "   ",
    "1 2 &",
    "1 a +",
    "--1",
    "+1",
    "1 +",
    "foo",
    "-0 5 +",
    "8 3 %",
    "8 3 /",
    "-8 3 /",
    "-8 3 %",
    "8 -3 /",
    "8 -3 %",
    "-8 -3 /",
    "-8 -3 %",
    "2 3 * 4 +",
    "10 3 / 3 %",  # this is (10/3)=3 then 3% needs two values? tokens: 10, 3, /, 3, %
    # stack: push 10, push 3, div -> 3, push 3, mod -> 0. OK one value.
    "1 2 + +",
    "42",
    "-0",
    "0 0 *",
    "0 1 -",
    "9 2 1 + /",
]
# fix comment line accidentally? I didn't include comments in the list. Good.
# Wait I have a comment in the python list as a string? No, the comment is a python comment between elements.
# "10 3 / 3 %" is in the list. Good.

exp = "\n".join(rpn_eval(s) for s in rpn_lines) + "\n"
check_raw("t2-rpn", "\n".join(rpn_lines) + "\n", exp, "rpn")
# line without trailing content already covered

# bignum
def big_line(a, b):
    return f"{a + b} {a * b}"

big_cases = [
    (999, 1),
    (0, 0),
    (0, 123),
    (123, 0),
    (5, 5),
    (99, 99),
    (100, 100),
    (999, 999),
    (1, 1),
    (2, 3),
    (10, 10),
    (999999, 999999),
]
random.seed(3)
for _ in range(30):
    la = random.randint(1, 40)
    lb = random.randint(1, 40)
    if la == 1:
        a = random.randint(0, 9)
    else:
        a = random.randint(10 ** (la - 1), 10 ** la - 1)
    if lb == 1:
        b = random.randint(0, 9)
    else:
        b = random.randint(10 ** (lb - 1), 10 ** lb - 1)
    big_cases.append((a, b))
# 100-digit extremes
big_cases.append((int("9" * 100), 1))
big_cases.append((int("9" * 100), int("9" * 100)))
big_cases.append((0, int("9" * 50)))
big_cases.append((int("1" + "0" * 99), int("1" + "0" * 99)))
text = "\n".join(f"{a} {b}" for a, b in big_cases) + "\n"
exp = "\n".join(big_line(a, b) for a, b in big_cases) + "\n"
check_raw("t2-bignum", text, exp, "bignum")
check_raw("t2-bignum", "", "", "bignum empty")

# wordfreq
def wordfreq(text):
    words = [w.lower() for w in re.findall(r"[A-Za-z]+", text)]
    cnt = Counter(words)
    items = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[:10]
    if not items:
        return ""
    return "\n".join(f"{w} {c}" for w, c in items) + "\n"

samples = [
    "The cat and THE hat.",
    "",
    "!!! ???",
    "don't stop",
    "Aaa AAA aaa bbb BBB",
    "one",
    "b b b\na a\nc c\nd d\ne e\nf f\ng g\nh h\ni i\nj j\nk k\nl l\nm\n",
    "apple app an and apple bee be a Bee",
    "well-known well known\nThe THE the",
    "abc123def ABC xyz",
    "\n".join(["word" + str(i) for i in range(15)]),
    "Same same SAME different Different",
]
for i, s in enumerate(samples):
    raw = s if s.endswith("\n") or s == "" else s + "\n"
    # For samples that are a single line without wanting extra, wordfreq of the text
    # Our program reads lines. Newline doesn't create letters so it's the same as spaces
    # except words don't cross... newline is a separator either way since it's not a letter
    # and we process line by line. Equivalent to the newline being a separator.
    check_raw("t2-wordfreq", raw if raw.endswith("\n") or raw == "" else raw + "\n", wordfreq(raw), f"wf {i}")

# larger wordfreq
random.seed(4)
vocab = ["the", "cat", "and", "hat", "dog", "apple", "app", "banana", "band", "car",
         "Car", "DOG", "a", "an", "be", "bee", "zoo", "applepie", "pie", "to"]
lines = []
for _ in range(400):
    k = random.randint(1, 8)
    lines.append(" ".join(random.choice(vocab) + random.choice(["", ",", ".", "!"]) for _ in range(k)))
text = "\n".join(lines) + "\n"
check_raw("t2-wordfreq", text, wordfreq(text), "wf large")

print("FAILS", fails)
sys.exit(1 if fails else 0)
