import sys

days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    print(days.get(int(line), "invalid"))
