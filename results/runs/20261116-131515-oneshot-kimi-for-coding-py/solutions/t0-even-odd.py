import sys

def main():
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
    sys.stdout.write("even %d\nodd %d\n" % (even, odd))

main()
