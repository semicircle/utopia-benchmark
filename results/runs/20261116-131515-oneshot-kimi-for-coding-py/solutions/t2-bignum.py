import sys

def main():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        a = int(parts[0])
        b = int(parts[1])
        out.append("%d %d" % (a + b, a * b))
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
