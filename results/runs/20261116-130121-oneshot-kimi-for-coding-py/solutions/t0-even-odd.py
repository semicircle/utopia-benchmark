import sys

even = 0
odd = 0
for line in sys.stdin.read().split():
    x = int(line)
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

sys.stdout.write("even %d\nodd %d\n" % (even, odd))
