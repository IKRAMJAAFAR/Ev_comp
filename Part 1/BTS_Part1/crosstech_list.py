import random

#https://medium.com/geekculture/crossover-operators-in-ga-cffa77cdd0c8

def onepcrossover(parent1, parent2): #One-point crossover
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def twopcrossover(parent1, parent2): #Two-point crossover
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child

def uniformcrossover(parent1, parent2): #Uniform crossover
    child1 = ''
    child2 = ''
    for g1, g2 in parent1, parent2:
        status = random.boolean
        child1 = child1.join(g1 if status else g2)
        child2 = child1.join(g2 if status else g1)
    return child1, child2