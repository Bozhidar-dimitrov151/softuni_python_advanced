from collections import deque


def in_bounds(r, c):
    return 0 <= r < rows and 0 <= c < cols


def spread_bunnies(matrix):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    bunny_positions = []

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'B':
                bunny_positions.append((r, c))

    for r, c in bunny_positions:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc):
                matrix[nr][nc] = 'B'


rows, cols = map(int, input().split())
field = [list(input().strip()) for _ in range(rows)]
commands = deque(input().strip())

player_r, player_c = None, None

for r in range(rows):
    for c in range(cols):
        if field[r][c] == 'P':
            player_r, player_c = r, c

moves = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

status = ""

while commands:
    cmd = commands.popleft()
    dr, dc = moves[cmd]

    next_r = player_r + dr
    next_c = player_c + dc

    field[player_r][player_c] = '.'

    if not in_bounds(next_r, next_c):
        spread_bunnies(field)
        status = "won"
        break

    if field[next_r][next_c] == 'B':
        player_r, player_c = next_r, next_c
        spread_bunnies(field)
        status = "dead"
        break

    player_r, player_c = next_r, next_c
    field[player_r][player_c] = 'P'

    spread_bunnies(field)

    if field[player_r][player_c] == 'B':
        status = "dead"
        break

for row in field:
    print(''.join(row))

print(f"{status}: {player_r} {player_c}")