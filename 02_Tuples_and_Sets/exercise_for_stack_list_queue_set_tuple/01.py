first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))
numbers = int(input())

for _ in range(numbers):
    tokens = input().split()

    command = " ".join(tokens[:2])
    nums = list(map(int, tokens[2:]))

    if command == "Add First":
        for num in nums:
            first_sequence.add(num)

    elif command == "Add Second":
        for num in nums:
            second_sequence.add(num)

    elif command == "Remove First":
        for num in nums:
            first_sequence.discard(num)

    elif command == "Remove Second":
        for num in nums:
            second_sequence.discard(num)

    elif command == "Check Subset":
        print(first_sequence.issubset(second_sequence) or
              second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")