import sys
import bisect

def main():
    lines = sys.stdin.read().splitlines()
    arr = []
    queries = []
    if lines:
        first = lines[0].strip()
        if first:
            arr = [int(x) for x in first.split()]
        for line in lines[1:]:
            line = line.strip()
            if line:
                queries.append(int(line))
    out = []
    for q in queries:
        lo = bisect.bisect_left(arr, q)
        hi = bisect.bisect_right(arr, q)
        if hi > lo:
            out.append("%d found" % lo)
        else:
            out.append("%d missing" % lo)
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
