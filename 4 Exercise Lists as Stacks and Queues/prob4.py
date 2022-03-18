clothes_value = input().split()
capacity_rack = int(input())
rack_counter = 0
cloth_value = 0
for i in range(len(clothes_value)):
    current_cloth = int(clothes_value.pop())
    cloth_value += current_cloth

    if cloth_value < capacity_rack:
        continue
    elif cloth_value <= capacity_rack:
        cloth_value = 0
        rack_counter += 1
    else:
        cloth_value = current_cloth
        rack_counter += 1

if cloth_value > 0:
    rack_counter += 1
print(rack_counter)


