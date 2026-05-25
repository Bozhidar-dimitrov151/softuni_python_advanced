def find_bunny_location(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == 'B':
                return r, c


size = int(input())
field = [input().split() for _ in range(size)]

start_row, start_col = find_bunny_location(field)

directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0),
}

best_route = []
best_direction = ''
most_eggs = float('-inf')

for direction, (dr, dc) in directions.items():

    row, col = start_row, start_col
    eggs = 0
    path = []

    while True:
        row += dr
        col += dc

        if not (0 <= row < size and 0 <= col < size):
            break

        if field[row][col] == 'X':
            break

        path.append([row, col])
        eggs += int(field[row][col])

    if path and eggs > most_eggs:
        most_eggs = eggs
        best_direction = direction
        best_route = path

print(best_direction)

for coords in best_route:
    print(coords)

print(most_eggs)