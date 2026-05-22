rows, columns = [int(x) for x in input().split(", ")]

matrix = []
sum_matrix = 0

for row in range(rows):
    lines = [int(x) for x in input().split(", ")]
    matrix.append(lines)

    sum_matrix += sum(matrix[row])

print(sum_matrix, matrix, sep="\n")