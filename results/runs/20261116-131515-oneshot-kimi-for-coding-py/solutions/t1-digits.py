import sys

def main():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        neg = n < 0
        s = str(abs(n))
        total = 0
        for ch in s:
            total += ord(ch) - 48
        rev = int(s[::-1])
        if neg and rev != 0:
            rev = -rev
        out.append("%d %d" % (total, rev))
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
