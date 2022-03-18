command = input()
sequence = [int(el) for el in input().split()]
if command == "Odd":
    print(sum(filter(lambda x: x % 2 != 0, sequence)) * len(sequence))
else:
    print(sum(filter(lambda x: x % 2 == 0, sequence)) * len(sequence))