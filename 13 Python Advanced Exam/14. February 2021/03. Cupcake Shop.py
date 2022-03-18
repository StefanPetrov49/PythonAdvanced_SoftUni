def stock_availability(*args):
    box = args[0]
    command = args[1]

    if command == 'delivery':
        for i in range(2, len(args)):
            box.append(args[i])
    elif command == 'sell':
        if len(args) == 2:
            box.pop(0)
        else:
            third = str(args[2])
            check_third = any(map(str.isdigit, third))
            if check_third:
                if args[2] > len(box):
                    for _ in range(len(box)):
                        box.pop(0)
                else:
                    for _ in range(args[2]):
                        box.pop(0)
            else:
                for i in range(2, len(args)):
                    for _ in range(len(box)):
                        if args[i] in box:
                            box.remove(args[i])
    return box


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate", "banana"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
