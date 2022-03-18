sequence = [int(el) for el in input().split()]
positive = []
negative = []
for el in sequence:
    if el >= 0:
        positive.append(el)
    else:
        negative.append(el)
print(sum(negative))
print(sum(positive))
if abs(sum(negative)) > sum(positive):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")