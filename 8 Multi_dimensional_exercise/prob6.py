rows, cols = [int(el) for el in input().split()]
matrix = []
for _ in range(rows):
    matrix.append(input().split())
command = input()

while not command == "END":
    command = command.split()
    if not command[0] == "swap" or not len(command) == 5:
        print("Invalid input!")
    else:
        com = command[0]
        f_row = int(command[1])
        f_col = int(command[2])
        s_row = int(command[3])
        s_col = int(command[4])
        if f_row > rows or f_col > cols or s_row > rows or s_col > cols:
            print("Invalid input!")
        else:
            first_output = matrix[f_row][f_col]
            second_output = matrix[s_row][s_col]

            matrix[f_row][f_col] = second_output
            matrix[s_row][s_col] = first_output
            for line in matrix:
                print(' '.join(map(str, line)))



    command = input()