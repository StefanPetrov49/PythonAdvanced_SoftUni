from sys import maxsize
rows, cols = [int(el) for el in input().split()]
matrix = []
maximum_sum = -maxsize
current_sum = 0
br, bc = 0, 0
for row in range(rows):
    matrix.append([int(el) for el in input().split()])
for i in range(rows-2):
    for j in range(cols-2):
        current_sum = sum([
            matrix[i][j], matrix[i][j + 1], matrix[i][j + 2],
            matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2],
            matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]])
        if current_sum > maximum_sum:
            maximum_sum = current_sum
            br, bc = i, j

print(f"Sum = {maximum_sum}")
print(matrix[br][bc], matrix[br][bc+1], matrix[br][bc+2])
print(matrix[br+1][bc], matrix[br+1][bc+1], matrix[br+1][bc+2])
print(matrix[br+2][bc], matrix[br+2][bc+1], matrix[br+2][bc+2])


