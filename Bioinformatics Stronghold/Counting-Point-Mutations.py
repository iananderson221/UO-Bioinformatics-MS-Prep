def hamming_distance(s, t):
    if len(s) != len(t):
	    print("Strings are not equal size!")
    else:
    	nt_difference = 0
    	for nt in range(len(s)):
       	    if s[nt] != t[nt]:
            	nt_difference += 1
    	return nt_difference

s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

result = hamming_distance(s, t)

print(result)
