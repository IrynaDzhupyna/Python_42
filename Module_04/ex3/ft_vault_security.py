def secure_archive(file_name, string=None,
                   new_content=None) -> tuple[True | False, str]:
    print("=== Cyber Archives Security ===")
    try:
        if string == "r":
            with open(file_name, string) as file:
                print("Using 'secure_archive' to read from regular file")
                content = file.read()
                return (bool(content), content)

        elif string == "w":
            with open(file_name, string) as file:
                file.write(new_content)
                return (True, "Content successfully written to file")

    except (FileNotFoundError, NotADirectoryError):
        print("Using 'secure_archive' to read from nonexisting file")
        return (False, "[Errno 2] No such file or directory")

    except IsADirectoryError:
        print("Using 'secure_archive' to read from directory not a file")
        return (False, "[Errno 2] Is a directory, not a file")

    except PermissionError:
        print("Using 'secure_archive' to read from inaccessible file")
        return (False, f"[Errno 13] Permission denied: '{file_name}'")


def main() -> None:
    print(secure_archive("test.txt", "w", "hello"))


if __name__ == "__main__":
    main()
