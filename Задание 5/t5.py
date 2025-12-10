def isInBoard(pos):
    r, c = pos
    return 0 <= r < 8 and 0 <= c < 8

def kingMoves(pos):
    moves = []
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr, nc = pos[0] + dr, pos[1] + dc
            if isInBoard((nr, nc)):
                moves.append((nr, nc))
    return moves

def rookMoves(pos):
    moves = []
    r, c = pos
    for nr in range(r - 1, -1, -1):
        moves.append((nr, c))
    for nr in range(r + 1, 8):
        moves.append((nr, c))
    for nc in range(c - 1, -1, -1):
        moves.append((r, nc))
    for nc in range(c + 1, 8):
        moves.append((r, nc))
    return moves

def squaresAttackedByRook(wk,wr,bk):
    attacked = []
    r, c = wr
    for nr in range(r - 1, -1, -1):
        attacked.append((nr, c))
        if (nr, c) == wk or (nr, c) == bk:
            break
    for nr in range(r + 1, 8):
        attacked.append((nr, c))
        if (nr, c) == wk or (nr, c) == bk:
            break
    for nc in range(c - 1, -1, -1):
        attacked.append((r, nc))
        if (r, nc) == wk or (r, nc) == bk:
            break
    for nc in range(c + 1, 8):
        attacked.append((r, nc))
        if (r, nc) == wk or (r, nc) == bk:
            break
    return attacked

def blackKingMoves(wk,wr,bk):
    moves = kingMoves(bk)
    valid = []
    for m in moves:
        if m == wk or m == wr:
            continue
        if m in squaresAttackedByRook(wk,wr,bk):
            continue
        if isAdjacent(m, wk):
            continue
        valid.append(m)
    return valid

def isAdjacent( pos1, pos2):
    return max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1])) == 1

def isCheck(bk):
    return bk in squaresAttackedByRook(wk,wr,bk)

def isCheckmate(wk,wr,bk):
    if not isCheck(bk):
        return False
    return len(blackKingMoves(wk,wr,bk)) == 0

def whiteMove(wk,wr,bk):
    wk_r, wk_c = wk
    bk_r, bk_c = bk
    dr = 0 if bk_r == wk_r else (1 if bk_r > wk_r else -1)
    dc = 0 if bk_c == wk_c else (1 if bk_c > wk_c else -1)
    new_wk = (wk_r + dr, wk_c + dc)
    if isInBoard(new_wk) and not isAdjacent(new_wk, bk):
        wk = new_wk

    wr_r, wr_c = wr

    # Двигаем ладью на ту же линию или столбец, что и черный король, без столкновения с белым королём
    if bk_r != wr_r and bk_c != wr_c:
        if bk_r == wk[0]:
            wr = (bk_r, wr_c)
        else:
            wr = (wr_r, bk_c)

    # Если ладья заняла позицию белого короля, немного сдвигаем ладью
    if wr == wk:
        if wr_r < 7:
            wr = (wr_r + 1, wr_c)
        else:
            wr = (wr_r - 1, wr_c)

    # Если ладья не на одном ряду или колонке с чёрным королём, ставим её на соответствующую линию
    if wr_r != bk_r and wr_c != bk_c:
        # Попытаемся поставить на ряд черного короля
        candidate = (bk_r, wr_c)
        if candidate != wk and isInBoard(candidate) and candidate != bk:
            wr = candidate
        else:
            # Попытаемся поставить на колонку чёрного короля
            candidate = (wr_r, bk_c)
            if candidate != wk and isInBoard(candidate) and candidate != bk:
                wr = candidate
    return wk, wr

# Ход черного короля
def blackMoveAuto(wk, wr, bk):
    available_moves = blackKingMoves(wk, wr, bk)

    if not available_moves:
        return None

    # Случайный выбор хода (раскомментировать при необходимости)
    import random
    selectedMove = random.choice(available_moves)
    print(f'Ход черного короля: {selectedMove}')

    return selectedMove

def printPositions(wk,wr,bk):
    print("  " + " ".join(str(i) for i in range(8)))
    board = [["·" if (i+j)%2 == 0 else "·" for j in range(8) ] for i in range(8)]
    wrR, wrC = wr
    wkR, wkC = wk
    bkR, bkC = bk
    board[wkR][wkC] = "♔"
    board[wrR][wrC] = "♖"
    board[bkR][bkC] = "♚"
    for i in range(8):
        print(str(i) + " " + " ".join(board[i]))
    # print("\n".join(" ".join(row) for row in board))
    print()

wk = (4,4) # белый король
wr = (4,3) # белая ладья
bk = (1,1) # черный король

MAX_MOVES = 100

for turn in range(MAX_MOVES):
    print(f"Ход {turn+1}")
    printPositions(wk,wr,bk)
    if isCheckmate(wk,wr,bk):
        print("Мат! Белые выиграли.")
        break
    wk, wr = whiteMove(wk,wr,bk)
    if isCheckmate(wk,wr,bk):
        print("Мат! Белые выиграли.")
        printPositions(wk,wr,bk)
        break
    bk = blackMoveAuto(wk,wr,bk)
else:
    print(f"Не удалось поставить мат за {MAX_MOVES} ходов.")
