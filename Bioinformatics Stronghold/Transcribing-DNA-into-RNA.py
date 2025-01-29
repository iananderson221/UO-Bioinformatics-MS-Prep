#Solution 1:
def dna_to_rna(t):
    for nt in t:
        if nt == "T":
            "".join("U")
        else:
            nt = "".join(nt)
    return t

#Solution 2:
def dna_to_rna(t):
    u = t.replace("T", "U")
    return u

# Sample dataset
t = "GATGGAACTTGACTACGTAAATT"

# Get the result
result = dna_to_rna(t)

# Print the result
print(result)
