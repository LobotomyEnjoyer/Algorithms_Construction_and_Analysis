# ЗАДАЧА КОММИВОЯЖЁРА
# ЗАДАЧА: из пункта А по вершинам вернуться в пункт А за МИНИМАЛЬНОЕ число шагов и найти самый короткий путь.

# МУРАВЬИНЫЙ АЛГОРИТМ
# 0) задается кол-во циклов C, кол-во городов N, кол-во муравьев A, гиперпараметры: a, b, p. a и b - степени в формуле, p - интенсивность испарения феромона за цикл в промежутке [0,1]. Гиперпараметры указаны в функциях.
# 1) инициализация феромонов для всех путей (это отдельная матрица + значения одинаковые и небольшие)
# 2) определенное количество виртуальных муравьев случайным образом размещается в разных городах
# 3) каждый муравей строит свой маршрут и возвращается в исходный пункт (ведётся список табу, чтобы вершины не повторялись. Выбор муравья происходит по формуле!!!)
# 4) обновление феромонов, глобальное и локальное (локальное - муравей откладывает немного феромона после прохождения. Если путь оказался короче, то прибавляем побольше феромона. Глобальное - немного феромона испаряется на всех маршрутах)
# 5) из всех построенных маршрутов ищется минимальный
# 6) запоминается кратчайший путь
# 7) обход происходит C раз.


# алгоритм передвижения муравья:
# для муравья в начальном пункте вызывается функция пути
# в функции инициализируется список табу (пройденные вершины, начальная вершина сразу туда попадает. Либо сам муравей является списком табу и путём?)
# вызывается функция выбора перехода из i в j (j выбирается случайно)
# если выбор и j не в табу:
# j попадает в список табу (i уже в списке)
# в муравье перезаписывается вершина на j
# иначе если j в табу:
#     продолжается перебор вершин
# если последняя доступная вершина:
#   она записывается в путь
#   начальная вершина записывается в путь
# возвращается построенный путь муравья

# кодирование городов:
# A - 0
# B - 1
# C - 2
# D - 3
# ...

import random as rnd


# инициализация матрицы феромонов
def init_pm(size): 
    pheromone = 0.1 # начальное количество феромона
    pm = [[pheromone for _ in range(size)] for _ in range(size)] # матрица феромонов
    return pm

# обновляет феромоны в матрице
# pm - матрица феромонов
# paths - пройденные пути
def update_pm(pm: list, paths: list):
    p = 0.2  #гиперпараметр, коэффициент испарения феромона
    q = 0.3 #интенсивность феромона
    for path in paths:
        for k in range(NUMBER_OF_CITIES):
            i = path[k]
            j = path[k+1]
            pm[i][j] = (1 - p)*pm[i][j] + (q/PATH_MATRIX[i][j])

# генерирует начальную матрицу пути
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

# функция выбора
# принимает муравья как taboo и потенциальную вершину
# i - вершина, в которой находится муравей
# j - следующая вершина
def decision(taboo: list, i: int, j: int) -> bool:
    # a и b - гиперпараметры
    a = 2
    b = 2
    indexes = [i for i in range(NUMBER_OF_CITIES)]
    denom = 0
    for k in indexes:
        if k not in taboo:
            denom += (PHEROMON_MATRIX[i][k] ** a) * ((1/PATH_MATRIX[i][k]) ** b)
    numer = (PHEROMON_MATRIX[i][j] ** a) * ((1/PATH_MATRIX[i][j]) ** b)

    attraction = numer/denom

    return rnd.random() < attraction


# строит путь одного муравья
# МУРАВЕЙ ХРАНИТ ВЕРШИНУ, В КОТОРОЙ ОН СТОИТ
def construct_ant_path(ant: int) -> list:
    taboo = [ant]
    path = [ant]

    while len(path) != NUMBER_OF_CITIES:
        j = rnd.randint(0, NUMBER_OF_CITIES-1)
        if j not in taboo:
            if decision(taboo, ant, j):
                taboo.append(j)
                path.append(j)
                ant = j
    
    path.append(taboo[0])

    return path.copy()


# инициализирует колонию, которая затем строит пути. Начальные вершины РАЗНЫЕ
def init_colony() -> list:
    colony = [rnd.randint(0, NUMBER_OF_CITIES-1) for _ in range(NUMBER_OF_ANTS)]
    ant_paths = []
    for ant in colony:
        path = construct_ant_path(ant)
        ant_paths.append(path.copy())
    
    for path in ant_paths:
        print(path)
    
    return ant_paths

# такой же алгоритм, но фиксированная начальная вершина А - 0
def optimized_init_colony() -> list:
    ant_paths = []
    ant = 0
    for _ in range(NUMBER_OF_ANTS):
        path = construct_ant_path(ant)
        ant_paths.append(path.copy())
    
    return ant_paths.copy()


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





# ГЛАВНАЯ ЧАСТЬ ПРОГРАММЫ

print("\nВНИМАНИЕ!\nВремя выполнения программы сильно увеличивается при большом количестве муравьев и городов!\n")

choice = int(input("Выберите способ генерации матрицы путей:\n" \
"1) Использовать фиксированную матрицу путей 10х10 с известным кратчайшим путём равным 66.\n" \
"2) Генерировать случайную матрицу заданного размера.\n" \
"Выбор по умолчанию: фиксированная матрица 10х10\n"))

match choice:
    case 1:
        PATH_MATRIX =  [[0, 12, 12, 10, 12, 13, 15, 15, 7, 14],
                [12, 0, 12, 7, 15, 7, 8, 5, 8, 5],
                [12, 12, 0, 5, 13, 5, 8, 7, 5, 12],
                [10, 7, 5, 0, 12, 8, 14, 5, 8, 6],
                [12, 15, 13, 12, 0, 14, 10, 6, 9, 11],
                [13, 7, 5, 8, 14, 0, 9, 5, 11, 14],
                [15, 8, 8, 14, 10, 9, 0, 8, 8, 15],
                [15, 5, 7, 5, 6, 5, 8, 0, 13, 9],
                [7, 8, 5, 8, 9, 11, 8, 13, 0, 5],
                [14, 5, 12, 6, 11, 14, 15, 9, 5, 0]] # матрица 10х10 для проверки. Кратчайший путь = 66
        PHEROMON_MATRIX = init_pm(10)
        NUMBER_OF_CITIES = 10
    case 2:
        NUMBER_OF_CITIES = int(input("Введите число городов (целое число): "))
        PATH_MATRIX = matrix_generator(NUMBER_OF_CITIES)
        PHEROMON_MATRIX = init_pm(NUMBER_OF_CITIES)
    
    case _:
        PATH_MATRIX =  [[0, 12, 12, 10, 12, 13, 15, 15, 7, 14],
                [12, 0, 12, 7, 15, 7, 8, 5, 8, 5],
                [12, 12, 0, 5, 13, 5, 8, 7, 5, 12],
                [10, 7, 5, 0, 12, 8, 14, 5, 8, 6],
                [12, 15, 13, 12, 0, 14, 10, 6, 9, 11],
                [13, 7, 5, 8, 14, 0, 9, 5, 11, 14],
                [15, 8, 8, 14, 10, 9, 0, 8, 8, 15],
                [15, 5, 7, 5, 6, 5, 8, 0, 13, 9],
                [7, 8, 5, 8, 9, 11, 8, 13, 0, 5],
                [14, 5, 12, 6, 11, 14, 15, 9, 5, 0]] # матрица 10х10 для проверки. Кратчайший путь = 66
        PHEROMON_MATRIX = init_pm(10)
        NUMBER_OF_CITIES = 10

CYCLES = abs(int(input("Введите количество обходов (целое число): ")))
NUMBER_OF_ANTS = abs(int(input("Введите количество муравьев (целое число): ")))

min = []
for i in range(1, CYCLES+1):
    print(f"Обход под номером {i}")
    paths = optimized_init_colony()
    update_pm(PHEROMON_MATRIX, paths)
    if len(min) == 0:
        min = find_minimal(paths)
    else:
        min2 = find_minimal(paths)
        if get_length(min2) < get_length(min):
            min = min2.copy()
    
print("\nПоиск пути происходит для матрицы путей вида\n")
for row in PATH_MATRIX:
    print(row)
print('\n')

print(f"Кратчайший путь имеет вид {path_to_string(min)} и длина его пути равна {get_length(min)}")