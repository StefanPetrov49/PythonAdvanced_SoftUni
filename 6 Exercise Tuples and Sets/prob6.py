n = int(input())
odd_set = set()
even_set = set()
for i in range(n):
    name = list(input())
    whole_sum_name = sum(ord(c) for c in name)
    index = i + 1
    whole_sum_name = whole_sum_name // index
    if whole_sum_name % 2 == 0:
        even_set.add(whole_sum_name)
    else:
        odd_set.add(whole_sum_name)

if sum(odd_set) == sum(even_set):
    cons = map(str, even_set.union(odd_set))
    print(", ".join(cons))
elif sum(odd_set) > sum(even_set):
    cons = map(str, odd_set.difference(even_set))
    print(", ".join(cons))
else:
    cons = map(str, odd_set.symmetric_difference(even_set))
    print(", ".join(cons))

