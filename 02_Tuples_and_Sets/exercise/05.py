number_intersections = int(input())

longest = []

for _ in range(number_intersections):
    first, second = input().split("-")

    first_start, first_end = map(int, first.split(","))
    second_start, second_end = map(int, second.split(","))

    set_1 = set(range(first_start, first_end + 1))
    set_2 = set(range(second_start, second_end + 1))

    current = set_1.intersection(set_2)

    if len(current) > len(longest):
        longest = list(current)

print(f"Longest intersection is [{', '.join(map(str, longest))}] with length {len(longest)}")