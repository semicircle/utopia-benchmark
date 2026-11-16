import sys

lines = sys.stdin.read().splitlines()
out = "\n".join(reversed(lines))
if out:
    sys.stdout.write(out + "\n")
