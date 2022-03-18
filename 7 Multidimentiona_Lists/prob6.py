n = int(input())
matrix = []
for row in range(n):
    matrix.append([el for el in list(input())])
symbol = input()
position = ()
for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol:
            position = (row, col)
            break

if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")