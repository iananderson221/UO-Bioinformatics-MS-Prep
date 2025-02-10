#Solution 1:
def dna_to_rna(t):
    #Initialize an empty string to store the RNA sequence
    rna_sequence = ""

    #Loop through each nucleotide in the given DNA sequence
    for nt in t:
        #If the nucleotide is "T", replace it with "U"
        if nt == "T":
            rna_sequence += "U"  # Add "U" to the RNA sequence
        else:
            rna_sequence += nt  # Otherwise, add the nucleotide as it is (A, C, or G)

    #Return the final RNA sequence
    return rna_sequence

#Solution 2:
def dna_to_rna(t):
    #Use Python's string replace method to convert all occurrences of "T" to "U"
    rna_sequence = t.replace("T", "U")  # Replace "T" with "U" in the DNA sequence

    #Return the modified RNA sequence
    return rna_sequence

t = "GATGGAACTTGACTACGTAAATT"

result = dna_to_rna(t)

print(result)
