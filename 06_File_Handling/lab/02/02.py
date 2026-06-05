import os

ABSOLUTE_PATH = os.path.dirname(os.path.abspath(__file__))
filename = "text.txt"

path = os.path.join(ABSOLUTE_PATH, filename)
file = open(filename, "r")
lines = file.readlines()

sum = 0
for line in lines:
    sum += int(line.strip())

file.close()

print(sum)