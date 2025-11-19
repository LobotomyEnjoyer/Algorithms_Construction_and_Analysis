# ЗАДАЧА КОММИВОЯЖЁРА
# ЗАДАЧА: из пункта А по вершинам вернуться в пункт А за МИНИМАЛЬНОЕ число шагов и найти самый короткий путь

# АЛГОРИТМ МЕТОДА ПЕРЕБОРА
# пара вида (N1, N2) является расстоянием между пунктами N1 и N2 (расстояние между одним и тем же пунктом = 0)
# путь должен начинаться и заканчиваться одним и тем же пунктом
# граф должен быть полным, т.е. из каждого пункта есть маршрут в остальные пункты
# 1) строим квадратную матрицу NxN для N вершин и заполняем её
# 2) путь представляем в виде списка/строки из вершин
# 3) выбираем начальный пункт
# 4) строим всевозможные маршруты
# 5) вычисляем длину найденного маршрута и сверяем его с минимальным (если такового нет, то записываем маршрут как минимальный)
# 6) после перебора выводим маршрут и его длину

PATH_MATRIX = [[0, 15, 31, 41], # Матрица расстояний между городами
               [15, 0, 27, 17],
               [31, 27, 0, 11],
               [41, 17, 11, 0]] # A - 0; B - 1; C - 2; D - 3

def get_length(_path):
    sum = 0
    for i in range(4):
        sum += PATH_MATRIX[_path[i]][_path[i+1]]
    return sum

def path_constructor() -> list:
    all_paths = []
    for P1 in range(4):
        _path = []
        _path.append(P1)
        for P2 in range(4):
            if P2 not in _path:
                _path.append(P2)
                for P3 in range(4):
                    if P3 not in _path:
                        _path.append(P3)
                        for P4 in range(4):
                            if P4 not in _path:
                                _path.append(P4)
                                _path.append(P1)
                                all_paths.append(_path.copy())
                                _path.pop(4) # использую метод pop() для устранения пунктов из пути, дабы цикл мог построить новые пути
                                _path.pop(3) 
                        _path.pop(2)
                _path.pop(1)
    return all_paths.copy()


def path_to_string(path):
    path_string = ""
    ASCII_start_pos = 65
    for P in path:
        path_string += chr(ASCII_start_pos + P)
    return path_string

def find_minimal(paths):
    min = 99999
    good_path = []
    for path in paths:
        if get_length(path) < min:
            min = get_length(path)
            good_path = path.copy()
    return good_path

all_paths = path_constructor()
minimal = find_minimal(all_paths)

print(path_to_string(minimal), get_length(minimal), minimal)