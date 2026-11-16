import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    if n > 0:
        sys.stdout.write("\n".join(str(i) for i in range(1, n + 1)) + "\n")

main()
