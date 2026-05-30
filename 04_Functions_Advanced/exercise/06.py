def func_executor(*args):
    string = ''
    for el in args:
        name, cur_args = el
        result = name(*cur_args)
        string += f"{name.__name__} - {result}\n"

    return string

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
