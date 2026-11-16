import sys

def main():
    lines = sys.stdin.readlines()
    for line in reversed(lines):
        sys.stdout.write(line)

main()
