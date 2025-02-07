import math

def mendel_probability(k, N):
    total_organisms = 2 ** k
    prob_Aa_Bb = 0.25

    prob_at_least_N = 0
    for i in range(N, total_organisms + 1):
        prob_at_least_N += math.comb(total_organisms, i) * (prob_Aa_Bb ** i) * ((1 - prob_Aa_Bb) ** (total_organisms - i))

    return prob_at_least_N

k, N = 2, 1
print(round(mendel_probability(k, N), 3))

