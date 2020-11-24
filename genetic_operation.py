import random


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
            # print("selected_index", selected_index[i+1])
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

