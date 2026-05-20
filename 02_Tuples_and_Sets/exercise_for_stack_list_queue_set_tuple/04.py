from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(x for x in input().split())
total = 0

function = {
    "+": lambda i: lambda a, b: a + b,
    "-": lambda i: lambda a, b: a - b,
    "*": lambda i: lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0
}

while bees in nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.popleft()
    if current_nectar >= current_bee:
        current_symbol = symbols.popleft()
        total += abs(function[current_symbol](current_bee, current_nectar))
    else:
        bees.append(current_bee)

print(f"Total honey made: {total}")
if bees:
    print_str = ', '.join(str(x) for x in bees)
    print(f"Bees left: {print_str}")
if nectar:
    print_str = ', '.join(str(x) for x in nectar)
    print(f"Nectar left: {print_str}")