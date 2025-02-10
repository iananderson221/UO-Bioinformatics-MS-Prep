def protein_weight(P):
    #Initialize total weight to 0
    weight = 0

    #Dictionary storing the monoisotopic mass of each amino acid
    amino_acid_masses = {
        "A": 71.03711,  # Alanine
        "C": 103.00919, # Cysteine
        "D": 115.02694, # Aspartic Acid
        "E": 129.04259, # Glutamic Acid
        "F": 147.06841, # Phenylalanine
        "G": 57.02146,  # Glycine
        "H": 137.05891, # Histidine
        "I": 113.08406, # Isoleucine
        "K": 128.09496, # Lysine
        "L": 113.08406, # Leucine
        "M": 131.04049, # Methionine
        "N": 114.04293, # Asparagine
        "P": 97.05276,  # Proline
        "Q": 128.05858, # Glutamine
        "R": 156.10111, # Arginine
        "S": 87.03203,  # Serine
        "T": 101.04768, # Threonine
        "V": 99.06841,  # Valine
        "W": 186.07931, # Tryptophan
        "Y": 163.06333  # Tyrosine
    }

    #Loop through each amino acid in the protein sequence
    for amino_acid in P:
        if amino_acid in amino_acid_masses:
            weight += amino_acid_masses[amino_acid]  #Add its mass to the total weight

    return weight  #Return the total weight of the protein sequence


#Example protein sequence
P = "SKADYEK"


result = protein_weight(P)


print(result)


