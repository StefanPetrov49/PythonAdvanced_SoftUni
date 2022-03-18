n, m = input().split()

set_n = set()
set_m = set()
for _ in range(int(n)):
    command = input()
    set_n.add(command)
for _ in range(int(m)):
    command = input()
    set_m.add(command)
final_set = set_n.intersection(set_m)
print("\n".join(final_set))
