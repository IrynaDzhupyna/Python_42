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
    with open(file_name, "r") as file:
        lines: List[str] = file.readlines()

    new_lines: List[str] = [line.rstrip("\n") + "#\n" for line in lines]

    with open(file_name, "w") as file:
        file.writelines(new_lines)

    with open(file_name, "r") as file:
        print("Transformed data: \n")
        for line in lines:
            print(line)
        # new_lines = [line.rstrip("\n") + "#" for line in file]
        # new_lines = [line.append("\n") for line in file]
        # print(new_lines)


def main() -> None:
    create_test_file()
    try:
        file_name = sys.argv[1]
    except IndexError:
        return print(f"Usage {sys.argv[0]} <file>")
    read_file(file_name)
    transform_data(file_name)

    



if __name__ == "__main__":
    main()