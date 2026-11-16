import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0]) if data else 0
    f = 1
    for i in range(2, n + 1):
        f *= i
    sys.stdout.write(str(f) + "\n")

main()
