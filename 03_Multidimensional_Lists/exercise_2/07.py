def start(matrix: list, length):
    row_idx = 0
    col_idx = 0
    for i in range(length):
        for j in range(length):
           if matrix[i][j] == 'S':
               row_idx, col_idx = i, j

    return row_idx, col_idx


def nice_kids(matrix, length):
    counter = 0
    for i in range(length):
        for j in range(length):
            if matrix[i][j] == 'V':
                counter += 1
    return counter


directions = {
    'left': [0, -1],
    'right': [0, +1],
    'up': [-1, 0],
    'down': [+1, 0],
}


def santa_move(matrix, action, row, col, presents, kids, kids_presents):
    matrix[row][col] = '-'
    row += directions[action][0]
    col += directions[action][1]

    if matrix[row][col] == 'V':
        kids -= 1
        presents -= 1
        kids_presents += 1
        matrix[row][col] = 'S'
    elif matrix[row][col] == 'X':
        matrix[row][col] = 'S'
    elif matrix[row][col] == 'C':
        matrix[row][col] = 'S'
        for key in directions.keys():
            current_r = row + directions[key][0]
            current_c = col + directions[key][1]

            if matrix[current_r][current_c] == 'X':
                matrix[current_r][current_c] = '-'
                presents -= 1
            elif matrix[current_r][current_c] == 'V':
                matrix[current_r][current_c] = '-'
                presents -= 1
                kids -= 1
                kids_presents += 1

            if presents == 0:
                break

    return matrix, row, col, presents, kids, kids_presents

num_presents = int(input())
size = int(input())
town = [[el for el in input().split()] for _ in range(size)]

santa_row, santa_col = start(town, size)
num_nice_kids = nice_kids(town, size)
nice_kids_with_presents = 0

while num_presents > 0 :
    com = input()
    if com == 'Christmas morning':
        break
    town, santa_row, santa_col, num_presents, num_nice_kids, nice_kids_with_presents = \
        santa_move(town, com, santa_row, santa_col, num_presents, num_nice_kids, nice_kids_with_presents)
    if num_presents == 0 and num_nice_kids > 0:
        print("Santa ran out of presents!")
        break

[print(*row) for row in town]
if num_nice_kids == 0:
    print(f"Good job, Santa! {nice_kids_with_presents} happy nice kid/s.")
else:
    print(f"No presents for {num_nice_kids} nice kid/s.")
