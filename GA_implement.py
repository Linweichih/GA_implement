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
    selected_index = []
    for i in range(len(pop)):
        if random.random() < p_c:
            selected_index.append(i)
        else:
            extra_chromo_index = i
    if len(selected_index) % 2 != 0:
        if random.random() < 0.5:
            # remove chromo
            selected_index.remove(selected_index[-1])
        else:
            # add chromo
            if extra_chromo_index is not None:
                selected_index.append(extra_chromo_index)
            else:
                print("every chromosome is selected")
    for i in range(len(selected_index)):
        if i % 2 == 0 and (i+1) < len(selected_index):
            #print("selected_index", selected_index[i+1])
            chromo_1 = pop[selected_index[i]]
            chromo_2 = pop[selected_index[i+1]]
            cpoint = random.randint(1, len(chromo_1)-1)
            temp1 = []
            temp2 = []
            temp1.extend(chromo_1[0:cpoint])
            temp1.extend(chromo_2[cpoint:len(chromo_1)])
            temp2.extend(chromo_2[0:cpoint])
            temp2.extend(chromo_1[cpoint:len(chromo_1)])
            pop[selected_index[i]] = temp1
            pop[selected_index[i + 1]] = temp2
    return pop


def mutation(pop, p_m):
    pop_size = len(pop)
    chromo_length = len(pop[0])

    for i in range(pop_size):
        for j in range(chromo_length):
            if random.random() < p_m:
                if pop[i][j] == 1:
                    pop[i][j] = 0
                else:
                    pop[i][j] = 1
    return pop

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
    #print("probability_select:", probability_select)
    # describe on page 28
    cumulative_probabilities = []
    pdf = 0
    for index in range(len(fitness_array)):
        pdf += probability_select[index]
        cumulative_probabilities.append(pdf)
    #print("cumulative_probabilities:", cumulative_probabilities)

    # Now we are ready to spin the roulette wheel 20 times
    random_sequence = []
    for i in range(20):
        random_sequence.append(random.random())
    # print(random_sequence)
    new_pop = []
    for i in range(len(random_sequence)):
        selected_index = select_from_random(cumulative_probabilities, random_sequence[i])
        # print("append chromo ", selected_index)
        new_pop.append(population[selected_index])
    return new_pop


def get_best_chromosome(population):
    fitness_array = []
    for index in range(len(population)):
        x1, x2 = chromo_decode(population[index])
        fitness = calculate_fitness(x1, x2)
        # print(fitness)
        # describe on page 26
        fitness_array.append(fitness)
    best_f = max(fitness_array)
    # print(population[fitness_array.index(max(fitness_array))])
    x1, x2 = chromo_decode(population[fitness_array.index(max(fitness_array))])
    best_x = [x1, x2]
    return best_x, best_f


def main():
    print("Start GA implement!!")
    pop_size = 20
    # x1 length is 24 ,x2 length is 21
    chromosome_length = 45
    generation_num = 1000
    p_c = 0.25
    p_m = 0.01
    best_fitness = 0
    best_x_pair = []
    # method on Page 23 init the population
    population = gene_population(pop_size, chromosome_length)
    # print(population)
    for generation in range(generation_num):
        select_pop = selection_process(population)
        # the genetic operators
        new_pop_cross = crossover(select_pop, p_c)
        pop_after_cross_mute = mutation(new_pop_cross, p_m)
        population = pop_after_cross_mute
        print("Generation", generation, "generated!!")
        best_x, best_f = get_best_chromosome(population)
        if best_f > best_fitness:
            best_x_pair = best_x
            best_fitness = best_f
            best_generation = generation
    print("[x1,x2]=", best_x_pair, "for fitness value =", best_fitness, f'in Generation {best_generation}')


if __name__ == '__main__':
    main()
