def garden_operations(operation_number):
    if operation_number == 0:
        int('abc')
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open('/non/existent/file')
    elif operation_number == 3:
        'abc' + 10
    else:
        return


def test_error_types(i):
    try:
        garden_operations(i)
    except ValueError:
        return ("Caught ValueError: invalid literal for int() "
                "with base 10: 'abc'")
    except ZeroDivisionError:
        return ("Caught ZeroDivisionError: division by zero")
    except FileNotFoundError:
        return ("Caught FileNotFoundError: [Errno 2] "
                "No such file or directory: '/non/existent/file'")
    except TypeError:
        return ('Caught TypeError: '
                'can only concatenate str (not "int") to str')
    else:
        return ("Operation completed successfully")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    i = 0
    while i < 5:
        print(f"Testing operation {i}...")
        print(f"{test_error_types(i)}")
        i += 1
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
