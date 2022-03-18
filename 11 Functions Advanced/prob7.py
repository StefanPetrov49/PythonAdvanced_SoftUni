from itertools import combinations
text = input().split(", ")
n = int(input())
result = combinations(text, n)
for x, y in result:
    print(f"{x}, {y}")