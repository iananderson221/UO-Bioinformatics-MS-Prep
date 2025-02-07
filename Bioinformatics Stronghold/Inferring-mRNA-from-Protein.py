with open('rosalind_mrna.txt', 'r') as file:
    aa = file.read().strip()

aa_dic = {'A': 4, 'R': 6, 'N': 2, 'D': 2, 'C': 2, 'Q': 2, 'E': 2, 'G': 4, 'H': 2, 'I': 3,
          'L': 6, 'K': 2, 'M': 1, 'F': 2, 'P': 4, 'S': 6, 'T': 4, 'W': 1, 'Y': 2, 'V': 4}
stop = 3
for i in aa:
    stop *= aa_dic[i]

print(stop % 1000000)

