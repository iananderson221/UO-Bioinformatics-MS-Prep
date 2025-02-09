def mortal_rabbits(n, m):
    fr = [0] * m
    fr[0] = 1  #Initial pair of rabbits
    for i in range(n - 1):  #Loop n-1 times to compute nth month
        new_born = sum(fr[1:])  #Newborns are sum of mature rabbits
        fr.insert(0, new_born)  #Shift population
        fr.pop()  #Remove the last (oldest) generation

    return sum(fr)  #Total number of rabbits at month n

print(mortal_rabbits(99, 17))

