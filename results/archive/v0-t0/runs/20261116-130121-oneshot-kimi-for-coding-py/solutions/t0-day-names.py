import sys

names = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

out = []
for line in sys.stdin.read().split():
    try:
        d = int(line)
    except ValueError:
        out.append("invalid")
        continue
    out.append(names.get(d, "invalid"))

if out:
    sys.stdout.write("\n".join(out) + "\n")
