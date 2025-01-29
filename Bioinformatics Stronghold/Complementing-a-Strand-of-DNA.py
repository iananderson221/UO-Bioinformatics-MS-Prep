def reverse_complement(pattern):
    pattern = reverse(pattern) #reverse all letters in a string
    pattern = complement(pattern) #complement each letter in a string
    return pattern

def reverse(pattern):
    rev = ""
    for char in pattern:
        rev = char + rev
    return rev

def complement(pattern):
    complement = ""
    for char in pattern:
        if char == "A":
            complement += "T"
        elif char == "T":
            complement += "A"
        elif char == "G":
            complement += "C"
        elif char == "C":
            complement += "G"
    return complement
pattern = "AAAACCCGGT"
print(reverse_complement(pattern))
