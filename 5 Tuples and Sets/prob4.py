n = int(input())
parking_lot = set()
for _ in range(n):
    direction, plate = input().split(", ")
    if direction == "IN":
        parking_lot.add(plate)
    else:
        parking_lot.discard(plate)
if parking_lot:
    [print(el) for el in parking_lot]
else:
    print("Parking Lot is Empty")