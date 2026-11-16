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
