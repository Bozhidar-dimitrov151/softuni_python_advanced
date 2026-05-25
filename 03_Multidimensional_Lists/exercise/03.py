def check_equal_symbols(matrix, r, c):
    symbol_1 = matrix[r][c]
    symbol_2 = matrix[r+1][c]
    symbol_3 = matrix[r][c+1]
    symbol_4 = matrix[r+1][c+1]

    if symbol_1 == symbol_2 == symbol_3 == symbol_4:
        return True
    else:
        return False

rows, cols = input().split(" ")
matrix = []
counter = 0

for row in range(int(rows)):
    matrix.append([str(x) for x in input().split(" ")])

cur_row = 0

while True:
    if cur_row == int(rows) - 1:
        break

    cur_col = 0

    while True:
        if cur_col == int(cols) - 1:
            break

        is_true = check_equal_symbols(matrix, cur_row, cur_col)

        if is_true:
            counter += 1

        cur_col += 1

    cur_row += 1

print(counter)