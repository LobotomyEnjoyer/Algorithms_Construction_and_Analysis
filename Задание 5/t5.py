import random

# Константы
FIELD_SIZE = 8
LIMIT_OF_STEPS = 100
WHITE_KING = '♔'
BLACK_KING = '♚'
WHITE_ROOK = '♖'
EMPTY = '·'


# Создает пустую доску
def create_board():
    return [[EMPTY for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)]



# Расставляет фигуры на доске
def place_pieces(board, bk_pos, wr_pos, wk_pos):
    # Очищаем доску
    for i in range(FIELD_SIZE):
        for j in range(FIELD_SIZE):
            board[i][j] = EMPTY
    
    # Расставляем фигуры
    bk_x, bk_y = bk_pos
    wr_x, wr_y = wr_pos
    wk_x, wk_y = wk_pos
    
    board[bk_y][bk_x] = BLACK_KING
    board[wr_y][wr_x] = WHITE_ROOK
    board[wk_y][wk_x] = WHITE_KING
    
    return board

# Выводит доску с использованием Unicode символов
def print_board(board):
    print("  " + " ".join(str(i) for i in range(FIELD_SIZE)))
    for y in range(FIELD_SIZE):
        print(f"{y} ", end="")
        for x in range(FIELD_SIZE):
            print(f"{board[y][x]} ", end="")
        print()
    print()

# Проверяет, атакует ли ладья поле
def is_attacked_by_rook(wr_pos, target_pos):
    wr_x, wr_y = wr_pos
    tx, ty = target_pos
    return wr_x == tx or wr_y == ty

# Проверяет, атакует ли король поле
def is_attacked_by_king(wk_pos, target_pos):
    wk_x, wk_y = wk_pos
    tx, ty = target_pos
    return abs(wk_x - tx) <= 1 and abs(wk_y - ty) <= 1

# Проверяет, находится ли черный король под шахом
def is_in_check(bk_pos, wr_pos, wk_pos):
    return (is_attacked_by_rook(wr_pos, bk_pos) or 
            is_attacked_by_king(wk_pos, bk_pos))

# Проверяет, безопасно ли поле для ладьи (не под боем короля)
def is_safe_for_rook(bk_pos, wr_pos):
    bk_x, bk_y = bk_pos
    wr_x, wr_y = wr_pos
    return not (abs(bk_x - wr_x) <= 1 and abs(bk_y - wr_y) <= 1)

# Проверяет, безопасно ли поле для белого короля (короли не могут стоять рядом)
def is_safe_for_king(bk_pos, wk_pos):
    bk_x, bk_y = bk_pos
    wk_x, wk_y = wk_pos
    return not (abs(bk_x - wk_x) <= 1 and abs(bk_y - wk_y) <= 1)



# Возвращает все возможные ходы короля
def get_king_moves(pos):
    x, y = pos
    moves = []
    
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < FIELD_SIZE and 0 <= new_y < FIELD_SIZE:
                moves.append((new_x, new_y))
    
    return moves



# Возвращает все возможные ходы ладьи
def get_rook_moves(pos, bk_pos, wk_pos):
    x, y = pos
    moves = []
    
    # Движение по вертикали вверх
    for new_y in range(y-1, -1, -1):
        if (x, new_y) != bk_pos and (x, new_y) != wk_pos:
            moves.append((x, new_y))
        else:
            break
    
    # Движение по вертикали вниз
    for new_y in range(y+1, FIELD_SIZE):
        if (x, new_y) != bk_pos and (x, new_y) != wk_pos:
            moves.append((x, new_y))
        else:
            break
    
    # Движение по горизонтали влево
    for new_x in range(x-1, -1, -1):
        if (new_x, y) != bk_pos and (new_x, y) != wk_pos:
            moves.append((new_x, y))
        else:
            break
    
    # Движение по горизонтали вправо
    for new_x in range(x+1, FIELD_SIZE):
        if (new_x, y) != bk_pos and (new_x, y) != wk_pos:
            moves.append((new_x, y))
        else:
            break
    
    return moves


# Проверяет, является ли позиция валидной
def is_valid_position(bk_pos, wr_pos, wk_pos):
    
    # Фигуры не могут стоять на одной клетке
    if bk_pos == wr_pos or bk_pos == wk_pos or wr_pos == wk_pos:
        return False
    
    # Белый король не должен быть под шахом
    if is_attacked_by_king(bk_pos, wk_pos):
        return False
    
    # Ладья не должна быть под боем черного короля
    if not is_safe_for_rook(bk_pos, wr_pos):
        return False
    
    # Не должно быть шаха черному королю в начальной позиции
    if is_in_check(bk_pos, wr_pos, wk_pos):
        return False
    
    return True

# Генерирует начальную позицию
def generate_initial_position():
    RANDOM_PLACEMENT = int(input("\nКакую расстановку желаете использовать?\n1 - случайная (мат не гарантирован за отведенное число ходов)\n0 - фиксированная (мат гарантирован)\n"))

    # Если расстановка случайная
    if RANDOM_PLACEMENT:
        while True:
            bk_pos = (random.randint(0, FIELD_SIZE-1), random.randint(0, FIELD_SIZE-1))
            wr_pos = (random.randint(0, FIELD_SIZE-1), random.randint(0, FIELD_SIZE-1))
            wk_pos = (random.randint(0, FIELD_SIZE-1), random.randint(0, FIELD_SIZE-1))
        
            if is_valid_position(bk_pos, wr_pos, wk_pos):
                return bk_pos, wr_pos, wk_pos

    # Если расстановка фиксированная
    else:
        bk_pos = (7,5)
        wr_pos = (4,4)
        wk_pos = (4,3)

        if is_valid_position(bk_pos, wr_pos, wk_pos):
                return bk_pos, wr_pos, wk_pos



# Возвращает все возможные ходы черного короля
def get_black_king_moves(bk_pos, wr_pos, wk_pos):
    moves = []
    
    for new_pos in get_king_moves(bk_pos):
        # Не может встать на клетку с белой фигурой
        if new_pos == wr_pos or new_pos == wk_pos:
            continue
        
        # Не может встать под шах
        if is_in_check(new_pos, wr_pos, wk_pos):
            continue
        
        # Не может встать рядом с белым королем
        if not is_safe_for_king(new_pos, wk_pos):
            continue
        
        moves.append(new_pos)
    
    return moves


# Проверяет, мат ли черному королю
def is_mate(bk_pos, wr_pos, wk_pos):
    # Если король не под шахом, то не мат
    if not is_in_check(bk_pos, wr_pos, wk_pos):
        return False
    
    # Если есть хотя бы один допустимый ход, то не мат
    return len(get_black_king_moves(bk_pos, wr_pos, wk_pos)) == 0



# Проверяет, пат ли
def is_stalemate(bk_pos, wr_pos, wk_pos):
    # Если король под шахом, то не пат
    if is_in_check(bk_pos, wr_pos, wk_pos):
        return False
    
    # Если нет допустимых ходов, то пат
    return len(get_black_king_moves(bk_pos, wr_pos, wk_pos)) == 0



# Находит лучший ход белых (ладьи или короля)
def find_best_white_move(bk_pos, wr_pos, wk_pos):
    best_move = None
    best_score = -float('inf')
    
    # Ходы ладьи
    for new_wr_pos in get_rook_moves(wr_pos, bk_pos, wk_pos):
        if not is_safe_for_rook(bk_pos, new_wr_pos):
            continue
        
        # Оцениваем позицию
        score = evaluate_position(bk_pos, new_wr_pos, wk_pos)
        if score > best_score:
            best_score = score
            best_move = ('R', new_wr_pos)
    
    # Ходы белого короля
    for new_wk_pos in get_king_moves(wk_pos):
        # Не может встать на клетку с другой фигурой
        if new_wk_pos == bk_pos or new_wk_pos == wr_pos:
            continue
        
        # Не может встать рядом с черным королем
        if not is_safe_for_king(bk_pos, new_wk_pos):
            continue
        
        # Оцениваем позицию
        score = evaluate_position(bk_pos, wr_pos, new_wk_pos)
        if score > best_score:
            best_score = score
            best_move = ('K', new_wk_pos)
    
    return best_move


# Оценивает позицию с точки зрения белых
def evaluate_position(bk_pos, wr_pos, wk_pos):
    score = 0
    
    bk_x, bk_y = bk_pos
    wk_x, wk_y = wk_pos
    
    # 1. Шах - это хорошо
    if is_in_check(bk_pos, wr_pos, wk_pos):
        score += 100
    
    # 2. Прижимаем короля к краю
    distance_to_edge = min(bk_x, FIELD_SIZE-1-bk_x, bk_y, FIELD_SIZE-1-bk_y)
    score += (3 - distance_to_edge) * 10  # Чем ближе к краю, тем лучше
    
    # 3. Сближаем королей (но не слишком близко)
    king_distance = max(abs(bk_x - wk_x), abs(bk_y - wk_y))
    if king_distance > 2:  # Идеальное расстояние - 2 клетки
        score -= abs(king_distance - 2) * 5
    else:
        score += (2 - king_distance) * 3
    
    # 4. Ладья должна контролировать короля
    if is_attacked_by_rook(wr_pos, bk_pos):
        score += 20
        # Лучше, если ладья на безопасном расстоянии
        wr_x, wr_y = wr_pos
        rook_distance = max(abs(bk_x - wr_x), abs(bk_y - wr_y))
        if rook_distance >= 2:
            score += 10
    
    # 5. Ограничиваем ходы черного короля
    black_moves = len(get_black_king_moves(bk_pos, wr_pos, wk_pos))
    score += (8 - black_moves) * 5
    
    # 6. Избегаем пата
    if is_stalemate(bk_pos, wr_pos, wk_pos):
        score -= 1000
    
    return score


# Находит лучший ход черного короля
def find_best_black_move(bk_pos, wr_pos, wk_pos):
    moves = get_black_king_moves(bk_pos, wr_pos, wk_pos)
    
    if not moves:
        return None
    
    # Черный король пытается убежать от края
    best_move = None
    best_score = -float('inf')
    
    for new_bk_pos in moves:
        # Оцениваем с точки зрения черных
        score = 0
        new_x, new_y = new_bk_pos
        
        # Двигаемся к центру
        distance_to_center = abs(new_x - FIELD_SIZE//2) + abs(new_y - FIELD_SIZE//2)
        score += (FIELD_SIZE - distance_to_center) * 2
        
        # Избегаем шаха
        if not is_in_check(new_bk_pos, wr_pos, wk_pos):
            score += 50
        
        # Избегаем близости к белому королю
        wk_x, wk_y = wk_pos
        king_distance = max(abs(new_x - wk_x), abs(new_y - wk_y))
        if king_distance > 2:
            score += 10
        
        if score > best_score:
            best_score = score
            best_move = new_bk_pos
    
    return best_move



# Основная стратегия оттеснения короля к краю
def push_to_edge_strategy(bk_pos, wr_pos, wk_pos):
    print("Начинаем стратегию оттеснения черного короля...")
    
    moves_count = 0
    board = create_board()
    
    while moves_count < LIMIT_OF_STEPS:  # Ограничение на количество ходов
        # Ход белых
        white_move = find_best_white_move(bk_pos, wr_pos, wk_pos)
        
        if not white_move:
            print("Белые не могут сделать ход!")
            break
        
        piece_type, new_pos = white_move
        if piece_type == 'R':
            wr_pos = new_pos
            print(f"Ход {moves_count+1}: Ладья → {new_pos}")
        else:
            wk_pos = new_pos
            print(f"Ход {moves_count+1}: Белый король → {new_pos}")
        
        moves_count += 1
        
        # Проверяем мат
        if is_mate(bk_pos, wr_pos, wk_pos):
            board = place_pieces(board, bk_pos, wr_pos, wk_pos)
            print_board(board)
            print(f"МАТ! Всего ходов: {moves_count}")
            return True
        
        # Проверяем пат
        if is_stalemate(bk_pos, wr_pos, wk_pos):
            print("Пат! Игра завершена.")
            return False
        
        # Ход черных
        black_move = find_best_black_move(bk_pos, wr_pos, wk_pos)
        
        if black_move:
            bk_pos = black_move
            print(f"Ход {moves_count+1}: Черный король → {black_move}")
            moves_count += 1
            
            # Проверяем мат после хода черных
            if is_mate(bk_pos, wr_pos, wk_pos):
                board = place_pieces(board, bk_pos, wr_pos, wk_pos)
                print_board(board)
                print(f"МАТ! Всего ходов: {moves_count}")
                return True
        else:
            # У черных нет ходов - проверяем мат или пат
            if is_in_check(bk_pos, wr_pos, wk_pos):
                print("МАТ!")
                return True
            else:
                print("Пат!")
                return False
        
        # Выводим доску
        if moves_count % 5 == 0 or moves_count < 5:  # Выводим чаще в начале и каждые 5 ходов
            board = place_pieces(board, bk_pos, wr_pos, wk_pos)
            print_board(board)
    
    print(f"Достигнут лимит ходов ({moves_count})")
    return False




# Запуск программы
def main():
    print("=== ШАХМАТЫ-2 ===")
    print(f"Размер доски: {FIELD_SIZE}x{FIELD_SIZE}")
    print()
    
    # Генерируем начальную позицию
    print("Генерация начальной позиции...")
    bk_pos, wr_pos, wk_pos = generate_initial_position()
    
    print(f"Начальная позиция:")
    print(f"Черный король: {bk_pos}")
    print(f"Белая ладья: {wr_pos}")
    print(f"Белый король: {wk_pos}")
    print()
    
    # Выводим начальную доску
    board = create_board()
    board = place_pieces(board, bk_pos, wr_pos, wk_pos)
    print("Начальная позиция:")
    print_board(board)
    
    # Проверяем начальную позицию
    if not is_valid_position(bk_pos, wr_pos, wk_pos):
        print("Ошибка: некорректная начальная позиция!")
        return
    
    # Запускаем стратегию
    success = push_to_edge_strategy(bk_pos, wr_pos, wk_pos)
    
    if success:
        print("Мат успешно поставлен!")
    else:
        print("Не удалось поставить мат в пределах лимита ходов.")


main()