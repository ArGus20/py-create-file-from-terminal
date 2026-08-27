import datetime
import os
from sys import argv


def create_file(command: list) -> None:
    last_element = len(command)
    if "-f" in command and "-d" in command:

        if command.index("-d") < command.index("-f"):
            dir_path = os.path.join(
                *command[command.index("-d") + 1:command.index("-f")]
            )
            os.makedirs(dir_path)
        else:
            dir_path = os.path.join(*command[command.index("-d") + 1:])
            os.makedirs(dir_path)

    elif "-d" in command:
        dir_path = os.path.join(*command[command.index("-d") + 1:last_element])
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in command:
        file_name = command[command.index("-f") + 1]

        if "-d" in command:
            file_name = os.path.join(dir_path, file_name)

        file_exists = os.path.exists(file_name)

        with open(file_name, "a") as a_file:
            if file_exists:
                a_file.write("\n")

            current_data = datetime.datetime.now()
            a_file.write(current_data.strftime("%Y-%m-%d %H:%M:%S") + "\n")

            text_line = input("Enter content line: ")
            count = 0
            while text_line != "stop":
                count += 1
                a_file.write(f"{count} {text_line}\n")
                text_line = input("Enter content line: ")


command = argv
create_file(command)
