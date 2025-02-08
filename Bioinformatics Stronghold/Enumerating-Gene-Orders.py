import itertools

def generate_permutations(n, filename="rosalind_perm.txt"):
    perm = itertools.permutations(range(1, n+1))
    with open(filename, "w") as file:
        perm_list = list(perm)  # Convert iterator to a list
        file.write(f"{len(perm_list)}\n")
        file.writelines(" ".join(map(str, p)) + "\n" for p in perm_list)

generate_permutations(3)

