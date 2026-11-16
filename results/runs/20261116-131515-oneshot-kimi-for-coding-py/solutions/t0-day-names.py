import sys

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def main():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        if 1 <= n <= 7:
            out.append(days[n - 1])
        else:
            out.append("invalid")
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
