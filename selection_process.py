import random
import math


def calculate_fitness(x1, x2):
    fitness = 21.5 + x1 * math.sin(4 * math.pi * x1) + x2 * math.sin(20 * math.pi * x2)
    return fitness


def chromo_decode(chromosome):
    x1_order = 0
    x2_order = 0
    # print("chromosome = ", chromosome)
    for i in range(24):
        x1_order += pow(2, i) * chromosome[i]
    for i in range(21):
        x2_order += pow(2, i) * chromosome[i+23]
    x1 = -3 + x1_order * 15.1 / (pow(2, 24) - 1)
    x2 = 4.1 + x2_order * 1.7 / (pow(2, 21) - 1)
    # print("x1=", x1, "x2=", x2)
    return x1, x2


def select_from_random(cumulative_probabilities, random_pro):
    for index in range(len(cumulative_probabilities)):
        if random_pro < cumulative_probabilities[index]:
            return index


def selection_process(population):

    fitness_array = []
    for index in range(len(population)):
        x1, x2 = chromo_decode(population[index])
        fitness = calculate_fitness(x1, x2)
        # print(fitness)
        # describe on page 26
        fitness_array.append(fitness)
    fitness_sum = sum(fitness_array)
    # describe on page 27
    probability_select = []
    for index in range(len(fitness_array)):
        probability = fitness_array[index] / fitness_sum
        probability_select.append(probability)
    # print("probability_select:", probability_select)
    # describe on page 28
    cumulative_probabilities = []
    pdf = 0
    for index in range(len(fitness_array)):
        pdf += probability_select[index]
        cumulative_probabilities.append(pdf)
    # print("cumulative_probabilities:", cumulative_probabilities)

    # Now we are ready to spin the roulette wheel 20 times
    random_sequence = []
    for i in range(20):
        random_sequence.append(random.random())
    # print(random_sequence)
    new_pop = []
    for i in range(len(random_sequence)):
        selected_index = select_from_random(cumulative_probabilities, random_sequence[i])
        # print("append chromosome ", selected_index)
        new_pop.append(population[selected_index])
    return new_pop

