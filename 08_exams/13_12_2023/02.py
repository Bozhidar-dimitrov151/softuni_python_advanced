def cur_position(position, board, sum_val, jackpot):
    cur_char = board[position[0]][position[1]]

    if cur_char == "J":
        sum_val += 100000
        jackpot = True
    elif cur_char == "W":
        sum_val += 100
    elif cur_char == "P":
        sum_val -= 200

    board[position[0]][position[1]] = "G"

    return sum_val, jackpot

def zero_amount(sum_val):
    return sum_val <= 0

def game_over():
    print("Game over! You lost everything!")

def move_gambler(command, position, board):
    row, col = position
    board[row][col] = '-'
    if command == "up":
        position[0] -= 1
    elif command == "down":
        position[0] += 1
    elif command == "left":
        position[1] -= 1
    elif command == "right":
        position[1] += 1

    return position

def is_out_of_bounds(position, size):
    return position[0] < 0 or position[0] >= size or position[1] < 0 or position[1] >= size


def find_start_position(size, fishing_area):
    for i in range(size):
        for j in range(size):
            if fishing_area[i][j] == 'G':
                return [i, j]
    return None


def fill_board(size):
    board = []
    for _ in range(size):
        board.append(list(input()))
    return board


size = int(input())
board = fill_board(size)
current_position = find_start_position(size, board)
sum_val = 100
jackpot = False

while True:
    if jackpot:
        print("You win the Jackpot!")
        break
    command = input()

    if current_position:
        current_position = move_gambler(command, current_position, board)

    if is_out_of_bounds(current_position, size) or zero_amount(sum_val):
        game_over()
        break
    else:
        sum_val, jackpot = current_position(current_position, board, sum_val, jackpot)

    if command == "end":
        break

if not (is_out_of_bounds(current_position, size) or zero_amount(sum_val)):
    print(f"End of the game. Total amount: {sum_val}$")
    for row in board:
        print(''.join(row))