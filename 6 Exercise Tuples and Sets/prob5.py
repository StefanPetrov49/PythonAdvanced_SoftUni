n = int(input())
f_set = set()
s_set = set()
longest = 0
longest_list = []
for _ in range(n):
    f_seq, s_seq = input().split("-")
    f_start, f_end = f_seq.split(",")
    s_start, s_end = s_seq.split(",")
    for num in range(int(f_start), int(f_end) + 1):
        f_set.add(num)
    for num in range(int(s_start), int(s_end) + 1):
        s_set.add(num)

    numbers = f_set.intersection(s_set)
    if len(numbers) > longest:
        longest_list.clear()
        longest = len(numbers)
        for el in numbers:
             longest_list.append(str(el))

    f_set.clear()
    s_set.clear()
    numbers.clear()
print(f"Longest intersection is [{', '.join(longest_list)}] with length {len(longest_list)}")
