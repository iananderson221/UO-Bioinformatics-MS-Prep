import math  #Import the math module for combinatorial calculations

def mendel_probability(k, N):
    #Compute the total number of organisms in the population (2^k)
    total_organisms = 2 ** k

    #Probability that any single organism has the AaBb genotype
    prob_Aa_Bb = 0.25  #Given in Mendelian inheritance for heterozygous AaBb parents

    #Compute the probability that fewer than N organisms have the AaBb genotype
    prob_less_than_N = sum(
        math.comb(total_organisms, i) * (prob_Aa_Bb ** i) * ((1 - prob_Aa_Bb) ** (total_organisms - i))
        for i in range(N)  #Summing probabilities for 0 to (N-1) organisms having AaBb
    )

    #Subtract from 1 to get the probability of at least N organisms having AaBb
    return round(1 - prob_less_than_N, 3)



k, N = 2, 1
print(mendel_probability(k, N))



