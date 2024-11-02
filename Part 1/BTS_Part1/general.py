import random
import string
import enchant  # This library provides a dictionary check
import re

# Initialize the dictionary (English)
dictionary = enchant.Dict("en_US")

target = "G7$pQz!9sW@tL4"
target_length = len(target)
characters = string.ascii_letters + string.punctuation # Possible character set

def requirement(password):
    ps_lower = password.lower()

    return len(password) >= 12 and not dictionary.check(ps_lower)

def specgene_fitness(individual, target):
    return 0

def monkey_fitness(individual, target):
    matches = sum(1 for i in range(len(target)) if individual[i] == target[i])
    return matches / len(target)  # Normalized fitness between 0 and 1




def generate_individual(length):
    return ''.join(random.choice(characters) for _ in range(length))

def generate_population(size, length):
    return [generate_individual(length) for _ in range(size)]

def select_parents(population, fitness_scores):
    # Select parents using a weighted random choice based on fitness scores
    weights = [fitness for fitness in fitness_scores]
    parent1 = random.choices(population, weights=weights, k=1)[0]
    parent2 = random.choices(population, weights=weights, k=1)[0]
    return parent1, parent2

def mutate(individual, mutation_rate):
    mutated = ''.join(
        (char if random.random() > mutation_rate else random.choice(characters))
        for char in individual
    )
    return mutated
