import sys

def read_the_file(file_name: str) -> str:
    try:
        file = open(file_name, "r")
        content = file.read()
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        return
    file.close()
    return content

def modify_the_content(content: str) -> str:
    lines = content.split()
    transformed = []
    for line in lines:
        transformed.append(line + "#")
    return transformed

def write_to_the_file(file_name: str, content: list) -> str | None:
    try:
        file = open(file_name, "w")
        for line in content:
            file.write(line)
    except OSError as e:
        print(f"{e}")
    file.close()
    return file

def main() -> None:
    try:
        file_name = sys.argv[1]
    except IndexError:
        print(f"Usage: {sys.argv[0]} <file>")

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
    for line in new_content:
        print(line)
    print("\n---")
    new_file_name = input("Enter new file name (or empty): ")
    if not new_file_name:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file_name}'.")
    new_file = write_to_the_file(new_file_name, new_content)
    if not new_file:
        print("Not saving data")
    print(f"Data saved in file '{new_file_name}'")
    



if __name__ == "__main__":
    main()