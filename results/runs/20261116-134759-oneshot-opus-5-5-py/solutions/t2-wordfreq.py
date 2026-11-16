import sys, re
text = sys.stdin.read().lower()
words = re.findall(r'[a-z]+', text)
cnt = {}
for w in words:
    cnt[w] = cnt.get(w, 0) + 1
items = sorted(cnt.items(), key=lambda x: (-x[1], x[0]))[:10]
out = ["%s %d" % (w, c) for w, c in items]
if out:
    sys.stdout.write("\n".join(out) + "\n")
