worms = list(map(int, input().split()))
holes = list(map(int, input().split()))

matches = 0
worm_size = len(worms)

while worms and holes:
    cur_worm = worms[-1]
    cur_hole = holes[0]

    if cur_worm == cur_hole:
        worms.pop()
        holes.pop(0)
        matches += 1
    else:
        worms[-1] -= 3

        if worms[-1] <= 0:
            worms.pop()
        holes.pop(0)

print(f"Matches: {matches}" if matches != 0 else "There are no matches.")

if matches != worm_size:
    print(f"Worms left: {', '.join(map(str, worms))}" if worms else "Worms left: none")
else:
    print("Every worm found a suitable hole!")

print(f"Holes left: {', '.join(map(str, holes))}" if holes else "Holes left: none")