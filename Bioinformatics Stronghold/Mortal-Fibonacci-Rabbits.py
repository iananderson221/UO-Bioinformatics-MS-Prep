def mortal_rabbits(n, m):
    #Create a list 'fr' where each element represents the number of rabbits of each age (up to m months)
    #Initialize the list with zeros, and set fr[0] to 1, as we start with one pair of newborn rabbits.
    fr = [0] * m
    fr[0] = 1

    #Loop for (n - 1) months because we already have the first month
    for i in range(n - 1):
        #Newborn rabbits are the sum of all mature rabbits (from age 1 to m-1 months)
        new_born = sum(fr[1:])  #Sum the rabbits from age 1 to m-1, since rabbits older than 1 month reproduce

        #Shift the population: add the new born rabbits at the front of the list (age 0)
        fr.insert(0, new_born)

        #Remove the last element of the list (representing the oldest rabbits that die after month m)
        fr.pop()

    #Return the total number of rabbits at month n, which is the sum of all ages (0 to m-1 months)
    return sum(fr)

print(mortal_rabbits(99, 17))


