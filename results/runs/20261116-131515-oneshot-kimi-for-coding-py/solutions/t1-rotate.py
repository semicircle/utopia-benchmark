import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    k = int(lines[0].strip())
    items = [l for l in lines[1:] if l != ""]
    n = len(items)
    if n == 0:
        return
    k %= n
    if k:
        items = items[-k:] + items[:-k]
    sys.stdout.write("\n".join(items) + "\n")

main()
