import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filename = "text.txt"

path = os.path.join(BASE_DIR, filename)

try:
    with open(path, "r") as file:
        print("File found")
except FileNotFoundError:
    print("File not found")