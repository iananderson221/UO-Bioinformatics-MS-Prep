def hamming_distance(s, t):
	#Ensure both sequences are of equal length
	if len(s) != len(t):
		print("Strings are not equal size!")
		return None  #Return None to show an invalid comparison

	#Initialize a counter for nucleotide differences
	nt_difference = 0

	#Loop through the sequences and compare corresponding nucleotides
	for nt in range(len(s)):
		if s[nt] != t[nt]:  #If nucleotides at the same position differ
			nt_difference += 1  #Increase the difference count

	return nt_difference  #Return the total number of differences


#Example DNA sequences
s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"


result = hamming_distance(s, t)
print(result)

