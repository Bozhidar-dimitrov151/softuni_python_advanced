from collections import deque

def fill_the_box(length, width, height, *args):
    volume = length * width * height
    cube = deque(args)

    while cube:
        cur_cube = cube.popleft()

        if cur_cube == "Finish":
            return f"There is free space in the box. You could put {volume} more cubes."

        if cur_cube > volume:
            cur_cube -= volume
            cube_left = cur_cube + sum(x for x in cube if x != "Finish")
            return f"No more free space! You have {cube_left} more cubes."

        volume -= cur_cube

print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))