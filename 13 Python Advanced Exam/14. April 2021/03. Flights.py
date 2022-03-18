def flights(*args):
    destinations = {}

    for index in range(0, len(args)+1, 2):
        key = args[index]
        if key != 'Finish':
            if key not in destinations:
                destinations[key] = 0
            destinations[key] += args[index + 1]
        else:
            break
    return destinations

result = flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15)
print(result)
