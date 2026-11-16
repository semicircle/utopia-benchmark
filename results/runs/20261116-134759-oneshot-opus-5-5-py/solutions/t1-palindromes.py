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
