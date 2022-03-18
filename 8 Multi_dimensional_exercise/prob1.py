n = int(input())
matrix = []
primal_diagonal = []
secondary_diagonal = []
for row in range(n):
    matrix.append([int(el) for el in input().split(", ")])

for row in range(n):
    primal_diagonal.append(matrix[row][row])
    secondary_diagonal.append(matrix[row][n -row -1])

print(f"Primary diagonal: {str(primal_diagonal)[1:-1]}. Sum: {sum(primal_diagonal)}")
print(f"Secondary diagonal: {str(secondary_diagonal)[1:-1]}. Sum: {sum(secondary_diagonal)}")
