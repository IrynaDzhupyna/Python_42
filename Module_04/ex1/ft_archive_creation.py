import sys


def read_file(file_name: str) -> str:

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    try:
        file = open(file_name, "r")
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
    else:
        lines = file.read()
        file.close()
        print("---\n")
        print(lines, end="")
        print("\n---\n")
        print(f"File '{file_name} closed.")
        return lines


def transform_data(file_name: str, lines: str) -> None:

    print("Transform data:")
    print("---\n")

    try:
        file = open(file_name, "w")
    except OSError as e:
        print(f"Error writting in a file {file_name}: {e}")
        return

    for line in lines:
        for letter in line:
            if letter == "\n":
                letter = "#\n"
            file.write(letter)
    try:
        file = open(file_name, "r")
    except OSError as e:
        print(f"Error opening file '{file}': {e}")
        return
    for line in file:
        print(line, end="")
    file.close()
    print("\n_ _ _\n")


def copy_file(file_name: str) -> None:

    new_name = input("Enter new file name (or empty): ")
    if not new_name:
        return print("Not saving data.")
    else:
        if new_name and not new_name.endswith(".txt"):
            new_name += ".txt"
        print(f"Saving data to '{new_name}'")
        try:
            new_file = open(new_name, "w")
        except OSError as e:
            print(f"File {new_file} can not be open: {e}")
        
        try:
            old_file = open(file_name, "r")
        except OSError as e:
            print("Error opening file '{file_name}': {e}")

        for line in old_file:
            new_file.write(line)
        print(f"Data saved in file '{new_name}'.")


def main() -> None:
    try:
        file_name = sys.argv[1]
    except IndexError:
        return print(f"Usage {sys.argv[0]} <file>")
    content = read_file(file_name)
    transform_data(file_name, content)
    copy_file(file_name)


if __name__ == "__main__":
    main()
