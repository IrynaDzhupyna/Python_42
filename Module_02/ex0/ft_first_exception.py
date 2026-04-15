def input_temperature(temp_str) -> int:
    return int(temp_str)


def test_temperature(temp_str) -> None:
    try:
        num = input_temperature(temp_str)
        print(f"Input data is '{num}'")
        print(f"Temperature is now {num}C")
    except (ValueError, TypeError):
        print(f"Input data is '{temp_str}'")
        print(f"Caught input_temperature error:"
              f"invalid literal for int() with base 10: '{temp_str}'")


def main() -> None:
    temp_str_1 = '25'
    temp_str_2 = 'abc'
    print("=== Garden temperature ===\n")
    test_temperature(temp_str_1)
    print()
    test_temperature(temp_str_2)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
