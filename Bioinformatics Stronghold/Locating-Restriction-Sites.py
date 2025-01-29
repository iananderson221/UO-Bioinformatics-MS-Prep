with open('rosalind_revp.txt', 'r') as file:
    dna = ''.join(nt.strip() for nt in file.readlines()[1:])
nt_comp = {'G':'C','C':'G','A':'T','T':'A'}
for i in range(len(dna) - 3):
    for j in range(min(len(dna), i + 12), i + 3, -1):
        sub_dna = dna[i:j]
        revcomp = ''.join(nt_comp[num] for num in sub_dna)[::-1]
        if sub_dna == revcomp:
            print(i + 1, j - i)