rows = int(input())
matrix = []
temp_list =[]
j = 0
for row in range(rows):
    current_nums = [int(el) for el in input().split(", ")]
    matrix.append([])
    for i in range(len(current_nums)):
        if current_nums[i] % 2 == 0:
            temp_list.append(current_nums[i])
    [matrix[j].append(el) for el in temp_list]
    temp_list = []
    j += 1
print(matrix)

