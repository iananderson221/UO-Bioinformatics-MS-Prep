import itertools

n = 5
perm = list(itertools.permutations(range(1, n+1)))
with open("rosalind_perm.txt", "w") as file:
    file.write(f"{len(perm)}\n")
    for num in perm:
        file.write(" ".join(map(str, num)) + "\n")
