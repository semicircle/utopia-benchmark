import sys
data = sys.stdin.buffer.read()
lines = data.split(b"\n")
if lines and lines[-1] == b"":
    lines.pop()
sys.stdout.buffer.write(b"".join(l + b"\n" for l in reversed(lines)))
