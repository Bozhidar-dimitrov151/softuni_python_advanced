import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

words_file = os.path.join(BASE_DIR, "word.txt")
text_file = os.path.join(BASE_DIR, "text.txt")
output_file = os.path.join(BASE_DIR, "output.txt")

# Read words to search for
with open(words_file, "r") as file:
    words = file.read().lower().split()

counts = {word: 0 for word in words}

# Read the text once
with open(text_file, "r") as file:
    text = file.read().lower()

# Count occurrences
for word in counts:
    pattern = rf"\b{re.escape(word)}\b"
    counts[word] = len(re.findall(pattern, text))

# Sort by count descending
sorted_counts = sorted(
    counts.items(),
    key=lambda item: item[1],
    reverse=True
)

# Write result
with open(output_file, "w") as file:
    for word, count in sorted_counts:
        file.write(f"{word} - {count}\n")