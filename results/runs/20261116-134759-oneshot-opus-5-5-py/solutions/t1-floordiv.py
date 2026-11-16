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
