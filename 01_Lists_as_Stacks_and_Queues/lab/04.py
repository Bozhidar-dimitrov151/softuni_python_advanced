from collections import deque
queue = deque()
liters = int(input())

while True:
    command = input()
    if command == "Start":
        break
    else:
        queue.append(command)

while True:
    command = input()
    tokens = command.split(" ")
    if tokens[0] == "End":
        print(f"{liters} liters left")
        break
    elif tokens[0] == "refill":
        liters += int(tokens[1])
    else:
        person = queue.popleft()
        if int(tokens[0]) <= liters:
            liters -= int(tokens[0])
            print(f"{person} got water")
        else:
            print(f"{person} must wait")






