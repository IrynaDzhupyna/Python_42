import sys


def main() -> None:
    # get the name from argv - str
    try:
        file_name = sys.argv[1]
    except IndexError:
        return print(f"Usage {sys.argv[0]} <file>")

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")

    try:
        file = open(file_name, "r")
    except (FileNotFoundError, NotADirectoryError):
        print(f"[Errno 2] No such file or directory: '{file_name}")
    except IsADirectoryError:
        print(f"[Errno 21] Is a directory")
    except PermissionError:
        print(f"Error opening file '{file_name}': "
              f"[Errno 13] Permission denied: '{file_name}'")
    else:
        content = file.read()
        print("---\n")
        print(content, end="")
        print("\n---\n")
        file.close()
        print(f"File '{file_name} closed.")

if __name__ == "__main__":
    main()
