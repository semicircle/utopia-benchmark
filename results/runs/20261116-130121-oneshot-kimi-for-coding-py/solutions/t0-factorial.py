import sys
import math

data = sys.stdin.read().split()
n = int(data[0]) if data else 0
print(math.factorial(n))
