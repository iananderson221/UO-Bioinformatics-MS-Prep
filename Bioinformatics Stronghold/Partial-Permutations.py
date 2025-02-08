import math

n = 21
k = 7
r = math.prod(range(n - k + 1, n + 1)) % 1000000

print(r)
