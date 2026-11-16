<solution task="t0-count">
import sys

data = sys.stdin.read().split()
n = int(data[0]) if data else 0
out = "\n".join(str(i) for i in range(1, n + 1))
if out:
    sys.stdout.write(out + "\n")
</solution>

<solution task="t0-day-names">
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
</solution>

<solution task="t0-even-odd">
import sys

even = 0
odd = 0
for line in sys.stdin.read().split():
    x = int(line)
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

sys.stdout.write("even %d\nodd %d\n" % (even, odd))
</solution>

<solution task="t0-factorial">
import sys
import math

data = sys.stdin.read().split()
n = int(data[0]) if data else 0
print(math.factorial(n))
</solution>

<solution task="t0-fizzbuzz">
import sys

data = sys.stdin.read().split()
n = int(data[0]) if data else 0

out = []
for i in range(1, n + 1):
    if i % 15 == 0:
        out.append("FizzBuzz")
    elif i % 3 == 0:
        out.append("Fizz")
    elif i % 5 == 0:
        out.append("Buzz")
    else:
        out.append(str(i))

sys.stdout.write("\n".join(out) + "\n")
</solution>

<solution task="t0-hello">
print("Hello, Utopia!")
</solution>

<solution task="t0-reverse-lines">
import sys

lines = sys.stdin.read().splitlines()
out = "\n".join(reversed(lines))
if out:
    sys.stdout.write(out + "\n")
</solution>