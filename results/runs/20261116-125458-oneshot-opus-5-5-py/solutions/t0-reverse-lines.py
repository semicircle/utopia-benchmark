import sys
data = sys.stdin.read()
if data:
    lines = data.split('\n')
    if lines and lines[-1] == '':
        lines.pop()
    lines.reverse()
    sys.stdout.write("".join(l + "\n" for l in lines))
