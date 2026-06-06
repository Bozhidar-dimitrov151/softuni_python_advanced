import os


def create_file(filename):
    open(filename, "w").close()


def add_to_file(filename, text):
    with open(filename, "a") as file:
        file.write(text + "\n")


def replace_in_file(filename, old_text, new_text):
    try:
        with open(filename, "r") as file:
            content = file.read()

        with open(filename, "w") as file:
            file.write(content.replace(old_text, new_text))

    except FileNotFoundError:
        print("An error occurred")


def delete_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print("An error occurred")


while True:
    command = input()

    if command == "End":
        break

    action, *args = command.split("-")

    if action == "Create":
        create_file(args[0])

    elif action == "Add":
        add_to_file(args[0], args[1])

    elif action == "Replace":
        replace_in_file(args[0], args[1], args[2])

    elif action == "Delete":
        delete_file(args[0])