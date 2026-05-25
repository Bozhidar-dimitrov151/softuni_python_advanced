from collections import deque
def command_game(size, field, amount_coal, col, row):
    while commands:
        current_command = commands.popleft()
        if current_command == 'left':
            col -= 1
            if 0 <= row < size and 0 <= col < size:
                if field[row][col] == 'c':
                    amount_coal -= 1
                    field[row][col] = '*'
                    if amount_coal == 0:
                        print(f"You collected all coal! ({row}, {col})")
                        break
                elif field[row][col] == 'e':
                    print(f"Game over! ({row}, {col})")
                    break
            else:
                col += 1
        elif current_command == 'right':
            col += 1
            if 0 <= row < size and 0 <= col < size:
                if field[row][col] == 'c':
                    amount_coal -= 1
                    field[row][col] = '*'
                    if amount_coal == 0:
                        print(f"You collected all coal! ({row}, {col})")
                        break
                elif field[row][col] == 'e':
                    print(f"Game over! ({row}, {col})")
                    break
            else:
                col -= 1
        elif current_command == 'up':
            row -= 1
            if 0 <= row < size and 0 <= col < size:
                if field[row][col] == 'c':
                    amount_coal -= 1
                    field[row][col] = '*'
                    if amount_coal == 0:
                        print(f"You collected all coal! ({row}, {col})")
                        break
                elif field[row][col] == 'e':
                    print(f"Game over! ({row}, {col})")
                    break
            else:
                row += 1
        elif current_command == 'down':
            row += 1
            if 0 <= row < size and 0 <= col < size:
                if field[row][col] == 'c':
                    amount_coal -= 1
                    field[row][col] = '*'
                    if amount_coal == 0:
                        print(f"You collected all coal! ({row}, {col})")
                        break
                elif field[row][col] == 'e':
                    print(f"Game over! ({row}, {col})")
                    break
            else:
                row -= 1
    else:
        print(f"{amount_coal} pieces of coal left. ({row}, {col})")

size = int(input())
commands = deque(input().split())
field = [input().split() for _ in range(size)]
amount_coal = 0
start_row = 0
start_col = 0

for i in range(size):
    for j in range(size):
        if field[i][j] == 'c':
            amount_coal += 1
        elif field[i][j] == 's':
            start_row = i
            start_col = j

command_game(size, field, amount_coal, start_col, start_row)