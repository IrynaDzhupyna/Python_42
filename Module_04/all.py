c3a8c1% cat ex0/ft_ancient_text.py 
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
        content = file.read()
        file.close()
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        return

    print("---\n")
    print(content, end="")
    print("\n---")
    print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
c3a8c1% cat ex1/ft_archive_creation.py 
import sys

def read_the_file(file_name: str) -> str | None:
    try:
        file = open(file_name, "r")
        content = file.read()
        file.close()
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        return None
    return content

def modify_the_content(content: str) -> str:
    lines = content.splitlines()
    transformed = []
    for line in lines:
        transformed.append(line + "#")
    return "\n".join(transformed)

def write_to_the_file(file_name: str, content: str) -> None:
    try:
        file = open(file_name, "w")
        file.write(content)
        file.close()
    except OSError as e:
        print(f"{e}")

def main() -> None:
    try:
        file_name = sys.argv[1]
    except IndexError:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    print("---\n")

    content = read_the_file(file_name)
    if content is None:
        return
    print(content)
    print()
    print("---")
    print(f"File '{file_name}' closed.")
    new_content = modify_the_content(content)
    print("Transform data:")
    print("---\n")
    print(new_content)
    print("\n---")
    new_file_name = input("Enter new file name (or empty): ")
    if not new_file_name:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file_name}'.")
    write_to_the_file(new_file_name, new_content)
    print(f"Data saved in file '{new_file_name}'")
    



if __name__ == "__main__":
    main()%                                                                     c3a8c1% cat ex2/ft_stream_management.py 
import sys

def print_error(message: str):
    print(f"[STDERR] {message}", file=sys.stderr)


def read_file(file_name: str) -> str | None:
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
    if content is None:
        return
    transformed_content = transform_data(content)
    copy_file(transformed_content)


if __name__ == "__main__":
    main()
c3a8c1% cat ex3/ft_vault_security.py 
def secure_archive(file_name: str, string: str,
                   new_content: str | None=None) -> tuple[bool, str]:
    try:
        if string == "r":
            with open(file_name, string) as file:
                content = file.read()
                return (True, content)

        elif string == "w" and new_content is not None:
            with open(file_name, string) as file:
                file.write(new_content)
                return (True, "Content successfully written to file")

        return (False, "Invalid operation")

    except OSError as e:
        return (False, str(e))

def main() -> None:
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "r"))

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt", "r")
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_fragment.txt", "w", result[1]))


if __name__ == "__main__":
    main()

