player_1, player_2 = input().split(', ')
matrix = [input().split() for _ in range(7)]
player_1_score = 501
player_2_score = 501
turn = 0
player_1_turns = 0
player_2_turns = 0
arent_finished = True


def check_trow(row, col, matrix):
    if matrix[row][col].isnumeric():
        return int(matrix[row][col])
    elif matrix[row][col] == 'D':
        return (int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][col]) + int(matrix[6][col])) * 2
    elif matrix[row][col] == 'T':
        return (int(matrix[row][0]) + int(matrix[row][6]) + int(matrix[0][col]) + int(matrix[6][col])) * 3


while arent_finished:
    row, col = input()[1:-1].split(', ')
    row, col = int(row), int(col)

    if turn % 2 == 0:
        player_1_turns += 1
        if 0 <= row <= 6 and 0 <= col <= 6:
            if matrix[row][col] == 'B':
                print(f"{player_1} won the game with {player_1_turns} throws!")
                exit()
            else:
                current_trow = check_trow(row, col, matrix)
                player_1_score -= current_trow
                if player_1_score <= 0:
                    print(f"{player_1} won the game with {player_1_turns} throws!")
                    exit()


    else:
        player_2_turns += 1
        if 0 <= row <= 6 and 0 <= col <= 6:
            if matrix[row][col] == 'B':
                print(f"{player_2} won the game with {player_2_turns} throws!")
                exit()
            else:
                current_trow = check_trow(row, col, matrix)
                player_2_score -= current_trow
                if player_2_score <= 0:
                    print(f"{player_2} won the game with {player_2_turns} throws!")
                    exit()
    turn += 1