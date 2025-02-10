import math #Import math module to use math.prod() to compute the result

n = 21
k = 7

#Calculate the product of numbers from (n-k+1) to n
r = math.prod(range(n - k + 1, n + 1)) % 1000000  #Compute the product and take modulo 1000000

print(r)

