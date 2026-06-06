import os.path

ABS_DIR = os.path.dirname(os.path.abspath(__file__))
filename = 'text.txt'
path_read = os.path.join(ABS_DIR, filename)

with open(path_read) as fr_files:
    lines = fr_files.readlines()

output_file = 'output.txt'
path_output = os.path.join(ABS_DIR, output_file)
restricted_char = {"-", ",", ".", "!", "?"}


with open(path_output, "w") as fw_file:
    for idx in range(0, len(lines), 2):
        string_add = ''
        new_line = lines[idx].split()

        for el in reversed(new_line):
            for char in el:
                if char in restricted_char:
                    el = el.replace(char, '@')
            string_add += el + ""

        print(string_add)


        fw_file.write(f"{string_add}\n")