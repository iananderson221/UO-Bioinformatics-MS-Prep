def rna_to_protein(s):
    #Initialize an empty string to store the resulting protein sequence
    protein = ""

    #Define the RNA codon table that maps RNA codons to their corresponding amino acids or "Stop" signals
    rna_codon_table = {
        "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
        "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
        "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
        "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
        "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
        "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
        "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
        "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
        "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
        "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
        "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
        "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
        "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
        "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
        "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
        "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G",
    }

    #Loop through the RNA sequence in steps of 3 (to extract each codon)
    for i in range(0, len(s) - len(s) % 3, 3):
        codon = s[i:i + 3]  # Extract a 3-nucleotide long codon

        #Check if the codon is present in the codon table
        if codon in rna_codon_table:
            amino_acid = rna_codon_table[codon]  # Get the corresponding amino acid or "Stop"

            #If we encounter a "Stop" codon, stop the translation process
            if amino_acid == "Stop":
                break

            #Add the amino acid to the protein sequence
            protein += amino_acid

    return protein  #Return the final protein sequence

s = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

print(rna_to_protein(s))


