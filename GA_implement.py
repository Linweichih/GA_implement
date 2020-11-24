import random
import math


def calculate_fitness(x1, x2):
    fitness = 21.5 + x1 * math.sin(4 * math.pi * x1) + x2 * math.sin(20 * math.pi * x2)
    return fitness


def select_from_random(cumulative_probabilities, random_pro):
    for index in range(len(cumulative_probabilities)):
        if random_pro < cumulative_probabilities[index]:
            return index


def crossover(pop, p_c):
    pop_size = len(pop)
    for i in range(pop_size - 1):
        if random.random() < p_c:
            cpoint = random.randint(0, len(pop[0]))
            temp1 = []
            temp2 = []
            temp1.extend(pop[i][0:cpoint])
            temp1.extend(pop[i+1][cpoint:len(pop[i])])
            temp2.extend(pop[i+1][0:cpoint])
            temp2.extend(pop[i][cpoint:len(pop[i])])
            pop[i] = temp1
            pop[i+1] = temp2


def mutation(pop, p_m):
    pop_size = len(pop)
    chromo_length = len(pop[0])

    for i in range(pop_size):
        if random.random() < p_m:
            mpoint = random.randint(0, chromo_length - 1)
            if pop[i][mpoint] == 1:
                pop[i][mpoint] = 0
            else:
                pop[i][mpoint] = 1


def chromo_decode(chromosome):
    x1 = 0
    x2 = 0
    x1_order = 0
    x2_order = 0
    # print("chromo = ", chromosome)
    for i in range(24):
        x1_order += pow(2, i) * chromosome[i]
    for i in range(21):
        x2_order += pow(2, i) * chromosome[i+23]
    x1 = -3 + x1_order * 15.1 / (pow(2, 24) - 1)
    x2 = 4.1 + x2_order * 1.7 / (pow(2, 21) - 1)
    # print("x1=", x1, "x2=", x2)
    return x1, x2


def gene_population(pop_size, chromosome_length):
    pop = [[]]
    for i in range(pop_size):
        temp = []
        for j in range(chromosome_length):
            temp.append(random.randint(0, 1))
        pop.append(temp)
    return pop[1:]


def main():
    print("Start GA implement!!")
    pop_size = 20
    # x1 length is 24 ,x2 length is 21
    chromosome_length = 45
    p_c = 0.25
    p_m = 0.01
    # method on Page 23
    population = gene_population(pop_size, chromosome_length)
    print(population)
    fitness_array = []
    fitness_sum = 0
    for index in range(len(population)):
        x1, x2 = chromo_decode(population[index])
        fitness = calculate_fitness(x1, x2)
        # print(fitness)

        # describe on page 26
        fitness_array.append(fitness)
    fitness_sum = sum(fitness_array)
    # describe on page 27
    probibility_select = []
    for index in range(len(fitness_array)):
        probibility = fitness_array[index] / fitness_sum
        probibility_select.append(probibility)
    print("probibility_select:", probibility_select)
    # describe on page 28
    cumulative_probabilities = []
    pdf = 0
    for index in range(len(fitness_array)):
        pdf += probibility_select[index]
        cumulative_probabilities.append(pdf)
    print("cumulative_probabilities:", cumulative_probabilities)
    # Now we are ready to spin the roulette wheel 20 times
    random_sequence = []
    for i in range(20):
        random_sequence.append(random.random())
    # print(random_sequence)

    new_pop = []
    for i in range(len(random_sequence)):
        selected_index = select_from_random(cumulative_probabilities, random_sequence[i])
        print("append chromo ", selected_index)
        new_pop.append(population[selected_index])


if __name__ == '__main__':
    main()
