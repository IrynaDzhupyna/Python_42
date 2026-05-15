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

def write_to_the_file(file_name: str, content: list) -> None:
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
    main()