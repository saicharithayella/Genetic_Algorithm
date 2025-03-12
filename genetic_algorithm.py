import random

# Knapsack Problem Parameters
knapsack_capacity = 50
item_weights = [10, 20, 30, 40, 50]
item_values = [60, 100, 120, 150, 200]
population_size = 50
generations = 100
mutation_rate = 0.1

def generate_chromosome():
    return [random.choice([0, 1]) for _ in range(len(item_weights))]

def initialize_population():
    return [generate_chromosome() for _ in range(population_size)]

def calculate_fitness(chromosome):
    total_value = sum(c * v for c, v in zip(chromosome, item_values))
    total_weight = sum(c * w for c, w in zip(chromosome, item_weights))

    # Penalize solutions that exceed the knapsack capacity
    if total_weight > knapsack_capacity:
        return 0
    else:
        return total_value

def select_parents(population):
    fitness_scores = [calculate_fitness(chromosome) for chromosome in population]
    total_fitness = sum(fitness_scores)
    parents = []

    while len(parents) < population_size:
        selected_index = random.choices(range(len(population)), weights=fitness_scores)[0]
        parents.append(population[selected_index])

    return parents

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(chromosome):
    mutation_point = random.randint(0, len(chromosome) - 1)
    chromosome[mutation_point] = 1 - chromosome[mutation_point]

def apply_mutation(population):
    for chromosome in population:
        if random.random() < mutation_rate:
            mutate(chromosome)

def genetic_algorithm():
    # Initialization
    population = initialize_population()

    for generation in range(generations):
        # Selection
        parents = select_parents(population)

        # Crossover
        offspring = []
        for i in range(0, len(parents), 2):
            if i + 1 < len(parents):
                child1, child2 = crossover(parents[i], parents[i + 1])
                offspring.extend([child1, child2])

        # Mutation
        apply_mutation(offspring)

        # Replace old population with offspring
        population = offspring

    # Return the best solution found
    best_solution = max(population, key=calculate_fitness)
    return best_solution, calculate_fitness(best_solution)

# Run the genetic algorithm
best_solution, best_fitness = genetic_algorithm()

# Display the results
print("Best Solution (Selected items):", best_solution)
print("Best Fitness (Total value):", best_fitness)
