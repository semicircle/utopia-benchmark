import sys
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
out = []
for line in sys.stdin.read().splitlines():
    s = line.strip()
    if not s:
        continue
    try:
        n = int(s)
    except ValueError:
        out.append("invalid")
        continue
    out.append(DAYS[n - 1] if 1 <= n <= 7 else "invalid")
sys.stdout.write("".join(s + "\n" for s in out))
