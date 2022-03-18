n = int(input())
matrix = []
primal_sum = 0
for row in range(n):
    matrix.append([int(el) for el in input().split()])

for i in range(n):
    primal_sum += matrix[i][i]
print(primal_sum)
