import math

def mendel_probability(k, N):
    total_organisms = 2 ** k
    prob_Aa_Bb = 0.25

    prob_less_than_N = sum(
        math.comb(total_organisms, i) * (prob_Aa_Bb ** i) * ((1 - prob_Aa_Bb) ** (total_organisms - i))
        for i in range(N)
    )

    return round(1 - prob_less_than_N, 3)

k, N = 2, 1
print(mendel_probability(k, N))


