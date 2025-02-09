import itertools

text = "A C G T"
n = 2

alphabet = text.split()
combinations = sorted("".join(l) for l in itertools.product(alphabet, repeat=n))

print("\n".join(combinations))