import sys

even = 0
odd = 0
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    if int(line) % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"even {even}")
print(f"odd {odd}")
