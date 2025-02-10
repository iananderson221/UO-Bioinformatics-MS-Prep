#Open the file 'rosalind_revp.txt' and read its contents
with open('rosalind_revp.txt', 'r') as file:
    #Read all lines, remove the first line (FASTA header), and concatenate into a single string
    dna = ''.join(nt.strip() for nt in file.readlines()[1:])

#Dictionary to get the complement of each nucleotide
nt_comp = {'G': 'C', 'C': 'G', 'A': 'T', 'T': 'A'}

#Loop over all possible starting positions in the DNA sequence
for i in range(len(dna) - 3):  #Start from each nucleotide, ensuring at least a 4-base substring
    #Loop over all possible palindromic substring lengths (from 12 down to 4)
    for j in range(min(len(dna), i + 12), i + 3, -1):
        sub_dna = dna[i:j]  #Extract the substring from index `i` to `j`

        #Compute the reverse complement of the substring
        revcomp = ''.join(nt_comp[nt] for nt in sub_dna)[::-1]

        #Check if the substring is a reverse palindrome
        if sub_dna == revcomp:
            #Print the starting position (1-based index) and the length of the palindrome
            print(i + 1, j - i)
