def mendel_prob(k, m, n):
    org_total = k + m + n
    org_pairings = float(org_total * (org_total - 1))
    return(1 - (n * (m + n - 1) / org_pairings + m * (m - 1)/(4 * org_pairings)))

k, m, n = 22, 21, 19
print(mendel_prob(k, m, n))