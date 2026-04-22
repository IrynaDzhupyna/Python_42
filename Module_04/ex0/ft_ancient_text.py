import sys


def main() -> None:
    try:
        file_name = sys.argv[1]
    except IndexError:
        return print(f"Usage {sys.argv[0]} <file>")

    print("=== Cyber Archives Recovery ===")
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


if __name__ == "__main__":
    main()
