rows, cols = (int(x) for x in input().split())
matrix = [[x for x in input().split()]for _ in range(rows)]

while True:
    comm = input().split()

    if comm[0] == "END":
        break

    if len(comm) == 5 and 0 <= int(comm[1]) < rows and 0 <= int(comm[2]) < cols \
            and 0 <= int(comm[3]) < rows and 0 <= int(comm[4]) < cols:
        first_value = matrix[int(comm[1])][int(comm[2])]
        second_value = matrix[int(comm[3])][int(comm[4])]
        matrix[int(comm[3])][int(comm[4])] = first_value
        matrix[int(comm[1])][int(comm[2])] = second_value

        for lists in matrix:
            print(*lists)

    else:
        print("Invalid input!")
