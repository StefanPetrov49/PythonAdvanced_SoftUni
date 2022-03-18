from pprint import pprint


def check_w(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == "w":
                return i, j


def check_b(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == "b":
                return i, j


def taking_enemy(color, row, col):
    try:
        if chess_board[row - 1][col - 1] in "wb":
            if color == 'w':
                chess_board[row][col] = "-"
                chess_board[row-1][col-1] = "w"
            if color == 'b':
                chess_board[row][col] = "-"
                chess_board[row - 1][col - 1] = "b"
        if chess_board[row - 1][row + 1] in "wb":
            if color == 'w':
                chess_board[row][col] = "-"
                chess_board[row - 1][col + 1] = "w"
            if color == 'b':
                chess_board[row][col] = "-"
                chess_board[row - 1][col + 1] = "b"
        return True
    except Exception:
        return False


def update_board(color, board, row, col):
    if color == "w":
        if row > 0:
            board[row - 1][col] = 'w'
            board[row][col] = '-'
        else:
            print("white wins with queen")
            exit()
    if color == "b":
        if row < 7:
            board[row + 1][col] = 'b'
            board[row][col] = '-'
        else:
            print("black wins with queen")
            exit()


chess_board = [(input().split()) for _ in range(8)]
row_w, col_w = check_w(chess_board)
row_b, col_b = check_b(chess_board)
turn = 1

for _ in range(16):
    if turn % 2 == 0:
        row_b, col_b = check_b(chess_board)
        if taking_enemy('b', row_b, col_b):
            print("black wins taking white")
            exit()
        update_board('b', chess_board, row_b, col_b)
    else:
        row_w, col_w = check_w(chess_board)
        if taking_enemy('w', row_w, col_w):
            print("white wins taking black")
            exit()
        update_board('w', chess_board, row_w, col_w)
    turn += 1
# TODO: white goes up
# TODO: black goes down

pprint(chess_board)