def starting_position(matrix):
    for r in range(5):
        for c in range(5):
            if matrix[r][c] == 'A':
                return r, c


def count_targets(matrix):
    return sum(row.count('x') for row in matrix)


def shooter_move(row, col, matrix, direction, steps):
    new_row = row + directions[direction][0] * steps
    new_col = col + directions[direction][1] * steps

    if (
        0 <= new_row < 5
        and 0 <= new_col < 5
        and matrix[new_row][new_col] == '.'
    ):
        matrix[row][col] = '.'
        matrix[new_row][new_col] = 'A'
        return new_row, new_col

    return row, col


def shoot(row, col, matrix, direction, targets):
    row += directions[direction][0]
    col += directions[direction][1]

    while 0 <= row < 5 and 0 <= col < 5:
        if matrix[row][col] == 'x':
            matrix[row][col] = '.'
            targets_hit.append([row, col])
            return targets - 1

        row += directions[direction][0]
        col += directions[direction][1]

    return targets


shooting_range = [input().split() for _ in range(5)]
commands = int(input())

targets_hit = []

directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0),
}

current_row, current_col = starting_position(shooting_range)
targets = count_targets(shooting_range)

for _ in range(commands):
    if targets == 0:
        break

    command = input().split()

    if command[0] == 'move':
        direction, steps = command[1], int(command[2])
        current_row, current_col = shooter_move(
            current_row,
            current_col,
            shooting_range,
            direction,
            steps
        )

    else:
        targets = shoot(
            current_row,
            current_col,
            shooting_range,
            command[1],
            targets
        )

if targets == 0:
    print(f'Training completed! All {len(targets_hit)} targets hit.')
else:
    print(f'Training not completed! {targets} targets left.')

for target in targets_hit:
    print(target)