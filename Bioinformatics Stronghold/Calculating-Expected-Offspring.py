def expected_offspring(couples):
    #Probability that an offspring will display the dominant phenotype for each type of couple.
    probabilities = [1, 1, 1, 0.75, 0.5, 0]

    #Initialize the total expected offspring with the dominant phenotype
    total_offspring = 0

    #Loop through each couple type and calculate their contribution to the expected count
    for i in range(len(couples)):
        #Multiply the number of couples by the probability of dominant phenotype and by 2 (the number of offspring)
        total_offspring += couples[i] * probabilities[i] * 2

    return total_offspring



couples = [1, 0, 0, 1, 0, 1]

print(expected_offspring(couples))  # Expected output: 3.5


