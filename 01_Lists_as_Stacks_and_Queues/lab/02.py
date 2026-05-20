expression = input()

parentheses_stack = []

for i in range(len(expression)):
    if expression[i] == "(":
        parentheses_stack.append(i)

    elif expression[i] == ")":
        start_idx = parentheses_stack.pop()
        end_idx = i + 1
        print(expression[start_idx:end_idx])