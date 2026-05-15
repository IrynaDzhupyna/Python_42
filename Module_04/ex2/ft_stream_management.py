import sys

def print_error(message: str):
    print(f"[STDERR] {message}", file=sys.stderr)


def read_file(file_name) -> str | None:
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")

    try:
        file = open(file_name, "r")
        content = file.read()
    except OSError as e:
        print_error(f"Error opening file '{file_name}': {e}")
        return

    print("---\n")
    print(content, end="")
    print("\n---\n")
    print(f"File '{file_name}' closed.\n")
    return content


def transform_data(content: str) -> str:
    transformed_lines = [line + "#" for line in content.splitlines()]
    transformed_content = "\n".join(transformed_lines)
    print("Transform data:")
    print("---\n")
    print(transformed_content)
    print("---")
    return transformed_content


def copy_file(transformed_content: str) -> None:
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_name = sys.stdin.readline().rstrip("\n")
    if not new_name:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_name}'")
    try:
        new_file = open(new_name, "w")
        new_file.write(transformed_content)
        new_file.close()
    except OSError as e:
        print_error(f"Error creating file '{new_name}': {e}")
        print("Data not saved.")
        return
    print(f"Data saved in file '{new_name}'.")


def main() -> None:
    # create_test_file()
    if len(sys.argv) != 2:
        return print(f"Usage {sys.argv[0]} <file>")
    file_name = sys.argv[1]
    content = read_file(file_name)
    file_name.close()
    if content is None:
        return
    transformed_content = transform_data(content)
    copy_file(transformed_content)


if __name__ == "__main__":
    main()
