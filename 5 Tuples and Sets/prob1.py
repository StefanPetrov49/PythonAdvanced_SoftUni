numbers = tuple(map(float, input().split()))
nums_ordered = {}
for num in numbers:
    if num not in nums_ordered:
        nums_ordered[num] = 0
    nums_ordered[num] += 1

[print(f"{key} - {value} times") for key, value in nums_ordered.items()]
