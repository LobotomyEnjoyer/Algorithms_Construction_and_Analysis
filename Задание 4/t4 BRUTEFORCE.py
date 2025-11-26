# ШАХМАТЫ-1 
# Расставить ферзи так, чтобы они не били друг друга.
# Рассчитать именно для N ферзей и (N x N) доски. Т.е. если ферзей 8, то доска (8 х 8)

# Алгоритм называется backtracking (рекурсия):
# Основная идея заключается в том, что мы размещаем по одному ферзю в каждом ряду, начиная с первого, и проверяем, не атакует ли новый ферзь уже установленных. 
# Если позиция безопасна, переходим к следующему ряду. 
# Если нет, или если мы дошли до конца, но не смогли разместить всех ферзей, мы "возвращаемся" на предыдущий шаг и меняем позицию последнего успешно размещенного ферзя. 

# Ставим 0-го ферзя на 0 строку и 0 колонку
# вызываем решатель для 1 ферзя
# если безопасное место
#     ставим ферзя
#     вызываем решатель для следующего ферзя
#     ...
#     если строка == N, то ответ найден (сохраняем его)
#         убираем N-1 ферзя
#         ищем безопасное место для N-1 ферзя, начиная с последнего безопасного места
#         если место найдено
#             ставим ферзя
#             вызываем решатель для N ферзя (т.е. для строки == N)
#         иначе если место не найдено
#             убираем N-2 ферзя
#             ищем безопасное место для N-1 ферзя, начиная с последнего безопасного места
#             ...
# иначе если последняя колонка
#     переходим к предыдущему ферзю
#     убираем его с поля и проверяем с последнего места
#     если место безопасно
#         ставим ферзя
#         вызываем решатель для следующего ферзя
#     если последняя колонка
#         переходим к предыдущему ферзю
#         ...
# если дошли до 0-й строки (0-го ферзя)
# если не последняя колонка:
#     двигаем 0-го ферзя на шаг вперёд
#     вызываем решатель для 1-го ферзя
#     ...
# иначе
#     вывод результатов

# ИЗВЕСТНЫЕ ПРОБЛЕМЫ
# solve() рекурсивно бесконечно углубляется

import sys
sys.setrecursionlimit(1999999999) # для более глубоких рекурсий (НЕ ТРОГАТЬ)


global N # Размер поля и кол-во ферзей
N = int(input("Введите число ферзей: "))

board = [-1] * N # Игровое поле

solutions = [] # Найденные решения

counter = 0
def count(): # счетчик
    global counter 
    counter += 1

def is_safe(row, col, board): # проверяет на безопасноть клетки
    for i in range(0, N):
        
        if(board[i] == col) or ((abs(row - i) == abs(col - board[i])) and board[i] != -1):
            return False
    
    return True


def rollback(row, board): # откатывается к N-1 ферзю, если не удалось разместить N-го ферзя
    if board[0] == N-1 and row == 0:
        END()

    start_col = board[row] + 1
    board[row] = -1

    if start_col < N-1:

        for col in range(start_col, N):
            if is_safe(row, col, board):
                board[row] = col
                return row + 1
            elif col == N-1:
                return rollback(row - 1, board)
            
    elif start_col == N-1:

        if is_safe(row, start_col, board):
            board[row] = start_col
            return row + 1
        else:
            return rollback(row - 1, board)
        
    else:

        return rollback(row - 1, board)



def solve(row, board): # ищет всевозможные решения (рекурсия)
    if row == N:
        if board not in solutions:
            solutions.append(board.copy())
            count()
        solve(rollback(row - 1, board), board)
    
    else:

        for col in range(N):
            if is_safe(row, col, board):
                board[row] = col
                solve(row + 1, board)
            
            elif col == N-1:
                Row = rollback(row - 1, board)
                if Row >= 0 and Row <= N-1:
                    solve(Row, board)


def END(): # завершает программу после нахождения всех ответов
    print(f"Всего решений: {counter}")
    if input("Хотите вывести результаты в виде досок?\nY - да\nN - нет\n").lower() == 'y':
        display()
    sys.exit(0)



def display(): # отрисовывает поле с ферзями
    for sol in solutions:
        txt = ""
        for row in range(N):
            for cell in range(N):
                if cell == sol[row]:
                    txt += "♕ "
                else:
                    txt += "▯ "
            txt += '\n'
        print(txt)


solve(0, board) # Запускает алгоритм поиска расстановки
