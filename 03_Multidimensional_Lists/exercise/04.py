from math import inf

def find_sum(matrix, r, c):
    square = [
    [matrix[r][c],
    matrix[r][c+1],
    matrix[r][c+2]],
    [matrix[r+1][c],
    matrix[r+1][c+1],
    matrix[r+1][c+2]],
    [matrix[r+2][c],
    matrix[r+2][c+1],
    matrix[r+2][c+2]]]

    cur_sum = sum([sum(x) for x in square])

    return cur_sum, square

rows, cols = input().split(" ")
matrix = []

max_sum = -inf
best_square = []

for row in range((int(rows))):
    matrix.append([int(x) for x in input().split(" ")])

for row in range(int(rows) - 2):
    for col in range(int(cols) - 2):
        cur_sum, cur_square = find_sum(matrix, row, col)

        if cur_sum > max_sum:
            max_sum = cur_sum
            best_square = cur_square

print(f"Sum = {max_sum}")
for sq_r in best_square:
    print(" ".join(str(x) for x in sq_r))