def find_subsequence_indices(s, t):
    indices = []
    t_index = 0

    # Loop through s and look for characters of t in order
    for i, char in enumerate(s):
        if t_index < len(t) and char == t[t_index]:
            indices.append(i + 1)  # Use 1-based index
            t_index += 1
        if t_index == len(t):  # Stop if all characters of t are found
            break

    return indices if len(indices) == len(t) else None


# Example usage with FASTA parsing
def parse_fasta(fasta_str):
    sequences = {}
    label = None
    for line in fasta_str.strip().split("\n"):
        if line.startswith(">"):
            label = line[1:]  # Extract label without '>'
            sequences[label] = ""
        else:
            sequences[label] += line.strip()
    return list(sequences.values())


# Sample input in FASTA format
fasta_input = """>seq1
TCGGGCACCCTAGGCTTCCGCAAAGCTTGACACTTACTTAAGCCTTATAGTCAATTGGGG
GGTGTCTGCCTATCAATACCATTGCTATAATAAACACCCGACGATTGATTTCACGAGACC
TTCTACGCAATTCATCATTGTATAGCACAGCAAATTCACATCACTTGTTAACGAGCCAAA
ATGCAAGGCGCAGTGGTTACTCGCGATAAACGAAGTCCGGCTGTGCGTGCGGGGTGATGG
TTATACGTTATGGAGACGCGTCATCGTGTAACTGGAATAGAACACGAATCAACGTGAGTG
CATGCGACCTACCTAACGCACCGTTTCTTACAAGGAACTGGATTAAATGCCAATGGTCAC
TTCATGCCTCCCAGTGTTCACATTTTCAAGGAACGCTACTCGCGAATAGAGAGTCAGTTG
GCCAACAGTCATCTAACGGATCCCCGACGCTGCAAACTTCAGATAAAGTAACGGATATAT
TCAGCCTTCTCGCTAGGGCCCAGCAAGTTCTGACACTCTGTGCAGTCTCCCGGAGTTAGC
GCAATTTTGAAAATCTAATAGCCACGAGTCAAATGATCTCACGCTCACGAAGCAGAACCT
TGCTTCAGTACCCGACAGGAGGTTCTTGTAGTATGCGATATTAGATGTGGTTACGACAGG
AAGTAGTCGCCGCACCGCCCTATCAGGACTCCATGGCTCGCGGCTACGAAACATACTCCC
GTCCTCAAGGATCTCCGGCGGCCTGCGGTCAGGATAGGAACCAGACGGATTTGCCTACAA
TTTGGAAGGCCTAGAGGCAACGTCCGCTAAGGTCAACGGCGGCCACTATCATATACAGAG
AAGAAGGGCCGGAATCGCGCCAAAACAAGATGGAACACTGGCGGAGAAGATGATCACAAT
AGCTAG
>seq2
ACTAGTCTTAGCA"""

s, t = parse_fasta(fasta_input)
result = find_subsequence_indices(s, t)
print(" ".join(map(str, result)))
