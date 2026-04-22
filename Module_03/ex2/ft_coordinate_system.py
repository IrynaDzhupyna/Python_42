import math


def get_player_pos() -> tuple:
    while True:
        u_input = input("Enter new coordinates as floats in format 'x,y,z': ")
        coordinates = u_input.split(',')
        if len(coordinates) != 3:
            print("Invalid synatax")
            continue
        try:
            x = float(coordinates[0])
            y = float(coordinates[1])
            z = float(coordinates[2])
        except ValueError:
            for value in coordinates:
                try:
                    float(value)
                except ValueError:
                    print(f"Error on parameter {value}: "
                          f"could not convert string to float: {value}")
        else:
            return x, y, z


def main() -> None:
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    s1 = get_player_pos()
    print(f"Got a first tuple: {s1}")
    print(f"It includes: X={s1[0]}, Y={s1[1]}, Z={s1[2]} ")
    print(f"Distance to center: "
          f"{math.sqrt(s1[0]**2 + s1[1]**2 + s1[2]**2):.4f}")
    print("\nGet a second set of coordinates")
    s2 = get_player_pos()
    distance = math.sqrt(
        (s2[0] - s1[0]) ** 2 +
        (s2[1] - s1[1]) ** 2 +
        (s2[2] - s1[2]) ** 2
    )
    print(f"Distance between the 2 sets of coordinates: {distance:.4f}")


if __name__ == "__main__":
    main()
