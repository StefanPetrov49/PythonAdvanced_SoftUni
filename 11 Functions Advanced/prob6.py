from itertools import permutations

text = input()
result = permutations(text)
for j in list(result):
    print("".join(j))
