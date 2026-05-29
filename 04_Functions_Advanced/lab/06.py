from functools import reduce


def operate(operators : str, *num):
    result = 0
    if operators == "+":
        result = reduce(lambda x, y: x + y, num)

    elif operators == "-":
        result = reduce(lambda x, y: x - y, num)

    elif operators == "*":
        result = reduce(lambda x, y: x * y, num)

    elif operators == "/":
        result = reduce(lambda x, y: x / y, num)

    return result

print(operate("*", 3, 4))