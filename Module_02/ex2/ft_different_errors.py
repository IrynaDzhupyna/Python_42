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


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
        except ValueError:
            print("Caught ValueError: invalid literal for int() "
                  "with base 10: 'abc'")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero")
        except FileNotFoundError:
            print("Caught FileNotFoundError: [Errno 2] "
                  "No such file or directory: '/non/existent/file'")
        except TypeError:
            print('Caught TypeError: '
                  'can only concatenate str (not "int") to str')
        else:
            print("Operation completed successfully")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
