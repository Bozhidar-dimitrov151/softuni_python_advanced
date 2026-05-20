numbers = tuple(map(float, input().split()))

counter = {}

for i in numbers:
    if i not in counter:
        counter[i] = 0

    counter[i] += 1

for key, value in counter.items():
    print(f"{key} - {value} times")