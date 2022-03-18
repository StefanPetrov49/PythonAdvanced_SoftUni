n = int(input())
chemicals = set()
for _ in range(n):
    command = input().split()

    for el in command:
        chemicals.add(el)
print("\n".join(chemicals))