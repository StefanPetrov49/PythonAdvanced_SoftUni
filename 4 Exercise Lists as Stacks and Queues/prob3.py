from _collections import deque

quantity_food = int(input())
orders = deque(input().split())
full_list_order = orders
max_value = deque()
for rr in full_list_order:
    max_value.append(int(rr))

biggest_order = max(max_value)


is_complete = True
for i in range(len(orders)):

    order = int(orders.popleft())
    if quantity_food >= order:
        quantity_food -= order

    else:
        orders.appendleft(str(order))
        is_complete = False
        break

print(biggest_order)
if is_complete:
    print("Orders complete")
else:
    print(f"Orders left:", " ".join(orders))

