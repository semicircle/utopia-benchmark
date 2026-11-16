import sys
even = odd = 0
for tok in sys.stdin.read().split():
    if int(tok) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"even {even}")
print(f"odd {odd}")
