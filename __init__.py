def myai051(board, color):
    """
    6x6オセロ盤で最も奥の石が取れる位置を返す
    color: 1=黒(自分), 2=白(対戦AI)
    """
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    best_move = None
    max_depth = -1

    for row in range(6):
        for col in range(6):
            if board[row][col] != 0:
                continue

            for dr, dc in directions:
                depth = 0
                r, c = row + dr, col + dc
                opponent = 3 - color

                while 0 <= r < 6 and 0 <= c < 6 and board[r][c] == opponent:
                    depth += 1
                    r += dr
                    c += dc

                if depth > 0 and 0 <= r < 6 and 0 <= c < 6 and board[r][c] == color:
                    if depth > max_depth:
                        max_depth = depth
                        best_move = (col, row)

    return best_move
