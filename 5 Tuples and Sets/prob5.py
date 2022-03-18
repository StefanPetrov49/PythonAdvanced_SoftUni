n = int(input())
vip_reservation = set()
reservation = set()
guests = set()

for _ in range(n):
    command = input()
    if command[0].isdigit():
        vip_reservation.add(command)
    else:
        reservation.add(command)

com = input()
while not com == "END":
    if com[0].isdigit():
        vip_reservation.discard(com)
    else:
        reservation.discard(com)
    com = input()

list_vip = list(vip_reservation)
sorted_vip = sorted(vip_reservation)
list_res = list(reservation)
sorted_res = sorted(reservation)

print(len(vip_reservation | reservation))
[print(el) for el in sorted_vip]
[print(el) for el in sorted_res]
