def palindromes(matrix, rows, cols):
    for r in range(rows):
        for c in range(cols):
            current_palindrome = (
                chr(r + 97) +
                chr(r + c + 97) +
                chr(r + 97)
            )
            matrix[r][c] = current_palindrome

    return matrix


row, col = (int(x) for x in input().split())

matrix = [["" for _ in range(col)] for _ in range(row)]

result = palindromes(matrix, row, col)

for row in result:
    print(" ".join(row))