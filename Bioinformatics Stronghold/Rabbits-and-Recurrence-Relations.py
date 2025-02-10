Solution 1:
def rabbit_pairs(n, k):
    #If there's 1 or 2 months, we start with 1 pair of rabbits
    if n == 1 or n == 2:
        return 1

    #Initialize a list to store the number of rabbits for each month
    rabbits = [0] * n
    rabbits[0] = 1  #1st month has 1 pair of rabbits
    rabbits[1] = 1  #2nd month also has 1 pair of rabbits

    #Loop to compute the number of rabbits for each subsequent month
    for i in range(2, n):
        rabbits[i] = rabbits[i - 1] + k * rabbits[i - 2]  # Add new pairs born from rabbits[i-2]

    #Return the total number of rabbit pairs in the nth month
    return rabbits[-1]



n = 36  #The number of months
k = 4  #Number of offspring produced by each pair of rabbits

result = rabbit_pairs(n, k)

print(result)

Solution 2:


def rabbit_pairs(n, k):
    #Initialize two variables to represent the number of rabbits
    #parent: represents the number of mature rabbits from the previous month
    #child: represents the number of new rabbits born
    parent, child = 1, 1

    #Loop over the months (n-1 iterations since we start with the first month)
    for i in range(n - 1):
        parent, child = parent, parent + (child * k)
        #Update 'parent' to the previous 'child', and calculate the new 'child'

    #Return the number of child rabbits after all months
    return child

print(rabbit_pairs(5, 3))


