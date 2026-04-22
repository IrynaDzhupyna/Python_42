import sys
''''sword': 1, 'potion': 5, 'shield': 2, 'armor': 3,
'helmet': 1, 'magic_item': 1'''


def parse_input(argv) -> dict:
    inventory = {}
    for arg in argv:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
        else:
            key, value = arg.split(':')
            try:
                value = int(value)
            except ValueError:
                print(f"Quantity error for '{key}': "
                      f"invalid literal for int() with base 10: '{value}'")
                continue

            if key in inventory:
                print(f"Redundant item '{key}' - discarding")
            else:
                inventory[key] = value

    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")
    data = parse_input(sys.argv[1:])
    print("Got inventory: ", data)

    keys = list(data.keys())
    print("Item list: ", keys)

    total_quantity = sum(data.values())
    print(f"Total quantity of the {len(data.values())}"
          f" items: ", total_quantity)
    for key in data:
        quantity = data[key]
        percentage = (quantity / total_quantity) * 100
        print(f"Item '{key}' represents {percentage:.1f}%")

    max_item = None
    max_value = -1
    for key in data:
        value = data[key]

        if value > max_value:
            max_value = value
            max_item = key
    print(f"Item most abundant: {max_item} wit quantity {max_value}")

    min_item = None
    min_value = max_value
    for key in data:
        value = data[key]

        if value < min_value:
            min_value = value
            min_item = key
    print(f"Item least abundant: {min_item} wit quantity {min_value}")
    data.update({"magic_item": 1})
    print(f"Updated inventory: {data}")


if __name__ == "__main__":
    main()
