import sys
import typing


def create_test_file():
    lines = [
        "[FRAGMENT 001] Digital preservation protocols established 2087",
        "[FRAGMENT 002] Knowledge must survive the entropy wars",
        "[FRAGMENT 003] Every byte saved is a victory against oblivion"
    ]
    with open("ancient_fragment.txt", "w") as file:
        for line in lines:
            file.write(f"{line}\n")


def read_file(file_name) -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    try:
        with open(file_name, "r") as file:
            lines = file.read()
    except (FileNotFoundError, NotADirectoryError):
        print(f"Error opening file '{file_name}': "
              f"[Errno 2] No such file or directory: '{file_name}'")
    except PermissionError:
        print(f"Error opening file '{file_name}': "
              f"[Errno 13] Permission denied: '{file_name}'")
    else:
        print("_ _ _\n")
        print(lines, end="")
        print("\n_ _ _\n")
        print(f"File '{file_name} closed.")


# need type hint
def transform_data(file_name: str) -> None:
    print("Transform data:")
    print("_ _ _\n")
    with open(file_name, "r") as file:
        lines = file.read()

    with open(file_name, "w") as file:
        for line in lines:
            for letter in line:
                if letter == "\n":
                    letter = "#\n"
                file.write(letter)

    with open(file_name, "r") as file:
        for line in file:
            print(line, end="")
    print("\n_ _ _\n")

def copy_file(file_name: str) -> None:
    new_name = input("Enter new file name (or empty): ")
    if not new_name:
        return print("Not saving data.")
    else:
        if new_name and not new_name.endswith(".txt"):
            new_name += ".txt"
        print(f"Saving data to '{new_name}'")
        with open(new_name, "w") as new_file:
            with open(file_name, "r") as old_file:
                for line in old_file:
                    new_file.write(line)
        print(f"Data saved in file '{new_name}'.")
            


def main() -> None:
    create_test_file()
    try:
        file_name = sys.argv[1]
    except IndexError:
        return print(f"Usage {sys.argv[0]} <file>")
    read_file(file_name)
    transform_data(file_name)
    copy_file(file_name)
    

    



if __name__ == "__main__":
    main()
