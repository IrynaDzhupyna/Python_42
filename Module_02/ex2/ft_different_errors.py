def garden_operations(operation_number):
    if operation_number == 0:
        int('abc')
    elif operation_number == 1:
        1 / 0
    elif operation_number == 2:
        open('/non/existent/file')
    elif operation_number == 3:
        'abc' + 10
    return

def test_error_types():
    try:
        garden_operations(0)
    except ValueError:
        return ("Caught ValueError: invalid literal for int() with base 10: 'abc'")

    try:
        garden_operations(1)
    except ZeroDivisionError:
        return ("Caught ZeroDivisionError: division by zero")
    '''while i != 5:
        try:
            garden_operations(i)
        except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError):
            if ValueError:
                print ("Caught ValueError: invalid literal for int() with base 10: 'abc'")
            elif ZeroDivisionError:
                print ("Caught ZeroDivisionError: division by zero")
            elif FileNotFoundError:
                print ("Caught FileNotFoundError: [Errno 2] No such file or directory: '/non/existent/file'")
            elif TypeError:
                print ('Caught TypeError: can only concatenate str (not "int") to str')
            else:
                print ("Operation completed successfully")'''


def main() -> None:
    i = 0
    for i in range(5):
        print(f"Testing operation {i}")
        print(f"{test_error_types()}")
        i += 1

if __name__ == "__main__":
    main()