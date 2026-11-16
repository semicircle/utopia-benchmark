import sys
n = int(sys.stdin.read().split()[0])
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
sys.stdout.write("".join(s + "\n" for s in out))
