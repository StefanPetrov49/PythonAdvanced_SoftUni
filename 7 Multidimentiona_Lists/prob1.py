rows, cols = [int(el) for el in input().split(", ")]
matrix = []
sum_total = 0
for row in range(rows):
    matrix.append([int(el) for el in input().split(", ")])
    sum_total += sum(matrix[row])
print(sum_total)
print(matrix)