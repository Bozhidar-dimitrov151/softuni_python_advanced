size = int(input())
matrix = [[int(x) for x in input().split(', ')] for rows in range(size)]

primary_diagonal_list = [matrix[row][row] for row in range(size)]
secondary_diagonal_list = [matrix[row][size - row - 1] for row in range(size)]

print(
    f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal_list)}. Sum: {sum(primary_diagonal_list)}"'\n'
    f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal_list)}. Sum: {sum(secondary_diagonal_list)}"
)