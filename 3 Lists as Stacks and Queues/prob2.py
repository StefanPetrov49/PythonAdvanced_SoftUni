problem = input()
stack = []

for i in range(len(problem)):
    if problem[i] == "(":
        stack.append(i)
    elif problem[i] == ")":
        start_index = (stack.pop())
        print(problem[start_index: i+1])

