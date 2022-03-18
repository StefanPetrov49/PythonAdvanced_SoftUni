import sys
rows, cols = [int(el) for el in input().split(", ")]
matrix = []
position = ()
for row in range(rows):
    matrix.append([int(el) for el in input().split(", ")])
max_sum = -sys.maxsize
for row in range(rows-1, 0, -1):
    for col in range(cols-1, 0, -1):
        current_sum = matrix[row][col] + matrix[row-1][col] \
                + matrix[row][col-1] + matrix[row-1][col-1]
        if current_sum >= max_sum:
            max_sum = current_sum
            position = (row, col)

best_row, best_col = position

print(matrix[best_row-1][best_col-1], matrix[best_row-1][best_col])
print(matrix[best_row][best_col-1], matrix[best_row][best_col])
print(max_sum)
