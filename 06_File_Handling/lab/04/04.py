import os.path

ABS_DIR = os.path.dirname(os.path.abspath(__file__))
file_name = "text.txt"

path = os.path.join(ABS_DIR, file_name)

try:
    os.remove(path)
except FileNotFoundError:
    print('FIle already deleted')