import os.path

ABS_DIR = os.path.dirname(os.path.abspath(__file__))

file_name = "my_first_file.txt."
path = os.path.join(ABS_DIR, file_name)

with open(path, 'a') as f:
    f.write("I just created my first file!")