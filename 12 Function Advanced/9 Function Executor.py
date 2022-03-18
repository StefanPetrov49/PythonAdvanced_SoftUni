def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

def func_executor(*function_args):
    res = []
    for func, fargs in function_args:
        result = func(*fargs)
        res.append(result)
    return res





print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))