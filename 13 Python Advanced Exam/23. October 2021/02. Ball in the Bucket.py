def check_trow(row, col, matrix):
    summ_col = 0
    if 0 <= row <= 5 and 0 <= col <= 5:
        if matrix[row][col].isdigit():
            return None, matrix
        elif matrix[row][col] == 'B':
            matrix[row][col] = '0'
            for i in range(6):
                if matrix[i][col].isnumeric():
                    summ_col += int(matrix[i][col])
            return summ_col, matrix
    return None, matrix


total_result = 0
matrix = [input().split() for _ in range(6)]
for _ in range(3):
    row, col = input()[1:-1].split(', ')
    row, col = int(row), int(col)
    result, matrix = check_trow(row, col, matrix)
    if result == None:
        pass
    else:
        total_result += result
        matrix[row][col] = '0'

if total_result < 100:
    print(f"Sorry! You need {100 - total_result} points more to win a prize.")
elif 100 <= total_result <= 199:
    print(f"Good job! You scored {total_result} points, and you've won Football.")
elif 200 <= total_result <= 299:
    print(f"Good job! You scored {total_result} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {total_result} points, and you've won Lego Construction Set.")
