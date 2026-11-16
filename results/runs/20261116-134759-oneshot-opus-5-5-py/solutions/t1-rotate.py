import sys
data = sys.stdin.read()
lines = data.split('\n')
if lines and lines[-1] == '':
    lines.pop()
if lines:
    k = int(lines[0].strip())
    items = lines[1:]
    n = len(items)
    if n:
        s = k % n
        if s:
            items = items[-s:] + items[:-s]
        sys.stdout.write("\n".join(items) + "\n")
