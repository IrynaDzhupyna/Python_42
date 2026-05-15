import sys


def read_file(file_name: str) -> str | None:
    # reads the original
    # transforms in memory
    # asks where to save

    try:
        file = open(file_name, "r")
    except OSError as e:
        print(f"Error opening file '{file_name}': {e}")
        return
    
    lines = file.read()
    file.close()
    print("---\n")
    print(lines, end="")
    print("\n---\n")
    print(f"File '{file_name} closed.\n")
    return lines


def transform_data(content: str) -> None:

    lines = content.split()
    transformed = []
    for line in lines:
        transformed.append(line + "#")
    "\n".join(transformed)
    return transformed


def copy_file(old_name: str, new_name: str) -> None:

        try:
            new_file = open(new_name, "w")
        except OSError as e:
            print(f"File {new_file} can not be open: {e}")
        
        try:
            old_file = open(old_name, "r")
        except OSError as e:
            print("Error opening file '{file_name}': {e}")

        for line in old_file:
            new_file.write(line)
        print(f"Data saved in file '{new_name}'.")


def main() -> None:
    try:
        file_name = sys.argv[1]
    except IndexError:
        return print(f"Usage {sys.argv[0]} <file>")
    
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file_name}'")
    content = read_file(file_name)

    print("Transform data:")
    print("---\n") 
    lines = transform_data(content)
    for line in lines:
        print(line)

    
    new_name = input("Enter new file name (or empty): ")
    if not new_name:
        print("Not saving data.")
        return
    else:
        print(f"Saving data to '{new_name}'")
   # copy_file(file_name)


if __name__ == "__main__":
    main()
