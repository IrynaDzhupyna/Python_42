# secure acces to any file
#   for reading or writing
#   returns tuple (True|False, str)
#       True + content of file
#       False + error message
# str == "w" or "r"
def create_test_file(file_name):
    lines = [
        "[FRAGMENT 001] Digital preservation protocols established 2087",
        "[FRAGMENT 002] Knowledge must survive the entropy wars",
        "[FRAGMENT 003] Every byte saved is a victory against oblivion"
    ]
    with open(f"{file_name}", "w") as file:
        for line in lines:
            file.write(f"{line}\n")


def secure_archive(file_name, str, new_content=None) -> tuple:
    print("=== Cyber Archives Security ===")
    try:
        with open(f"{file_name}", str) as file:
            if str == "r":
                content = file.read()
            elif str == "w":
                file.write(new_content)
    except (FileNotFoundError, NotADirectoryError):
        print(f"Error opening file '{file_name}': "
              f"[Errno 2] No such file or directory: '{file_name}'")
    except PermissionError:
        print(f"Error opening file '{file_name}': "
              f"[Errno 13] Permission denied: '{file_name}'")


def main() -> None:
    new_file = create_test_file("ancient_fragment.txt")
    
    with open(f"{new_file}", "r") as f:
        content = f.read()
        for line in content:
            print(line)
    secure_archive(new_file, "r")

if __name__ == "__main__":
    main()
