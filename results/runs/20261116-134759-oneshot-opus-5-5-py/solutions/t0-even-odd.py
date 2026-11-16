import sys
even = 0
odd = 0
for tok in sys.stdin.read().split():
    v = int(tok)
    if v % 2 == 0:
        even += 1
    else:
        odd += 1
print("even %d" % even)
print("odd %d" % odd)
