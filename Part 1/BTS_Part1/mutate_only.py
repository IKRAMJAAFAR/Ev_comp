import random
import string

# Target string
target = "HelloWorld!!"
target_length = len(target)
characters = string.ascii_letters + string.punctuation # Possible character set

def _main_():
    return 0

def calculate_fitness(individual, target):
    matches = sum(1 for i in range(len(target)) if individual[i] == target[i])
    return matches / len(target)  # Normalized fitness between 0 and 1

def generate_individual(length):
    return ''.join(random.choice(characters) for _ in range(length))

def generate_population(size, length):
    return [generate_individual(length) for _ in range(size)]

def mutate(individual, mutation_rate):
    mutated = ''.join(
        (char if random.random() > mutation_rate else random.choice(characters))
        for char in individual
    )
    return mutated

def genetic_algorithm(target, mutation_rate):
    population = generate_population(population_size, len(target))
    generation = 1
    while(True):
        # Calculate fitness for each individual
        fitness_scores = [calculate_fitness(ind, target) for ind in population]

        # Check if we found the target
        if max(fitness_scores) == 1.0:
            print(f"Target string found in generation {generation}")
            break

        # Generate the next generation
        next_generation = []
        for _ in range(population_size):
            parent1, parent2 = select_parents(population, fitness_scores)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            next_generation.append(child)

        population = next_generation
        best_individual = population[fitness_scores.index(max(fitness_scores))]
        print(f"Generation {generation}: {best_individual}, Fitness: {max(fitness_scores)}")
        generation += 1

    return best_individual