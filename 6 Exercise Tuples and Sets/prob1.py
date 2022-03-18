n = int(input())
my_set = set()

for _ in range(n):
    command = input()
    my_set.add(command)
print("\n".join(my_set))
