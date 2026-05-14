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
