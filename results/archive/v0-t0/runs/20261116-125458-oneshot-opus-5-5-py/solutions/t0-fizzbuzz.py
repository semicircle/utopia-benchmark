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
