def reverse_complement(pattern):
    pattern = reverse(pattern)  #Reverse the sequence
    pattern = complement(pattern)  #Complement each nucleotide
    return pattern


def reverse(pattern):
    rev = ""
    for char in pattern:
        rev = char + rev  #Add each character to the beginning to reverse the string
    return rev


def complement(pattern):
    complement = ""  #Initialize an empty string to store the complement
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


#Example DNA sequence
pattern = "AAAACCCGGT"


print(reverse_complement(pattern))

