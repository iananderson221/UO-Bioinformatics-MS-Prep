#Solution 1:
def nt_count(s):
    # Count occurrences of each nucleotide
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for nt in s:
        if nt == "A":
            count_a += 1
        elif nt == "C":
            count_c += 1
        elif nt == "G":
            count_g += 1
        elif nt == "T":
            count_t += 1
    # Return the counts as a formatted string
    return f"{count_a} {count_c} {count_g} {count_t}"

# Sample dataset
s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

# Get the result
result = nt_count(s)

# Print the result
print(result)

#Solution 2:
def nt_count(s):
    # Count occurrences of each nucleotide
    count_a = s.count('A')
    count_c = s.count('C')
    count_g = s.count('G')
    count_t = s.count('T')
    # Return the counts as a formatted string
    return f"{count_a} {count_c} {count_g} {count_t}"

# Sample dataset
s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

# Get the result
result = nt_count(s)

# Print the result
print(result)
