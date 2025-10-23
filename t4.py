# ШАХМАТЫ-1 
# Расставить ферзи так, чтобы они не били друг друга

# план:
# 1) построить шахматную доску
# 2) разместить n ферзей любым образом
# 3) составить алгоритм для проврки бьёт/не бьёт (проверять от каждого ферзя, либо составить список запрещённых координат)
# 4) если размещение ХОРОШЕЕ, то вывести позиции ферзей (либо же доску с ферзями)

# общий алгоритм
# задать максимальное число ферзей
# выбрать позицию 1-го ферзя (0 0)
# прогонка мест для следующего ферзя
# если ферзи в этом месте не бьют друг друга
#     если не расставлены все ферзи
#         запоминать позицию и прогонять для нового ферзя
#     иначе
#         записать в счётчик/вывести доску
# иначе
#     пропускаем позицию
# после полного перебора вывести количество найденных позиций

# алгоритм проверки для любого количества ферзей (рекурсия)
# параметры: количество оставшихся ферзей, запрещенные позиции, позиции других ферзей
# ввести список ферзей (0 - первый ферзь, 1 - второй ферзь, ..., n - n+1 ферзь)
# ввести список запрещенных позиций
# по циклу прогонять проверку между новым и остальными ферзями

# алгоритм проверки (перебор для случая из 4-х ферзей)
# цикл1 для перебора позиций 1-го ферзя
#     цикл2 для перебора позиций 2-го ферзя
#         если позиция не опасна и не бьет ферзей
#             цикл3 для перебора позиций 3-го ферзя
#                 если позиция не опасна и не бьет ферзей
#                     цикл4 для перебора позиций 4-го ферзя
#                         если позиция не опасна и не бьет ферзей
#                             счетчик++

import numpy as np

# === ЗНАЧЕНИЯ ===
global SIZE
SIZE = 3

global ENEMY 
ENEMY = 9

global COUNT 
COUNT = 0
# === ЗНАЧЕНИЯ ===

def board(): # строит доску (для визуализации, если потребуется)
    solid = '▮'
    hollow = '▯'
    field = []
    for i in range(0, SIZE):
        row = []
        for j in range(0, SIZE):
            if((i+j) % 2 == 0):
                row.append(solid)
            else:
                row.append(hollow)
        field.append(row)
    
    return field.copy()


# алгоритм немного плохой, надо попробовать переписать рекурсией
def algorithm():
    enemy = ENEMY
    counter = 0
    for row in range(0, SIZE):  # ФЕРЗЬ 1
        for col in range(0, SIZE):

            matr = np.zeros((SIZE, SIZE), dtype = int)
            matr[row, col] = enemy
            killer(row, col, matr)
            # print(matr)

            for row1 in range(0, SIZE):     # ФЕРЗЬ 2
                for col1 in range(0, SIZE):

                    matr1 = matr.copy()

                    if matr1[row1, col1] == 0:
                        if checker(row1, col1, matr1):
                            matr1[row1, col1] = enemy
                            killer(row1, col1, matr1)

                            # for row2 in range(0, SIZE):     # ФЕРЗЬ 3
                            #     for col2 in range(0, SIZE):

                            #         matr2 = matr1.copy()


                            #         if matr2[row2, col2] == 0:
                            #             if checker(row2, col2, matr2):
                            #                 matr2[row2, col2] = enemy
                            #                 killer(row2, col2, matr2)

                            #                 print(matr2)

                            #                 counter += 1
                            #                 print(counter)





                                            # for row3 in range(0, SIZE):     # ФЕРЗЬ 4
                                            #     for col3 in range(0, SIZE):

                                            #         matr3 = matr2.copy()

                                            #         if matr3[row3, col3] == 0:
                                            #             if checker(row3, col3, matr3):
                                            #                 matr3[row3, col3] = 2
                                            #                 killer(row3, col3, matr3)

                                            #                 counter += 1
                                            #                 print(counter)



# ФУНКЦИЯ ОБЯЗАТЕЛЬНА
# функция для пометки опасных полей и ферзей. 0 - безопасно; 1 - опасно; 2 - ферзь.
# функция отвратительная, я знаю, но лучшего варианта получше я не придумал.
def killer(i, j, mat):
    enemy = ENEMY
    # стороны
    for up in range(i-1, -1, -1):
        mat[up, j] = 1

    for down in range(i+1, SIZE):
            mat[down, j] = 1

    for left in range(j-1, -1, -1):
            mat[i, left] = 1

    for right in range(j+1, SIZE):
            mat[i, right] = 1
    
    # главная диагональ
    row = i 
    col = j 
    while(row != 0 and col != 0):
        row -= 1
        col -= 1
    
    while(row != SIZE and col != SIZE):
        if mat[row, col] != enemy:
            mat[row, col] = 1
        row += 1
        col += 1
    
    # побочная диагональ
    row = i
    col = j 
    while(row != 0 and col != SIZE-1):
        row -= 1
        col += 1
    
    while(row != SIZE and col != -1):
        if mat[row, col] != enemy:
            mat[row, col] = 1
        row += 1
        col -= 1


# ФУНКЦИЯ ОБЯЗАТЕЛЬНА
# функция для проверки потенциально хорошего места, т.е. 0
# Если на пути проверки попадётся 2, то место плохое и вернёт FALSE
def checker(i, j, mat):
    enemy = ENEMY
    flag = False
    # стороны
    for up in range(i-1, -1, -1):
        if mat[up, j] == enemy:
             return flag

    for down in range(i+1, SIZE):
        if mat[down, j] == enemy:
             return flag

    for left in range(j-1, -1, -1):
        if mat[i, left] == enemy:
             return flag

    for right in range(j+1, SIZE):
        if mat[i, right] == enemy:
            return flag
    
    # главная диагональ
    row = i 
    col = j 
    while(row != 0 and col != 0):
        row -= 1
        col -= 1
    
    while(row != SIZE and col != SIZE):
        if mat[row, col] == enemy:
            return flag
        row += 1
        col += 1
    
    # побочная диагональ
    row = i
    col = j 
    while(row != 0 and col != SIZE-1):
        row -= 1
        col += 1
    
    while(row != SIZE and col != -1):
        if mat[row, col] == enemy:
            return flag
        row += 1
        col -= 1
    
    return not flag




def display(f: list): # выводит поле
    field = f.copy()
    field.reverse()
    for line in field:
        for spot in line:
            print(spot, end="")
        print('\r')


algorithm()