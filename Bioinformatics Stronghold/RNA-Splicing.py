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

    # Read FASTA file
    with open("rosalind_splc.txt", "r") as file:
        sequences = file.read().strip().split(">")[1:]  # Split into sequences, ignore first empty split
        sequences = ["".join(seq.split("\n")[1:]) for seq in sequences]  # Remove headers, join sequences

    # The first sequence is the full DNA sequence; the rest are introns
    dna_seq = sequences[0]
    introns = sequences[1:]

    # Remove introns
    for intron in introns:
        dna_seq = dna_seq.replace(intron, "")

    # Transcribe DNA to RNA
    rna_seq = dna_seq.replace("T", "U")

    # Translate RNA to protein
    protein = "".join(
        table.get(rna_seq[i:i + 3], "")  # Get amino acid from codon
        for i in range(0, len(rna_seq) - 2, 3)
        if table.get(rna_seq[i:i + 3]) != "Stop"
    )

    print(protein)


rna_splicing()

