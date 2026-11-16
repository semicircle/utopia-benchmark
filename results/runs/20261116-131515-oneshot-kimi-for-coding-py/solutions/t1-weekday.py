import sys
from datetime import date

names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def main():
    out = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        y = int(line[0:4])
        m = int(line[5:7])
        d = int(line[8:10])
        out.append(names[date(y, m, d).weekday()])
    if out:
        sys.stdout.write("\n".join(out) + "\n")

main()
