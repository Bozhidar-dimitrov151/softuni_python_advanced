from collections import deque

magic_level_to_doll = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

materials = deque(map(int, input().split()))
magic_level = deque(map(int, input().split()))

toys_crafted = []
is_crafted = False

while materials and magic_level:

    current_material = materials.pop()
    current_magic = magic_level.popleft()

    if current_material == 0 or current_magic == 0:
        if current_material == 0 and current_magic == 0:
            continue
        elif current_material == 0:
            magic_level.appendleft(current_magic)
        else:
            materials.append(current_material)
        continue

    product = current_material * current_magic

    if product in magic_level_to_doll:
        toys_crafted.append(magic_level_to_doll[product])

    elif product < 0:
        materials.append(current_material + current_magic)

    elif product > 0:
        materials.append(current_material + 15)

if ("Doll" in toys_crafted and "Wooden train" in toys_crafted) or \
   ("Teddy bear" in toys_crafted and "Bicycle" in toys_crafted):
    is_crafted = True

if is_crafted:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")

if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for toy in sorted(set(toys_crafted)):
    print(f"{toy}: {toys_crafted.count(toy)}")