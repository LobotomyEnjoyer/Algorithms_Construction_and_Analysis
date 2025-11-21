# МНОГОЧЛЕН (ДИОФАНТОВОЕ УРАВНЕНИЕ)
# a + 2b + 3c + 4d = 30

#  ГЕНЕТИЧЕСКИЙ АЛГОРИТМ
# Алгоритм:
# 1) инициализация популяции (случайными значениями в случайном количестве. Гены особи - неизвестные a, b, c, d)
# 2) оценка приспособленности (по формуле. Больше значение - выше приспособленность)
# 3) селекция (метод рулетки или турнирная селекция)
# 4) скрещивания (берётся часть генов от X и Y, передаются потомку Z)
# 5) мутация (небольшие изменения в генах потомка Z)
# 6) формирование нового поколения из потомков. (если потомки не подошли к решению, то продолжаем процесс)

import random


def init_popul(AMOUNT): # создает начальную популяцию
    BOTTOM = 0 # нижняя граница значения гена
    TOP = 100 # верхняя граница значения гена
    N = AMOUNT # количество особей
    popul = []
    for i in range(0, N+1):
        a,b,c,d = random.randint(BOTTOM, TOP), random.randint(BOTTOM, TOP), random.randint(BOTTOM, TOP), random.randint(BOTTOM, TOP)
        popul.append((a, b, c, d))
    return popul.copy()


def fitness_score(specie: tuple) -> float: # вычисляет приспособленность особи
    err = specie[0] + 2*specie[1] + 3*specie[2] + 4*specie[3]
    err = (abs(err - 30) + 1)**(-1) # формула оценки приспособленности
    return err

def tour_selection(population, N): # турнирная селекция 
    parents = [] # из selected выбирается родитель с наилучшим fitness_score (нужно достичь размера популяции N)
    while len(parents) != N:
        max = 0
        winner = ()
        selected = [] # селекция везунчиков (выбрать, на пример, 10-15 везунчиков)

        while len(selected) <= (int(0.5*N) if N >= 20 else int(N/2)):
            if decision():
                X = population[random.randint(0, N-1)]
                selected.append(X)
        
        for specie in selected:
            if max < fitness_score(specie):
                max = fitness_score(specie)
                winner = specie
        
        parents.append(winner)
    
    return parents.copy()


def mutation(Z):
    for i in range(len(Z)):
        Z[i] += random.randint(-5, 5)
    for i in range(len(Z)):
        if Z[i] < 0:
            Z[i] *= -1
        if Z[i] >= 31:
            Z[i] %= 31



def crossingover(parents, N):
    new_gen = []
    while len(new_gen) <= N:
        for _ in parents:
            X = parents[random.randint(0, N-1)]
            Y = parents[random.randint(0, N-1)]
            Z = [X[0], X[1], Y[2], Y[3]]
            mutation(Z)
            new_gen.append(tuple(Z))

    return new_gen.copy()
        

def decision():
    return random.random() < 0.50



CYCLES = abs(int(input("Введите количество поколений (целое число): ")))
NUMBER_OF_SPECIES = abs(int(input("Введите количество особей (целое число): "))) 

population = init_popul(NUMBER_OF_SPECIES)
answers = []

for i in range(1, CYCLES+1):
    print(f"Поколение {i}")
    population = crossingover(tour_selection(population, NUMBER_OF_SPECIES), NUMBER_OF_SPECIES)
    for specie in population:
        if fitness_score(specie) == 1 and (specie not in answers):
            answers.append(specie)
            formula = specie[0] + 2*specie[1] + 3*specie[2] + 4*specie[3]
            print(specie, fitness_score(specie), formula, i)

print(f"Всего ответов: {len(answers)}")

