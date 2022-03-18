rows, cols = [int(el) for el in input().split()]
matrix = []
for row in range(rows):
    matrix.append([el for el in input().split()])
counter = 0
for i in range(rows-1):
    for j in range(cols-1):
        ff = matrix[i][j]
        fs = matrix[i][j+1]
        sf = matrix[i+1][j]
        ss = matrix[i+1][j+1]
        if ff == fs and fs == sf and sf == ss:
            counter += 1
print(counter)
