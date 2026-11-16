import sys
even = 0
odd = 0
for tok in sys.stdin.read().split():
    try:
        v = int(tok)
    except ValueError:
        continue
    if v % 2 == 0:
        even += 1
    else:
        odd += 1
print("even", even)
print("odd", odd)
