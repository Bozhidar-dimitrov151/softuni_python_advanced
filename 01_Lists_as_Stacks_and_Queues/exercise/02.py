n = int(input())

stack = []

for i in range(n):
    num = input().split()

    if num[0] == "1":
        stack.append(int(num[1]))

    elif num[0] == "2":
        if stack:
            stack.pop()

    elif num[0] == "3":
        if stack:
            print(max(stack))

    elif num[0] == "4":
        if stack:
            print(min(stack))

if stack:
    stack.reverse()
    print(*stack, sep=", ")