n = int(input())
student = {}
grades = []
whole_sum = 0
for _ in range(n):
    line = tuple(input().split())
    name, mark = line
    if name not in student:
        student[name] = []
    student[name].append(mark)

for i in student:
    for x in student[i]:
        grades.append(x)
    listToStr = ' '.join([str(elem) for elem in grades])
    for el in grades:
        whole_sum += float(el)
    average = whole_sum / len(grades)
    print(f"{i} -> {listToStr} (avg: {average:.2f})")
    grades = []
    whole_sum = 0
