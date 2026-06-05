class MatrixContentError(Exception):
    pass


class MatrixSizeError(Exception):
    pass


def is_integer_matrix(matrix):
    try:
        for row in matrix:
            for item in row:
                int(item)
        return True
    except ValueError:
        return False


def rotate_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()


mtrx = []

while True:
    line = input().strip()

    if not line:
        break

    mtrx.append(line.split())

if not is_integer_matrix(mtrx):
    raise MatrixContentError("The matrix must consist of only integers")

n = len(mtrx)

if not all(len(row) == n for row in mtrx):
    raise MatrixSizeError("The size of the matrix is not a perfect square")

rotate_matrix(mtrx)

for row in mtrx:
    print(*row)