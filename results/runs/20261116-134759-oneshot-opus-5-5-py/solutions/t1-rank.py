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
