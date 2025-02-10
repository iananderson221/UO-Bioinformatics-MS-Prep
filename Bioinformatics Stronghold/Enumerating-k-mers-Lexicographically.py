import itertools  #Import the itertools module for generating Cartesian products

#Define the alphabet as a space-separated string
text = "A C G T"

#Define the length of the strings to generate
n = 2

#Split the input string into a list of characters
alphabet = text.split()  #Converts "A C G T" into ['A', 'C', 'G', 'T']

#Generate all possible ordered combinations of length 'n' using the given alphabet
combinations = sorted("".join(l) for l in itertools.product(alphabet, repeat=n))

#Print each combination on a new line
print("\n".join(combinations))
