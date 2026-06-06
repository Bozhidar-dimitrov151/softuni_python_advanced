import os.path
from string import punctuation

ABS_DIR = os.path.dirname(os.path.abspath(__file__))
file_read = 'text.txt'
path_read = os.path.join(ABS_DIR, file_read)

with open(path_read) as fr_file:
    lines = fr_file.readlines()

file_to_write = 'output.txt'
path_write = os.path.join(ABS_DIR, file_to_write)
line_counter = 0

for line in lines:
    punctuation_counter = 0
    letter_counter = 0
    line_counter += 1
    for char in line:
        if char in punctuation:
            punctuation_counter += 1
        elif char.isalpha():
            letter_counter += 1

    new_line = f"Line {line_counter}: {line.strip()} ({letter_counter})({punctuation_counter})\n"
    with open(path_write, 'a') as fw_file:
        fw_file.write(new_line)