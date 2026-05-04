def secure_archive(file_name, string=None, new_content=None) -> tuple:
    print("=== Cyber Archives Security ===")
    try:
        with open(file_name, string) as file:
            if string == "r":
                print("Using 'secure_archive' to read from regular file")
                content = file.read()
                return (bool(content), content)

            elif string == "w":
                print("Using 'secure_archive' "
                      "to write previous content to a new file")
                with open(file_name, "r") as file_1:
                    content = file_1.read()

                with open("new_file.txt", "w") as file_2:
                    file_2.write(content)

                return (bool(content), content)
    except (FileNotFoundError, NotADirectoryError, IsADirectoryError):
        print("Using 'secure_archive' to read from nonexisting file")
        return ("False", f"[Errno 2] No such file or directory: '{file_name}'")
    except PermissionError:
        print("Using 'secure_archive' to read from inaccessible file")
        return ("False", f"[Errno 13] Permission denied: '{file_name}'")


def main() -> None:
    print(secure_archive("test.txt", "r"))
    print(secure_archive("ancient_fragment.txt", "w"))


if __name__ == "__main__":
    main()
