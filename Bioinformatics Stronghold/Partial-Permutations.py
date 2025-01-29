n = 98
k = 8
r = 1
for i in range(n - k + 1, n + 1):
    r *= i

print(r % 1000000)