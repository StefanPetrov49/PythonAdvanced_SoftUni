from _collections import deque

pizza_orders = deque([int(el) for el in input().split(', ') if 0 < int(el) <= 10])
employees_capacities = [int(el) for el in input().split(', ')]

total_pizzas_made = 0

while pizza_orders and employees_capacities:

    current_pizza_count = pizza_orders.popleft()
    current_employee_capacity = employees_capacities.pop()
    if current_pizza_count > current_employee_capacity:
        current_pizza_count -= current_employee_capacity
        total_pizzas_made += current_employee_capacity
        pizza_orders.appendleft(current_pizza_count)
    elif current_pizza_count <= current_employee_capacity:
        total_pizzas_made += current_pizza_count

if pizza_orders:
    print(f'Not all orders are completed.')
    print(f'Orders left: {", ".join(str(el) for el in pizza_orders)}')
else:
    print(f'All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizzas_made}')
    print(f'Employees: {", ".join(str(el) for el in employees_capacities)}')
