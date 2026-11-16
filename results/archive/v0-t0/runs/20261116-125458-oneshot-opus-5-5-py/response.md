All seven solutions are straightforward. Where the input format leaves room for doubt, I made these choices:

- **Blank lines:** in the line-based tasks they are skipped.
- **Non-numeric lines:** in the day-names task they print `invalid`.
- **Reverse lines:** the input is split only on `\n`, so each line is printed exactly as read, including any other characters such as `\r`.

<solution task="t0-count">
import sys
data = sys.stdin.read().split()
n = int(data[0]) if data else 0
out = [str(i) for i in range(1, n + 1)]
if out:
    sys.stdout.write("\n".join(out) + "\n")
</solution>

<solution task="t0-day-names">
import sys
names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
out = []
for line in sys.stdin.read().split('\n'):
    s = line.strip()
    if not s:
        continue
    try:
        v = int(s)
    except ValueError:
        out.append("invalid")
        continue
    if 1 <= v <= 7:
        out.append(names[v - 1])
    else:
        out.append("invalid")
if out:
    sys.stdout.write("\n".join(out) + "\n")
</solution>

<solution task="t0-even-odd">
import sys
even = 0
odd = 0
for tok in sys.stdin.read().split():
    try:
        v = int(tok)
    except ValueError:
        continue
    if v % 2 == 0:
        even += 1
    else:
        odd += 1
print("even", even)
print("odd", odd)
</solution>

<solution task="t0-factorial">
import sys
data = sys.stdin.read().split()
n = int(data[0]) if data else 0
r = 1
for i in range(2, n + 1):
    r *= i
print(r)
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
if out:
    sys.stdout.write("\n".join(out) + "\n")
</solution>

<solution task="t0-hello">
print("Hello, Utopia!")
</solution>

<solution task="t0-reverse-lines">
import sys
data = sys.stdin.read()
if data:
    lines = data.split('\n')
    if lines and lines[-1] == '':
        lines.pop()
    lines.reverse()
    sys.stdout.write("".join(l + "\n" for l in lines))
</solution>