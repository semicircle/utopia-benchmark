<solution task="t0-count">
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    if n > 0:
        sys.stdout.write("\n".join(str(i) for i in range(1, n + 1)) + "\n")

main()
</solution>

<solution task="t0-day-names">
import sys

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def main():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if 1 <= n <= 7:
            out.append(days[n - 1])
        else:
            out.append("invalid")
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
</solution>

<solution task="t0-even-odd">
import sys

def main():
    even = 0
    odd = 0
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        if int(line) % 2 == 0:
            even += 1
        else:
            odd += 1
    sys.stdout.write("even %d\nodd %d\n" % (even, odd))

main()
</solution>

<solution task="t0-factorial">
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0]) if data else 0
    f = 1
    for i in range(2, n + 1):
        f *= i
    sys.stdout.write(str(f) + "\n")

main()
</solution>

<solution task="t0-fizzbuzz">
import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0]) if data else 0
    out = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
</solution>

<solution task="t0-hello">
print("Hello, Utopia!")
</solution>

<solution task="t0-reverse-lines">
import sys

def main():
    lines = sys.stdin.readlines()
    for line in reversed(lines):
        sys.stdout.write(line)

main()
</solution>

<solution task="t1-digits">
import sys

def main():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        neg = n < 0
        s = str(abs(n))
        total = 0
        for ch in s:
            total += ord(ch) - 48
        rev = int(s[::-1])
        if neg and rev != 0:
            rev = -rev
        out.append("%d %d" % (total, rev))
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
</solution>

<solution task="t1-floordiv">
import sys

def main():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        a = int(parts[0])
        b = int(parts[1])
        q = a // b
        r = a - b * q
        out.append("%d %d" % (q, r))
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
</solution>

<solution task="t1-palindromes">
import sys

def main():
    out = []
    for line in sys.stdin:
        line = line.rstrip("\n").rstrip("\r")
        chars = []
        for c in line:
            o = ord(c)
            if 48 <= o <= 57 or 65 <= o <= 90 or 97 <= o <= 122:
                if 65 <= o <= 90:
                    o += 32
                chars.append(chr(o))
        s = "".join(chars)
        if s == s[::-1]:
            out.append("yes")
        else:
            out.append("no")
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
</solution>

<solution task="t1-rank">
import sys
import bisect

def main():
    lines = sys.stdin.read().splitlines()
    arr = []
    queries = []
    if lines:
        first = lines[0].strip()
        if first:
            arr = [int(x) for x in first.split()]
        for line in lines[1:]:
            line = line.strip()
            if line:
                queries.append(int(line))
    out = []
    for q in queries:
        lo = bisect.bisect_left(arr, q)
        hi = bisect.bisect_right(arr, q)
        if hi > lo:
            out.append("%d found" % lo)
        else:
            out.append("%d missing" % lo)
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
</solution>

<solution task="t1-rotate">
import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    k = int(lines[0].strip())
    items = [l for l in lines[1:] if l != ""]
    n = len(items)
    if n == 0:
        return
    k %= n
    if k:
        items = items[-k:] + items[:-k]
    sys.stdout.write("\n".join(items) + "\n")

main()
</solution>

<solution task="t1-weekday">
import sys
from datetime import date

names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def main():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        y = int(line[0:4])
        m = int(line[5:7])
        d = int(line[8:10])
        out.append(names[date(y, m, d).weekday()])
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
</solution>

<solution task="t2-bignum">
import sys

def main():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        a = int(parts[0])
        b = int(parts[1])
        out.append("%d %d" % (a + b, a * b))
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
</solution>

<solution task="t2-life">
import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    g = int(lines[0].strip())
    grid = [list(l) for l in lines[1:] if l != ""]
    R = len(grid)
    C = len(grid[0]) if R else 0
    for _ in range(g):
        new = [row[:] for row in grid]
        for r in range(R):
            for c in range(C):
                cnt = 0
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        if dr == 0 and dc == 0:
                            continue
                        nr = r + dr
                        nc = c + dc
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == "#":
                            cnt += 1
                if grid[r][c] == "#":
                    new[r][c] = "#" if cnt == 2 or cnt == 3 else "."
                else:
                    new[r][c] = "#" if cnt == 3 else "."
        grid = new
    sys.stdout.write("\n".join("".join(row) for row in grid) + "\n")

main()
</solution>

<solution task="t2-rpn">
import sys

def is_int(tok):
    s = tok
    if s.startswith("-"):
        s = s[1:]
    if len(s) == 0:
        return False
    for ch in s:
        if not ("0" <= ch <= "9"):
            return False
    return True

def trunc_div(a, b):
    q = abs(a) // abs(b)
    if (a < 0) != (b < 0):
        q = -q
    return q

def main():
    out = []
    for line in sys.stdin:
        line = line.rstrip("\n").rstrip("\r")
        tokens = line.split()
        stack = []
        err = False
        for tok in tokens:
            if is_int(tok):
                stack.append(int(tok))
            elif tok in ("+", "-", "*", "/", "%"):
                if len(stack) < 2:
                    err = True
                    break
                b = stack.pop()
                a = stack.pop()
                if tok == "+":
                    stack.append(a + b)
                elif tok == "-":
                    stack.append(a - b)
                elif tok == "*":
                    stack.append(a * b)
                else:
                    if b == 0:
                        err = True
                        break
                    q = trunc_div(a, b)
                    if tok == "/":
                        stack.append(q)
                    else:
                        stack.append(a - b * q)
            else:
                err = True
                break
        if err or len(stack) != 1:
            out.append("error")
        else:
            out.append(str(stack[0]))
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
</solution>

<solution task="t2-wordfreq">
import sys
from collections import Counter

def main():
    text = sys.stdin.read()
    counts = Counter()
    cur = []
    for ch in text:
        o = ord(ch)
        if 65 <= o <= 90:
            cur.append(chr(o + 32))
        elif 97 <= o <= 122:
            cur.append(ch)
        else:
            if cur:
                counts["".join(cur)] += 1
                cur = []
    if cur:
        counts["".join(cur)] += 1
    items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    out = ["%s %d" % (w, c) for w, c in items[:10]]
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
</solution>