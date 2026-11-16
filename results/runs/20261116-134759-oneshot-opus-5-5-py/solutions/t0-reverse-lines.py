import sys
data = sys.stdin.read()
lines = data.split('\n')
if lines and lines[-1] == '':
    lines.pop()
lines.reverse()
if lines:
    sys.stdout.write("\n".join(lines) + "\n")
