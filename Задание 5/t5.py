# ШАХМАТЫ-2
# ЗАДАЧА: Дан черный король, белый король и белая ладья. Необходимо поставить мат черному королю

# АЛГОРИТМ
# Ставятся фигуры
# Запускается цикл по ходам. Если количество ходов закончится, программа завершится.
# Программа сразу проверяет, не является ли данная расстановка матом
# Если это мат, то программа выводит результат и завершается.
# Иначе двигаем белые фигуры к черному королю
# Потом проверяем, поставлен ли мат. Если нет, продолжаем процесс заново до тех пор, пока не закончатся ходы или не будет поставлен мат.

# проверяет, не вышли ли за рамки игрового поля
def is_on_board(pos) -> bool:
    row, col = pos
    return 0 <= row < 8 and 0 <= col < 8


# возвращает все ходы короля (белого или черного)
def all_king_moves(pos) -> list:
    moves = []
    for dif_row in (-1, 0, 1):
        for dif_col in (-1, 0, 1):
            if dif_row == 0 and dif_col == 0:
                continue
            next_row, next_col = pos[0] + dif_row, pos[1] + dif_col
            if is_on_board((next_row, next_col)):
                moves.append((next_row, next_col))
    return moves


# возвращает все ходы ладьи
def all_rook_moves(pos) -> list:
    all_moves = []
    row, col = pos
    for row_i in range(row - 1, -1, -1):
        all_moves.append((row_i, col))
    for row_i in range(row + 1, 8):
        all_moves.append((row_i, col))
    for col_i in range(col - 1, -1, -1):
        all_moves.append((row, col_i))
    for col_i in range(col + 1, 8):
        all_moves.append((row, col_i))
    return all_moves

# возвращает все атакуемые позиции ладьей
def spots_attacked_by_rook(wk,wr,bk) -> list:
    all_attacked_by_rook = []
    row, col = wr
    for row_i in range(row - 1, -1, -1):
        all_attacked_by_rook.append((row_i, col))
        if (row_i, col) == wk or (row_i, col) == bk:
            break
    for row_i in range(row + 1, 8):
        all_attacked_by_rook.append((row_i, col))
        if (row_i, col) == wk or (row_i, col) == bk:
            break
    for col_i in range(col - 1, -1, -1):
        all_attacked_by_rook.append((row, col_i))
        if (row, col_i) == wk or (row, col_i) == bk:
            break
    for col_i in range(col + 1, 8):
        all_attacked_by_rook.append((row, col_i))
        if (row, col_i) == wk or (row, col_i) == bk:
            break
    return all_attacked_by_rook

# возвращает все доступные ходы черного короля
def all_bking_moves(wk,wr,bk) -> list:
    moves = all_king_moves(bk)
    valid_moves = []
    for m in moves:
        if m == wk or m == wr:
            continue
        if m in spots_attacked_by_rook(wk,wr,bk):
            continue
        if is_adjacent(m, wk):
            continue
        valid_moves.append(m)
    return valid_moves

# проверяет, не стоят ли короли рядом
def is_adjacent(pos1, pos2) -> bool:
    return max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1])) == 1

# Проверка на мат
def is_check(bk) -> bool:
    return bk in spots_attacked_by_rook(white_king,white_rook,bk)

def is_checkmate(wk,wr,bk) -> bool:
    if not is_check(bk):
        return False
    return len(all_bking_moves(wk,wr,bk)) == 0

# Функция ходов белых
def whiteMove(wk,wr,bk) -> tuple:
    wk_row, wk_col = wk
    bk_row, bk_col = bk

    # Передвижение черного короля относительно черного
    difference_row = 0 if bk_row == wk_row else (1 if bk_row > wk_row else -1)
    difference_col = 0 if bk_col == wk_col else (1 if bk_col > wk_col else -1)
    new_wk = (wk_row + difference_row, wk_col + difference_col)
    if is_on_board(new_wk) and not is_adjacent(new_wk, bk):
        wk = new_wk

    wr_row, wr_col = wr

    # Двигаем ладью на ту же линию или столбец, что и черный король, без столкновения с белым королём
    if bk_row != wr_row and bk_col != wr_col:
        if bk_row == wk[0]:
            wr = (bk_row, wr_col)
        else:
            wr = (wr_row, bk_col)

    # Если ладья заняла позицию белого короля, немного сдвигаем ладью
    if wr == wk:
        if wr_row < 7:
            wr = (wr_row + 1, wr_col)
        else:
            wr = (wr_row - 1, wr_col)

    # Если ладья не на одном ряду или колонке с чёрным королём, ставим её на соответствующую линию
    if wr_row != bk_row and wr_col != bk_col:
        # Попытаемся поставить на ряд черного короля
        possible_position = (bk_row, wr_col)
        if possible_position != wk and is_on_board(possible_position) and possible_position != bk:
            wr = possible_position
        else:
            # Попытаемся поставить на колонку чёрного короля
            possible_position = (wr_row, bk_col)
            if possible_position != wk and is_on_board(possible_position) and possible_position != bk:
                wr = possible_position
    return wk, wr

# Ход черного короля
def black_move(wk, wr, bk) -> list:
    available_moves = all_bking_moves(wk, wr, bk)

    if not available_moves:
        return None

    # Случайный выбор хода (раскомментировать при необходимости)
    import random
    selectedMove = random.choice(available_moves)
    # print(f'Ход черного короля: {selectedMove}')

    return selectedMove


# Отображает игровое поле с фигурами
def display_positions(wk,wr,bk) -> None:
    print("  " + " ".join(str(i) for i in range(8)))
    board = [["·" if (i+j)%2 == 0 else "·" for j in range(8) ] for i in range(8)]
    wrROW, wrCOL = wr
    wkROW, wkCOL = wk
    bkROW, bkCOL = bk
    board[wkROW][wkCOL] = "♔"
    board[wrROW][wrCOL] = "♖"
    board[bkROW][bkCOL] = "♚"
    for i in range(8):
        print(str(i) + " " + " ".join(board[i]))
    print()



# ОСНОВНАЯ ЧАСТЬ ПРОГРАММЫ

white_king = (3,4) # белый король
white_rook = (3,3) # белая ладья
black_king = (1,1) # черный король

MAX_MOVES = 100

for turn in range(MAX_MOVES):
    print(f"Ход под номером {turn+1}")
    display_positions(white_king,white_rook,black_king)

    if is_checkmate(white_king,white_rook,black_king):
        print("МАТ! Черный король побеждён.\nИгра окончена.")
        break

    white_king, white_rook = whiteMove(white_king,white_rook,black_king)

    if is_checkmate(white_king,white_rook,black_king):
        print("МАТ! Черный король побеждён.\nИгра окончена.")
        display_positions(white_king,white_rook,black_king)
        break

    black_king = black_move(white_king,white_rook,black_king)
else:
    print(f"Не удалось поставить мат черному королю.\nПревышено количество ходов.")

# TODO:
# ВВЕСТИ ПООЧЕРЕДНОСТЬ БЕЛЫХ ФИГУР!!! БЕЛЫЕ ФИГУРЫ ХОДЯТ ОДНОВРЕМЕННО, ТАК НЕЛЬЗЯ!
