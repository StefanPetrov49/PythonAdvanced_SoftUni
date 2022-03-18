rows = int(input())
matrix = []
for row in range(rows):
    [matrix.append(int(el)) for el in input().split(", ")]
print(matrix)
