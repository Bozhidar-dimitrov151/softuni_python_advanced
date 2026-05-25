from collections import deque

size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

coordinates = deque(input().split())

while coordinates:
    cur_bomb = coordinates.popleft()

    cur_row, cur_column = [int(x) for x in cur_bomb.split(",")]

    if matrix[cur_row][cur_column] <= 0:
        continue

    cur_dmg = matrix[cur_row][cur_column]

    for row in range(cur_row - 1, cur_row + 2):
        for col in range(cur_column - 1, cur_column + 2):

            if 0 <= row < size and 0 <= col < size:
                if matrix[row][col] > 0:
                    matrix[row][col] -= cur_dmg

alive_sum = 0
alive = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] > 0:
            alive += 1
            alive_sum += matrix[row][col]

print(f"Alive cells: {alive}")
print(f"Sum: {alive_sum}")

for row in matrix:
    print(*row)