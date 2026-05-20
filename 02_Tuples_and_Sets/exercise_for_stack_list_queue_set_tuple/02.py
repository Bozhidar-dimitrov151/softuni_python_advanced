from functools import reduce

string_expression = input().split()

function = {
    "+": lambda i:reduce(lambda a, b: a + b, map(int, string_expression[:i])),
    "-": lambda i:reduce(lambda a, b: a - b, map(int, string_expression[:i])),
    "*": lambda i:reduce(lambda a, b: a * b, map(int, string_expression[:i])),
    "/": lambda i:reduce(lambda a, b: a / b, map(int, string_expression[:i]))
}

index = 0

while index < len(string_expression):
    el = string_expression[index]

    if el in "+-*/":
        string_expression[0] = function[el](index)
        [string_expression.pop(1) for _ in range(index)]
        index = 1

    index += 1

print(string_expression[0])