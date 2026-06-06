from collections import defaultdict
import os


path = input()
files_by_extension = defaultdict(list)

try:
    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            _, extension = os.path.splitext(file)

            if extension:
                files_by_extension[extension].append(file)

    with open(os.path.join(path, "report.txt"), "w") as report:
        for extension, files in sorted(files_by_extension.items()):
            report.write(f"{extension}\n")

            for file in sorted(files):
                report.write(f"- - - {file}\n")

except FileNotFoundError:
    print("Directory does not exist")