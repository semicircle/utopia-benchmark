import sys
from collections import Counter

def main():
    text = sys.stdin.read()
    counts = Counter()
    cur = []
    for ch in text:
        o = ord(ch)
        if 65 <= o <= 90:
            cur.append(chr(o + 32))
        elif 97 <= o <= 122:
            cur.append(ch)
        else:
            if cur:
                counts["".join(cur)] += 1
                cur = []
    if cur:
        counts["".join(cur)] += 1
    items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    out = ["%s %d" % (w, c) for w, c in items[:10]]
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
