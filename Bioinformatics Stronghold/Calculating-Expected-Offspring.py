def expected_offspring(couples):
    probabilities = [1, 1, 1, 0.75, 0.5, 0]
    total_offspring = 0

    for i in range(len(couples)):
        total_offspring += couples[i] * probabilities[i] * 2
    return total_offspring


couples = [1, 0, 0, 1, 0, 1]
print(expected_offspring(couples))


