import sys
import typing


'''def create_test_file():
    lines = [
        "[FRAGMENT 001] Digital preservation protocols established 2087",
        "[FRAGMENT 002] Knowledge must survive the entropy wars",
        "[FRAGMENT 003] Every byte saved is a victory against oblivion"
    ]
    with open("ancient_fragment.txt", "w") as file:
        for line in lines:
            file.write(f"{line}\n")'''


def print_error(message: str):
    print(f"[STDERR] {message}", file=sys.stderr)


def read_file(file_name) -> str | None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    try:
        with open(file_name, "r") as file:
            content = file.read()
    except (FileNotFoundError, NotADirectoryError, PermissionError, OSError) as e:
        print_error(f"Error opening file '{file_name}': {e}")
        return

    print("_ _ _\n")
    print(content, end="")
    print("\n_ _ _\n")
    print(f"File '{file_name}' closed.")
    return content


# need type hint
def transform_data(content: str) -> str:
    transformed_lines = [line + "#" for line in content.splitlines()]
    transformed_content = "\n".join(transformed_lines)
    print("Transform data:")
    print("_ _ _\n")
    print(transformed_content)
    print("_ _ _")
    return transformed_content


def copy_file(transformed_content: str) -> None:
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_name = sys.stdin.readline().rstrip("\n")
    if not new_name:
        return print("Not saving data.")

    try:
        with open(new_name, "w") as new_file:
            new_file.write(transformed_content)
            print(f"Saving data to '{new_name}'")
    except (FileNotFoundError, NotADirectoryError, PermissionError, OSError) as e:
        print_error(f"Error creating file '{new_name}': {e}")
        return
    print(f"Data saved in file '{new_name}'.")


def main() -> None:
    # create_test_file()
    if len(sys.argv) != 2:
        return print_error(f"Usage {sys.argv[0]} <file>")
    file_name = sys.argv[1]
    content = read_file(file_name)
    if content is None:
        return

    transformed_content = transform_data(content)
    copy_file(transformed_content)


if __name__ == "__main__":
    main()