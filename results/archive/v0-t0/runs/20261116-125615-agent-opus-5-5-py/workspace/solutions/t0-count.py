import sys
n = int(sys.stdin.read().split()[0])
sys.stdout.write("".join(f"{i}\n" for i in range(1, n + 1)))
