num = int(input())
matrix = []
a_row = 0
a_col = 0
tea_bags = 0
r_col = 0
r_row = 0
failed = False

for n in range(num):
    cur_row = input().split(" ")
    matrix.append(cur_row)

    if "A" in cur_row:
        a_col = cur_row.index("A")
        a_row = n

    if "R" in cur_row:
        r_col = cur_row.index("R")
        r_row = n

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

row, col = a_row, a_col

while True:
    matrix[row][col] = "*"
    cur_dir = input()
    row += directions[cur_dir][0]
    col += directions[cur_dir][1]

    if not 0 <= row < num or not 0 <= col < num:
        failed = True
        break


    if matrix[row][col].isdigit():
        tea_bags += int(matrix[row][col])
        matrix[row][col] = "*"
    elif matrix[row][col] == ".":
        matrix[row][col] = "*"
    elif matrix[row][col] == "R":
        matrix[row][col] = "*"
        failed = True
        break


    if tea_bags >= 10:
        print("She did it! She went to the party.")
        break


if failed:
    print("Alice didn't make it to the tea party.")

for r in matrix:
    print(" ".join(r))
