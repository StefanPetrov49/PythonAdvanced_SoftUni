string = input().split()
final = []

for i in range(len(string)):
    final.append(string.pop())

print(" ".join(final))
