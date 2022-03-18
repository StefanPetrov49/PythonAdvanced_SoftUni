from math import floor
def check_player_position(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'P':
                return i, j


def check_wall(i, j, board):
    if board[i][j] == 'X':
        return True
    return False


def check_command(command, i, j, board):
    """

    :type j: int
    """
    if command == 'up':
        if i - 1 < 0:
            #return (i + len(board) - 1), j
            i = len(board) -1
            return i, j

        return (i - 1), j
    elif command == 'down':
        if i + 1 > len(board) - 1:
            #return (i - len(board) - 1), j
            i = 0
            return i, j

        return (i + 1), j
    elif command == 'left':
        if j - 1 < 0:
            #return i, (j + len(board) - 1)
            j = len(board) -1
            return i, j
        return i, (j - 1)
    elif command == 'right':
        if j + 1 > len(board) - 1:
            #return i, (j - len(board) - 1)
            j = 0
            return i, j
        return i, (j + 1)


N = int(input())
matrix = [input().split() for _ in range(N)]
coins_collected = 0
player_not_win = True
player_not_lost = True
rol, col = check_player_position(matrix)
rol, col = int(rol), int(col)
matrix[rol][col] = '0'
coordinates = [[rol, col]]
while player_not_win and player_not_lost:
    my_command = input()
    curr_rol, curr_col = check_command(my_command, rol, col, matrix)
    if check_wall(curr_rol, curr_col, matrix):
        print(f"Game over! You've collected {floor(coins_collected / 2)} coins.")
        player_not_lost = False
    else:
        coins_collected += int(matrix[curr_rol][curr_col])
        matrix[curr_rol][curr_col] = '0'
    if coins_collected >= 100:
        player_not_win = False
    rol = curr_rol
    col = curr_col
    coordinates.append([rol, col])

if not player_not_win:
    print(f"You won! You've collected {coins_collected} coins.")
print('Your path:')
for el in coordinates:
    print(el)
