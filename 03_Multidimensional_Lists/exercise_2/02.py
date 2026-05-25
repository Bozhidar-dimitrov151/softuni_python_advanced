matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

while True:
    com = input()

    if com == "END":
        break

    operation, row, col, value = com.split()

    row = int(row)
    col = int(col)
    value = int(value)

    if operation == "Add" and 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        matrix[row][col] += value

    elif operation == "Subtract" and 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        matrix[row][col] -= value

    else:
        print("Invalid coordinates")

for row in matrix:
    print(*row)