def mendel_prob(k, m, n):
    pop_total = k + m + n
    total_pop_pairings = float(pop_total * (pop_total - 1))
    return (1 - (n * (m + n - 1) / total_pop_pairings + m * (m - 1)/(4 * total_pop_pairings)))

k, m, n = 2, 2, 2
print(mendel_prob(k, m, n))


