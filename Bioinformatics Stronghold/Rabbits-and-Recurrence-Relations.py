Solution 1:
def rabbit_pairs(n, k):
    if n == 1 or n == 2:
        return 1
    rabbits = [0] * n
    rabbits[0] = 1
    rabbits[1] = 1

    for i in range(2, n):
        rabbits[i] = rabbits[i - 1] + k * rabbits[i - 2]
    return rabbits[-1]


# Sample dataset
n = 36
k = 4

# Get the result
result = rabbit_pairs(n, k)

# Print the result
print(result)

Solution 2:
def rabbit_pairs(n, k):
    parent, child = 1, 1
    for i in range(n - 1):
        parent, child = parent, parent + (child * k)
    return child

print(rabbit_pairs(5, 3))

