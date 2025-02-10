#Open the file 'rosalind_mrna.txt' and read its contents
with open('rosalind_mrna.txt', 'r') as file:
    aa = file.read().strip()  # Read the protein string and remove any trailing whitespace

#Dictionary mapping amino acids to the number of codons that encode them
aa_dic = {
    'A': 4, 'R': 6, 'N': 2, 'D': 2, 'C': 2, 'Q': 2, 'E': 2, 'G': 4, 'H': 2, 'I': 3,
    'L': 6, 'K': 2, 'M': 1, 'F': 2, 'P': 4, 'S': 6, 'T': 4, 'W': 1, 'Y': 2, 'V': 4
}

stop = 3  #There are 3 possible stop codons in the genetic code

#Loop through each amino acid in the given protein sequence
for i in aa:
    stop *= aa_dic[i]  # Multiply the number of ways to encode each amino acid

#Compute the result modulo 1,000,000 to avoid very large numbers
print(stop % 1000000)



