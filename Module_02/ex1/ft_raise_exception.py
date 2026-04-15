def input_temperature(temp_str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise Exception(f"Caught input_temperature error: {temp}°C "
              "is too cold for plants (min 0°C)")
    elif temp > 40:
        raise Exception(f"Caught input_temperature error: {temp}°C "
              "is too hot for plants (max 40°C)")
    else:
        print(f"Temperature is now {temp}°C")
        return temp


def test_temperature(temp_str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        input_temperature(temp_str)
    except (ValueError, TypeError, Exception):
        print(f"Caught input_temperature error: "
              f"invalid literal for int() with base 10: '{temp_str}'")


def main() -> None:
    print("=== Garden temperature Checker ===\n")
    test_temperature('25')
    print()
    test_temperature('abc')
    print()
    test_temperature('100')
    print()
    test_temperature('-50')
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
