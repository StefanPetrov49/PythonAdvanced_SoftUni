def shopping_list(budget, **kwargs):
    number_of_groceries = 0
    result = ''
    if budget < 100:
        return f"You do not have enough budget."

    for name in kwargs:
        price, quantity = kwargs.get(name)
        price, quantity = float(price), int(quantity)
        total_price = price * quantity
        if number_of_groceries < 5:
            if budget > total_price:
                budget -= total_price
                number_of_groceries +=1
                result += f"You bought {name} for {total_price:.2f} leva.\n"
    return result.strip()




print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print()
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print()
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))


