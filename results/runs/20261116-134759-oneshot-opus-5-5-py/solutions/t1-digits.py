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
