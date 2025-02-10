import itertools  #Import the itertools module for generating permutations

def generate_permutations(n, filename="rosalind_perm.txt"):
    #Generate all permutations of numbers from 1 to n
    perm = itertools.permutations(range(1, n+1))

    #Open the output file in write mode
    with open(filename, "w") as file:
        #Convert the permutations to a list so we can count them
        perm_list = list(perm)

        #Write the total number of permutations as the first line in the file
        file.write(f"{len(perm_list)}\n")

        #Write each permutation as a space-separated string on a new line
        file.writelines(" ".join(map(str, p)) + "\n" for p in perm_list)

#Generate permutations for numbers 1 to 3 and save them in "rosalind_perm.txt"
generate_permutations(3)


