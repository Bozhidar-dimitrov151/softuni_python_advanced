n = int(input())
health = 100
maze = []
row, col = None, None

directions =  {
    "down": (1, 0),
    "up": (-1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

for r in range(n):
    maze.append([chr for chr in input()])
    for c in range(n):
        if maze[r][c] == "P":
            row, col = r, c

while True:
    move = input()

    if not (0 <= row + directions[move][0] < n and 0 <= col + directions[move][1] < n):
        continue

    maze[row][col] = "-"
    row += directions[move][0]
    col += directions[move][1]

    if maze[row][col] == "X":
        print("Player escaped the maze. Danger passed!")
        maze[row][col] = "P"
        break

    elif maze[row][col] == "H":
        health = min(100, health + 15)

    elif maze[row][col] == "M":
        health -= 40

    if health <= 0:
        health = 0
        print("Player is dead. Maze over!")
        maze[row][col] = "P"
        break

    maze[row][col] = "P"

print(f"Player's health: {health} units")
for row in maze:
    print(''.join(row))