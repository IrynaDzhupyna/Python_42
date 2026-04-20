def input_temperature(temp_str: str) -> int:
    return int(temp_str)

def test_temperature(input) -> str:
    try:
        value: int = input
        print(f"Temperature is now {value}°C")
    except ValueError:
        print("Caught input_temperature error: invalid literal for int() with base 10: 'abc'")

def main() -> None:
    temp_str = '25'
    input_temperature(temp_str)
