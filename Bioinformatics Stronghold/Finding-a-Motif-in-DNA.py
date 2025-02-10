#Define the main DNA sequence (s) and the substring to search for (t)
s = "GATATATGCATATACTT"
t = "ATAT"

#Loop through each nucleotide position in s
for nt in range(len(s)):
    #Check if the substring starting at the current position matches t
    if s[nt:].startswith(t):
        #Print the position (1-based index)
        print(nt + 1)
