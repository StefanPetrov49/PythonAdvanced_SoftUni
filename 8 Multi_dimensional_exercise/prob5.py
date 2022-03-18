from pprint import pprint
rows, cols = [int(el) for el in input().split()]
start = 97
matrix = []
c = 0
for _ in range(rows):
    matrix.append([])
for i in range(rows):
    for j in range(cols):
        matrix[i].append(chr(97+c)+chr(97+j+i)+chr(97+c))
    c += 1

for line in matrix:
    print(' '.join(map(str, line)))

