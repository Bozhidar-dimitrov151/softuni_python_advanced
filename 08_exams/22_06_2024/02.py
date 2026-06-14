size_field = int(input())

matrix = [list(input()) for _ in range(size_field)]

bee_row = bee_col = 0

for r in range(size_field):
    for c in range(size_field):
        if matrix[r][c] == "B":
            bee_row, bee_col = r, c
            break

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

energy = 15
nectar = 0
restored = False
reached_hive = False

while True:
    command = input()

    matrix[bee_row][bee_col] = "-"

    dr, dc = directions[command]

    bee_row = (bee_row + dr) % size_field
    bee_col = (bee_col + dc) % size_field

    energy -= 1

    current_cell = matrix[bee_row][bee_col]

    if current_cell.isdigit():
        nectar += int(current_cell)
        matrix[bee_row][bee_col] = "-"

    if current_cell == "H":
        reached_hive = True
        matrix[bee_row][bee_col] = "B"
        break

    if energy == 0:
        if nectar >= 30 and not restored:
            energy += nectar - 30
            nectar = 30
            restored = True

            if energy == 0:
                break
        else:
            break

if not reached_hive:
    matrix[bee_row][bee_col] = "B"

if reached_hive:
    if nectar >= 30:
        print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
    else:
        print("Beesy did not manage to collect enough nectar.")
else:
    print("This is the end! Beesy ran out of energy.")

for row in matrix:
    print("".join(row))