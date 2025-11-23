# ЗАДАЧА КОММИВОЯЖЁРА
# ЗАДАЧА: из пункта А по вершинам вернуться в пункт А за МИНИМАЛЬНОЕ число шагов и найти самый короткий путь.

# АЛГОРИТМ МЕТОДА ПЕРЕБОРА
# пара вида (N1, N2) является расстоянием между пунктами N1 и N2 (расстояние между одним и тем же пунктом = 0)
# путь должен начинаться и заканчиваться одним и тем же пунктом
# граф должен быть полным, т.е. из каждого пункта есть маршрут в остальные пункты
# 1) строим квадратную матрицу NxN для N вершин и заполняем её
# 2) путь представляем в виде списка/строки из вершин
# 3) выбираем начальный пункт
# 4) строим всевозможные маршруты (путём перестановок)
# 5) вычисляем длину найденного маршрута и сверяем его с минимальным (если такового нет, то записываем маршрут как минимальный)
# 6) после перебора выводим маршрут и его длину

import random as rnd
import itertools as it

global CITIES
NUMBER_OF_CITIES = int(input("\nВНИМАНИЕ!\nВремя выполнения программы сильно увеличивается при 8 городах и выше!\nВведите число городов (целое число): "))


def matrix_generator(num_of_cities):
# верхняя и нижняя граница для функции генерации случайных целых чисел соответственно.
    TOP = 15
    BOTTOM = 5
    matrix = []
    for start in range(num_of_cities):
        row = [-1] * num_of_cities
        for i in range(start, num_of_cities):
            row[i] = rnd.randint(BOTTOM, TOP)
        matrix.append(row)
    
    for i in range(num_of_cities):
        matrix[i][i] = 0
    
    for row in range(num_of_cities):
        for col in range(num_of_cities):
            if matrix[row][col] == -1:
                matrix[row][col] = matrix[col][row]
    
    return matrix.copy()


# Возвращает длину пути
def get_length(_path):
    sum = 0
    for i in range(NUMBER_OF_CITIES):
        sum += PATH_MATRIX[_path[i]][_path[i+1]]
    return sum

# функция example_path_constructor() строит список путей вида:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# [2, 1, 0, 3, 4, 5, 6, 7, 8, 9, 2]
# [3, 1, 2, 0, 4, 5, 6, 7, 8, 9, 3]
# [4, 1, 2, 3, 0, 5, 6, 7, 8, 9, 4]
# [5, 1, 2, 3, 4, 0, 6, 7, 8, 9, 5]
# [6, 1, 2, 3, 4, 5, 0, 7, 8, 9, 6]
# [7, 1, 2, 3, 4, 5, 6, 0, 8, 9, 7]
# [8, 1, 2, 3, 4, 5, 6, 7, 0, 9, 8]
# [9, 1, 2, 3, 4, 5, 6, 7, 8, 0, 9]
# для функции перестановок. В примере выше маршруты строятся для 10 городов. А - 0, В - 1, С - 2, ...
def example_path_constructor(): 
    example_path = [i for i in range(NUMBER_OF_CITIES)]
    example_path.append(example_path[0])

    paths = []
    paths.append(example_path)

    for P in range(1, NUMBER_OF_CITIES):
        path = example_path.copy()
        path[0], path[NUMBER_OF_CITIES] = P, P
        for i in range(1, NUMBER_OF_CITIES):
            if path[i] == P:
                path[i] = 0
                paths.append(path.copy())
    
    return paths

# строит всевозможные маршруты для всех городов
def path_constructor():
    example_paths = example_path_constructor()
    all_paths = []
    for ex_path in example_paths:
        paths = sorted([e for e in set(it.permutations(ex_path))]) 
        for path in paths:
            all_paths.append(path)

    all_valid_paths = []

    for path in all_paths:
        if path[0] == path[NUMBER_OF_CITIES]:
            all_valid_paths.append(path)
    
    return all_valid_paths.copy()



# строит путь для перестановки только для пункта А под индексом 0
def alternative_example_path_constructor():
    path = [i for i in range(NUMBER_OF_CITIES)]
    path.append(path[0])
    return path.copy()

# строит всевозможные пути для пункта А под индексом 0
def alternative_path_constructor():
    example_paths = alternative_example_path_constructor()
    all_paths = []
    paths = sorted([e for e in set(it.permutations(example_paths))]) 
    for path in paths:
        all_paths.append(path)

    all_valid_paths = []

    for path in all_paths:
        if path[0] == path[NUMBER_OF_CITIES]:
            all_valid_paths.append(path)
    
    return all_valid_paths.copy()


# конвертирует путь вида [0, 1, 2, 3, 0] в строку вида ABCDA
def path_to_string(path):
    path_string = ""
    ASCII_start_pos = 65
    for P in path:
        path_string += chr(ASCII_start_pos + P)
    return path_string

# среди всех маршрутов ищет кратчайший
def find_minimal(paths):
    min = 9999999999999999
    good_path = []
    for path in paths:
        if get_length(path) < min:
            min = get_length(path)
            good_path = path
    return good_path


print("Матрица маршрутов между городами")
PATH_MATRIX = matrix_generator(NUMBER_OF_CITIES)
# PATH_MATRIX = [[0, 8, 6, 7, 9, 8, 13, 15, 9], # для проверки точности. точный ответ = 60, если искать минимальный обход по всем вершинам
#                [8, 0, 5, 5, 14, 10, 15, 10, 12],
#                [6, 5, 0, 10, 8, 8, 8, 12, 12],
#                [7, 5, 10, 0, 9, 12, 6, 6, 11],
#                [9, 14, 8, 9, 0, 5, 10, 5, 14],
#                [8, 10, 8, 12, 5, 0, 14, 11, 8],
#                [13, 15, 8, 6, 10, 14, 0, 14, 10],
#                [15, 10, 12, 6, 5, 11, 14, 0, 12],
#                [9, 12, 12, 11, 14, 8, 10, 12, 0]]
for row in PATH_MATRIX:
    print(row)

print("\nИдёт построение всевозможных путей, ожидайте...\n")
paths = path_constructor()

print("Маршруты построены. Ищем кратчайший путь...\n")
minimal = find_minimal(paths)

print(f"Кратчайший путь имеет вид {path_to_string(minimal)} и его длина равна {get_length(minimal)}")

