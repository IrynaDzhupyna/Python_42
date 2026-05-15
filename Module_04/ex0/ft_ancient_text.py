import sys


def main() -> None:
    try:
        file_name = sys.argv[1]
    except IndexError:
        print(f"Usage {sys.argv[0]} <file>")
        return

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")

    try:
        file = open(file_name, "r")
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        return

    content = file.read()
    file.close()
    print("---\n")
    print(content, end="")
    print("\n---")
    print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
