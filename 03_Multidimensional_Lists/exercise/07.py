rows, cols = (int(x) for x in input().split())
matrix = [["" for _ in range(cols)] for _ in range(rows)]
expression = input()

cells = rows * cols
full_lengths = cells // len(expression)
remainder = cells - full_lengths * len(expression)
total_string = expression * full_lengths + expression[:remainder]
idx = 0
row = 0
column = 0

for _ in range(cells):
    matrix[row][column] = total_string[idx]
    idx += 1
    if row % 2 == 0:
        column += 1
        if column == cols:
            column -= 1
            row += 1
    else:
        column -= 1
        if column < 0:
            row += 1
            column = 0

for list in matrix:
    print(''.join(list))
