from turtledemo.chaos import coosys


def start_position(size, airspace):
    for i in range(size):
        for j in range(size):
            if airspace[i][j] == "J":
                return airspace[i][j]

    return None

def handle_current_position(position, airspace, armour, enemy_planes):
    cur_char = airspace[position[0]][position[1]]

    if cur_char == "E":
        if enemy_planes != 1:
            armour -= 100
        enemy_planes -= 1
    elif cur_char == "R":
        if armour == 300:
            armour = 300

    airspace[position[0]][position[1]] = "J"

    return armour, enemy_planes

def move_plane(command, position, airspace):
    row, col = position

    airspace[row][col] = "-"

    if command == "up":
        position[0] -= 1
    elif command == "down":
        position[0] += 1
    elif command == "left":
        position[1] -= 1
    elif command == "right":
        position[1] += 1

    return position

def final_print(airspace):
    for row in airspace:
        print("".join(row))


def clear_skies():
    armor = 300
    enemy_planes = 4

    size = int(input())
    airspace = [list(input()) for _ in range(size)]

    current_position = start_position(size, airspace)

    while True:
        if armor <= 0:
            assert current_position is not None
            print(
                f"Mission failed, your jetfighter was shot down! Last coordinates [{current_position[0]}, {current_position[1]}]!")
            break

        if enemy_planes == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            break

        command = input()
        assert current_position is not None
        move_plane(command, current_position, airspace)
        armor, enemy_planes = handle_current_position(current_position, airspace, armor, enemy_planes)

    final_print(airspace)

clear_skies()