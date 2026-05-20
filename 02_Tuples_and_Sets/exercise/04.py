word = input()

counter = {}

for character in word:
    if character not in counter:
        counter[character] = 0
    counter[character] += 1

for symbol, count in sorted(counter.items()):
    print(f"{symbol}: {count} time/s")