# Edit code
def rna_splicing():
    # Codon translation table
    table = {
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
        "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
    }

    # Open and read the file using a context manager
    with open("rosalind_splc.txt", "r") as file:
        lines = file.readlines()

    # Extract sequences: First line is header, remaining lines are the sequences
    introns = []
    buffer = ''
    for line in lines:
        if line.startswith('>'):
            if buffer:
                introns.append(buffer)
            buffer = ''
        else:
            buffer += line.strip()  # Removing newline characters
    introns.append(buffer)  # Add the last sequence (the final exon)

    # The first sequence is the full sequence (including exons and introns)
    seq = introns.pop(0)

    # Remove introns from the sequence
    for intron in introns:
        seq = seq.replace(intron, "")

    # Convert DNA to RNA (T -> U)
    seq = seq.replace('T', 'U')

    # Translate RNA to protein
    protein = ''
    for i in range(0, len(seq) - 2, 3):  # Step by 3 to get codons
        codon = seq[i:i + 3]
        amino_acid = table.get(codon, None)
        if amino_acid == 'Stop' or amino_acid is None:
            break
        protein += amino_acid

    print(protein)


rna_splicing()
