from genetic_operation import *
from selection_process import *


def gene_population(pop_size, chromosome_length):
    pop = [[]]
    for i in range(pop_size):
        temp = []
        for j in range(chromosome_length):
            temp.append(random.randint(0, 1))
        pop.append(temp)
    return pop[1:]


def get_best_chromosome_from_pop(population):
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
    best_generation = 0
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
        best_x, best_f = get_best_chromosome_from_pop(population)
        if best_f > best_fitness:
            best_x_pair = best_x
            best_fitness = best_f
            best_generation = generation
    print("[x1,x2]=", best_x_pair, "for fitness value =", best_fitness, f'in Generation {best_generation}')


if __name__ == '__main__':
    main()
