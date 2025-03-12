# Genetic_Algorithm
## Solving the Knapsack Problem Using Genetic Algorithm

### Problem Statement
The Knapsack Problem is a well-known optimization problem where the objective is to select a subset of items, each with a given weight and value, to maximize the total value while staying within a given weight constraint. Formally, given a set of items with weights wi and values vi, and a knapsack of capacity W, the goal is to find the subset of items that maximizes the total value without exceeding the knapsack capacity.

### Genetic Algorithm Components

1. *Chromosome Representation*  
   - Each chromosome represents a potential solution and is encoded as a binary string of length N, where N is the number of items.  
   - A 1 at position i indicates that the item is selected, and 0 means it is not.

2. *Initialization*  
   - The initial population of potential solutions (chromosomes) is generated randomly.

3. *Fitness Function*  
   - The fitness score is calculated as the total value of the selected items in the knapsack.  
   - If the total weight exceeds the knapsack capacity, the fitness score is set to 0.

4. *Crossover Policy*  
   - A two-point crossover policy is used.  
   - Two random crossover points are selected on both parent chromosomes, and genetic material between them is exchanged to produce two offspring.

5. *Mutation Operation*  
   - Mutation introduces genetic diversity by randomly selecting a gene in a chromosome and flipping its value (0 becomes 1 and vice versa) with a low probability.

6. *Selection Strategy*  
   - Tournament selection is used to choose parents based on their fitness scores.  
   - Fitter individuals have a higher probability of being selected.

7. *Termination Criteria*  
   - The algorithm terminates after a maximum number of generations or when a certain fitness threshold is reached.

### Python Implementation Overview

*Knapsack Problem Parameters:*  
- knapsack_capacity = 50
- item_weights = [10, 20, 30, 40, 50]
- item_values = [60, 100, 120, 150, 200]
- population_size = 50
- generations = 100
- mutation_rate = 0.1

*Key Functions:*  
- generate_chromosome(): Creates a random binary chromosome.  
- initialize_population(): Generates the initial population.  
- calculate_fitness(chromosome): Calculates the total value of selected items, with penalty for exceeding capacity.  
- select_parents(population): Selects parents based on fitness scores.  
- crossover(parent1, parent2): Performs two-point crossover to create offspring.  
- mutate(chromosome): Flips a random gene with a certain probability.  
- apply_mutation(population): Applies mutation across the population.  
- genetic_algorithm(): Runs the main genetic algorithm loop.

*Output:*  
- Best Solution (Selected items): Binary string representing the best set of items.  
- Best Fitness (Total value): Maximum total value achievable without exceeding capacity.

### Execution
To run the program, execute the genetic_algorithm() function, and the best solution and fitness score will be displayed.


# Evolutionary String Generation using Genetic Algorithm

## Overview
This project implements a Genetic Algorithm (GA) to evolve a population of strings, aiming to match a given target string. It simulates natural selection and evolution, refining the population over multiple generations until the desired target string is reached.

## Problem Description
The goal is to generate a specific target string by evolving a population of candidate strings. Each candidate string consists of characters (genes) from a predefined set. The GA iteratively improves the population until an exact match is found.

## Components of the Genetic Algorithm

### 1. Population
A collection of candidate strings (individuals) that evolve over generations.

### 2. Chromosome Representation
- Each string is a chromosome.
- Each character in the string is a gene.
- Valid genes include uppercase and lowercase letters, digits, and special characters.

### 3. Fitness Function
Quantifies the similarity between a candidate string and the target string. The fitness score is calculated as the number of differing characters between the candidate and target strings.

### 4. Crossover Operation
Combines genetic information from two parent strings to produce offspring. Each gene is selected from one of the parents with a probability:
- 45% chance of taking the gene from parent 1
- 45% chance of taking the gene from parent 2
- 10% chance of mutation

### 5. Mutation Operation
Introduces random small changes in individual strings to maintain diversity. Mutation happens with a low probability of 10% per gene.

## Implementation Details

### Python Modules Used
- random — for random number and gene selection

### Key Constants
- POPULATION_SIZE = 100 — number of individuals per generation
- GENES — valid characters for genes
- TARGET = "Example" — target string to evolve toward

### Classes and Functions
- **Individual Class**:
    - __init__ — initializes an individual with a random chromosome and calculates its fitness
    - mutated_genes — generates a random valid gene for mutation
    - create_gnome — creates a random chromosome
    - mate — performs crossover between two individuals
    - cal_fitness — calculates the fitness score
- *Population Functions*:
    - initialize_population — creates the initial population
    - select_parents — selects two random parents based on fitness
    - crossover — combines parents’ genes to produce offspring
    - mutate_chromosome — applies mutation to a chromosome
    - mutate — mutates an individual
- **main Function**:
    - Drives the evolution process
    - Uses elitism by preserving the top 10% of fittest individuals
    - Generates offspring for the remaining 90% of the population
    - Prints the best individual of each generation until the target string is reached

## Execution Instructions
1. Ensure Python is installed.
2. Save the provided code in a file named string_generation_ga.py.
3. Open a terminal and navigate to the file’s directory.
4. Run the script:
bash
python string_generation_ga.py


## Sample Output
bash
Generation: 1   String: Pzcmqle   Fitness: 5
Generation: 10  String: Example  Fitness: 0


## Conclusion
This project demonstrates the application of Genetic Algorithms in evolving a population of strings to match a target string. By using selection, crossover, and mutation, the algorithm iteratively refines the population and efficiently reaches the optimal solution.
