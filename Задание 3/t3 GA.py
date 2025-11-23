# ЗАДАЧА КОММИВОЯЖЁРА
# ЗАДАЧА: из пункта А по вершинам вернуться в пункт А за МИНИМАЛЬНОЕ число шагов и найти самый короткий путь.

# АЛГОРИТМ ГЕНЕТИЧЕСКОГО АЛГОРИТМА
# 1) Инициализируем популяцию из N особей, гены которых являются городами. Первый и последний ген ВСЕГДА совпадают.
# 2) Селекция (турнирная селекция. Выбираем t особей и среди них выбираем лучшую.)
# 3) Кроссинговер (потомку Z от родитей X и Y случайным образом передаем гены)
# 4) Мутация (меняем местами 2 случайных пункта в генах Z)
# 5) Построение нового поколения из потомков
# 6) Запоминаем кратчайший путь среди потомков
# 7) Повторяем 1-6 до окончания итераций по поколениям и выводим ответ

# кодирование городов:
# A - 0
# B - 1
# C - 2
# D - 3
# ...

import random as rnd

# генерирует особь
def init_specimen():
    # пусть пункт А - 0 является отправным
    specimen = [-1] * (NUMBER_OF_CITIES + 1)
    specimen[0], specimen[NUMBER_OF_CITIES] = 0, 0
    for i in range(1, NUMBER_OF_CITIES):
        while True:
            x = rnd.randint(1, NUMBER_OF_CITIES-1)
            if x not in specimen:
                specimen[i] = x
                break
    return specimen.copy()


# инициализирует популяцию
def init_population(AMOUNT):
    species = []
    for _ in range(AMOUNT):
        species.append(init_specimen())
    return species.copy()

# селекция
def tour_selection(population, N):
    winners = [] # родители

    while len(winners) != N:
        min = 999999999999999
        selected = []
        best = []
        while len(selected) <= int(N/2):
            X = population[rnd.randint(0, N-1)]
            selected.append(X)
        
        for specie in selected:
            if get_length(specie) < min:
                min = get_length(specie)
                best = specie
        
        winners.append(best)
    
    return winners.copy()

def mutation(Z):
    pos1 = rnd.randint(1, NUMBER_OF_CITIES-1)
    pos2 = rnd.randint(1, NUMBER_OF_CITIES-1)

    while pos1 == pos2: # избавляемся от одинаковых индексов, т.е. пока pos1 == pos2, то перегенерируем pos2
        pos2 = rnd.randint(1, NUMBER_OF_CITIES-1)

    tmp = Z[pos1]
    Z[pos1] = Z[pos2]
    Z[pos2] = tmp


def crossingover(parents, N):
    new_gen = []
    while len(new_gen) != N:
        Z = [-1] * (NUMBER_OF_CITIES+1)
        Z[0], Z[NUMBER_OF_CITIES] = 0, 0
        X = parents[rnd.randint(0, N-1)]
        Y = parents[rnd.randint(0, N-1)]
        for i in range(1, NUMBER_OF_CITIES):
            if rnd.random() < 0.5: # True - X; False - Y
                pos = rnd.randint(1, NUMBER_OF_CITIES-1)
                while X[pos] in Z:
                    pos = rnd.randint(1, NUMBER_OF_CITIES-1)
                Z[i] = X[pos]
            else:
                pos = rnd.randint(1, NUMBER_OF_CITIES-1)
                while Y[pos] in Z:
                    pos = rnd.randint(1, NUMBER_OF_CITIES-1)
                Z[i] = Y[pos]  
        mutation(Z)
        new_gen.append(Z)
    return new_gen.copy()


def matrix_generator(size):
# верхняя и нижняя граница для функции генерации случайных целых чисел соответственно.
    TOP = 15
    BOTTOM = 5
    matrix = []
    for start in range(size):
        row = [-1] * size
        for i in range(start, size):
            row[i] = rnd.randint(BOTTOM, TOP)
        matrix.append(row)
    
    for i in range(size):
        matrix[i][i] = 0
    
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == -1:
                matrix[row][col] = matrix[col][row]
    
    return matrix.copy()

# Возвращает длину пути
def get_length(_path) -> int:
    sum = 0
    for i in range(NUMBER_OF_CITIES):
        sum += PATH_MATRIX[_path[i]][_path[i+1]]
    return sum

# конвертирует путь вида [0, 1, 2, 3, 0] в строку вида ABCDA
def path_to_string(path):
    path_string = ""
    ASCII_start_pos = 65
    for P in path:
        path_string += chr(ASCII_start_pos + P)
    return path_string

# среди всех маршрутов ищет кратчайший
def find_minimal(paths) -> list:
    min = 9999999999999999
    good_path = []
    for path in paths:
        if get_length(path) < min:
            min = get_length(path)
            good_path = path
    return good_path


print("\nВНИМАНИЕ!\nВремя выполнения программы сильно увеличивается при большом количестве особей!\n")
NUMBER_OF_CITIES = int(input("Введите число городов (целое число): "))
CYCLES = abs(int(input("Введите количество поколений (целое число): ")))
NUMBER_OF_SPECIES = abs(int(input("Введите количество особей (целое число): ")))
PATH_MATRIX = matrix_generator(NUMBER_OF_CITIES)

# PATH_MATRIX = [[0, 8, 6, 7, 9, 8, 13, 15, 9], # для проверки точности. точный ответ = 60
#                [8, 0, 5, 5, 14, 10, 15, 10, 12],
#                [6, 5, 0, 10, 8, 8, 8, 12, 12],
#                [7, 5, 10, 0, 9, 12, 6, 6, 11],
#                [9, 14, 8, 9, 0, 5, 10, 5, 14],
#                [8, 10, 8, 12, 5, 0, 14, 11, 8],
#                [13, 15, 8, 6, 10, 14, 0, 14, 10],
#                [15, 10, 12, 6, 5, 11, 14, 0, 12],
#                [9, 12, 12, 11, 14, 8, 10, 12, 0]]

print("\nПоиск пути происходит для матрицы путей вида\n")
for row in PATH_MATRIX:
    print(row)
print('\n')

population = init_population(NUMBER_OF_SPECIES)
min = []
for i in range(1, CYCLES+1):
    print(f"Поколение {i}")
    population = crossingover(tour_selection(population, NUMBER_OF_SPECIES), NUMBER_OF_SPECIES)
    if len(min) == 0:
        min = find_minimal(population)
    else:
        min2 = find_minimal(population)
        if get_length(min2) < get_length(min):
            min = min2.copy()

print(f"Кратчайший путь имеет вид {path_to_string(min)} и длина его пути равна {get_length(min)}")

