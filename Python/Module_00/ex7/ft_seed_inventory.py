def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    name = str.capitalize(seed_type) + " seeds:"
    if unit == "packets":
        print(name, quantity, "packets available")
    elif unit == "grams":
        print(name, quantity, "grams total")
    elif unit == "area":
        print(name + " covers", quantity, "square meters")
    else:
        print("Unknown unit type")
