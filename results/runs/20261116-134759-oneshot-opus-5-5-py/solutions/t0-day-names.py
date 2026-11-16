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
