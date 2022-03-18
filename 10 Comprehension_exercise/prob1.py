text = input().split()
print('\n'.join([el for el in text if len(el) % 2 == 0]))
