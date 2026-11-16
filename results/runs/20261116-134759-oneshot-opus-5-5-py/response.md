<solution task="t0-count">
import sys
data = sys.stdin.read().split()
n = int(data[0]) if data else 0
out = [str(i) for i in range(1, n + 1)]
if out:
    sys.stdout.write("\n".join(out) + "\n")
</solution>

<solution task="t0-day-names">
import sys
names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
out = []
for line in sys.stdin.read().split('\n'):
    s = line.strip()
    if not s:
        continue
    try:
        v = int(s)
    except ValueError:
        out.append("invalid")
        continue
    if 1 <= v <= 7:
        out.append(names[v - 1])
    else:
        out.append("invalid")
if out:
    sys.stdout.write("\n".join(out) + "\n")
</solution>

<solution task="t0-even-odd">
import sys
even = 0
odd = 0
for tok in sys.stdin.read().split():
    v = int(tok)
    if v % 2 == 0:
        even += 1
    else:
        odd += 1
print("even %d" % even)
print("odd %d" % odd)
</solution>

<solution task="t0-factorial">
import sys
data = sys.stdin.read().split()
n = int(data[0]) if data else 0
r = 1
for i in range(2, n + 1):
    r *= i
print(r)
</solution>

<solution task="t0-fizzbuzz">
import sys
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
</solution>

<solution task="t0-hello">
print("Hello, Utopia!")
</solution>

<solution task="t0-reverse-lines">
import sys
data = sys.stdin.read()
lines = data.split('\n')
if lines and lines[-1] == '':
    lines.pop()
lines.reverse()
if lines:
    sys.stdout.write("\n".join(lines) + "\n")
</solution>

<solution task="t1-digits">
import sys
out = []
for line in sys.stdin.read().split('\n'):
    s = line.strip()
    if not s:
        continue
    n = int(s)
    a = abs(n)
    ds = str(a)
    total = sum(int(c) for c in ds)
    r = int(ds[::-1])
    if n < 0:
        r = -r
    out.append("%d %d" % (total, r))
if out:
    sys.stdout.write("\n".join(out) + "\n")
</solution>

<solution task="t1-floordiv">
import sys
out = []
for line in sys.stdin.read().split('\n'):
    p = line.split()
    if len(p) < 2:
        continue
    a = int(p[0]); b = int(p[1])
    q, r = divmod(a, b)
    out.append("%d %d" % (q, r))
if out:
    sys.stdout.write("\n".join(out) + "\n")
</solution>

<solution task="t1-palindromes">
import sys
data = sys.stdin.read()
lines = data.split('\n')
if lines and lines[-1] == '':
    lines.pop()
out = []
for line in lines:
    s = [c.lower() for c in line if c.isascii() and c.isalnum()]
    out.append("yes" if s == s[::-1] else "no")
if out:
    sys.stdout.write("\n".join(out) + "\n")
</solution>

<solution task="t1-rank">
import sys, bisect
data = sys.stdin.read()
lines = data.split('\n')
if lines and lines[-1] == '':
    lines.pop()
out = []
if lines:
    arr = [int(x) for x in lines[0].split()]
    arr.sort()
    for line in lines[1:]:
        s = line.strip()
        if not s:
            continue
        q = int(s)
        i = bisect.bisect_left(arr, q)
        found = i < len(arr) and arr[i] == q
        out.append("%d %s" % (i, "found" if found else "missing"))
if out:
    sys.stdout.write("\n".join(out) + "\n")
</solution>

<solution task="t1-rotate">
import sys
data = sys.stdin.read()
lines = data.split('\n')
if lines and lines[-1] == '':
    lines.pop()
if lines:
    k = int(lines[0].strip())
    items = lines[1:]
    n = len(items)
    if n:
        s = k % n
        if s:
            items = items[-s:] + items[:-s]
        sys.stdout.write("\n".join(items) + "\n")
</solution>

<solution task="t1-weekday">
import sys, datetime
names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
out = []
for line in sys.stdin.read().split('\n'):
    s = line.strip()
    if not s:
        continue
    y, m, d = s.split('-')
    dt = datetime.date(int(y), int(m), int(d))
    out.append(names[dt.weekday()])
if out:
    sys.stdout.write("\n".join(out) + "\n")
</solution>

<solution task="t2-bignum">
import sys
out = []
for line in sys.stdin.read().split('\n'):
    p = line.split()
    if len(p) < 2:
        continue
    a = int(p[0]); b = int(p[1])
    out.append("%s %s" % (str(a + b), str(a * b)))
if out:
    sys.stdout.write("\n".join(out) + "\n")
</solution>

<solution task="t2-life">
import sys
data = sys.stdin.read().split('\n')
lines = [l.strip() for l in data]
lines = [l for l in lines if l != '']
g = int(lines[0])
grid = [list(r) for r in lines[1:]]
H = len(grid)
W = len(grid[0]) if H else 0
for _ in range(g):
    ng = []
    for i in range(H):
        row = []
        for j in range(W):
            c = 0
            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue
                    ii = i + di; jj = j + dj
                    if 0 <= ii < H and 0 <= jj < len(grid[ii]) and grid[ii][jj] == '#':
                        c += 1
            alive = grid[i][j] == '#'
            if alive and (c == 2 or c == 3):
                row.append('#')
            elif not alive and c == 3:
                row.append('#')
            else:
                row.append('.')
        ng.append(row)
    grid = ng
out = ["".join(r) for r in grid]
if out:
    sys.stdout.write("\n".join(out) + "\n")
</solution>

<solution task="t2-rpn">
import sys, re
num_re = re.compile(r'-?[0-9]+')

def evaluate(line):
    toks = line.split()
    if not toks:
        return None
    st = []
    for t in toks:
        if num_re.fullmatch(t):
            st.append(int(t))
        elif t in ('+', '-', '*', '/', '%'):
            if len(st) < 2:
                return None
            b = st.pop()
            a = st.pop()
            if t == '+':
                st.append(a + b)
            elif t == '-':
                st.append(a - b)
            elif t == '*':
                st.append(a * b)
            else:
                if b == 0:
                    return None
                q = abs(a) // abs(b)
                if (a < 0) != (b < 0):
                    q = -q
                if t == '/':
                    st.append(q)
                else:
                    st.append(a - b * q)
        else:
            return None
    if len(st) != 1:
        return None
    return st[0]

data = sys.stdin.read()
lines = data.split('\n')
if lines and lines[-1] == '':
    lines.pop()
out = []
for line in lines:
    r = evaluate(line)
    out.append("error" if r is None else str(r))
if out:
    sys.stdout.write("\n".join(out) + "\n")
</solution>

<solution task="t2-wordfreq">
import sys, re
text = sys.stdin.read().lower()
words = re.findall(r'[a-z]+', text)
cnt = {}
for w in words:
    cnt[w] = cnt.get(w, 0) + 1
items = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[:10]
out = ["%s %d" % (w, c) for w, c in items]
if out:
    sys.stdout.write("\n".join(out) + "\n")
</solution>