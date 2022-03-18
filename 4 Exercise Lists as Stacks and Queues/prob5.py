from _collections import deque

number_petrol_pumps = int(input())
list_pp = deque()
for _ in range(number_petrol_pumps):
    command = input().split()
    list_pp.append([int(command[0]), int(command[1])])

for i in range(number_petrol_pumps):

    tank = 0
    pumps_completed = 0
    for command in list_pp:
        fuel, distance = command[0], command[1]
        tank += fuel
        if tank < distance:
            break
        tank -= distance
        pumps_completed +=1
    if pumps_completed == len(list_pp):
        print(i)
        break


    list_pp.rotate(-1)