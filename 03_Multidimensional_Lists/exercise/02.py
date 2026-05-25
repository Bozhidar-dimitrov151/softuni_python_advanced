size = int(input())
matrix = [[int(x) for x in input().split()] for rows in range(size)]

first_diagonal = 0
second_diagonal = 0

for row in range(len(matrix)):
    column = row
    col_sec = size - row - 1
    first_diagonal += matrix[row][column]
    second_diagonal += matrix[row][col_sec]

print(abs(first_diagonal - second_diagonal))