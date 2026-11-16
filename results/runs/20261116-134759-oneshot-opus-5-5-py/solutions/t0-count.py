import sys
data = sys.stdin.read().split()
n = int(data[0]) if data else 0
out = [str(i) for i in range(1, n + 1)]
if out:
    sys.stdout.write("\n".join(out) + "\n")
