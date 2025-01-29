#Problem 4:
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

def fibonacci_loop_pythonic(months, offsprings):
    parent, child = 1, 1
    for itr in range(months - 1):
        child, parent = parent, parent + (child * offsprings)
    return child

print(fibonacci_loop_pythonic(5, 3))

"""
o - small (children) rabbits. They have to mature and reproduce in the next cycle only.
0 - mature (parents) rabbits. They can reproduce and move to the next cycle.
Month 1: [o]
Month 2: [0]
Month 3: [0 o o]
Month 4: [0 o o 0 0]
Month 5: [0 o o 0 0 0 o o 0 o o]
Month 6: [0 o o 0 0 0 o o 0 o o 0 o o 0 0 0 o o 0 0]
"""