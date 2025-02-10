def mendel_prob(k, m, n):
    #Calculate the total population size (sum of all genotype counts)
    pop_total = k + m + n  #Total number of organisms
    #Calculate the total number of possible pairings in the population
    total_pop_pairings = float(pop_total * (pop_total - 1))  #Total possible pairings (without replacement)

    #Return the probability that at least one offspring will have the dominant allele
    return (1 - (n * (m + n - 1) / total_pop_pairings + m * (m - 1) / (4 * total_pop_pairings)))



k, m, n = 2, 2, 2

print(mendel_prob(k, m, n))



