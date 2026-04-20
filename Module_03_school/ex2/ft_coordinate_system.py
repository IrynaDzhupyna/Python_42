import math

def get_player_pos() -> tuple:
    while True:
        user_input = input("Enter new coordinates as floats in format 'x,y,z': ")
        coordinates = user_input.split(',')
        try:
            x = float(coordinates[0])
            y = float(coordinates[1])
            z = float(coordinates[2])
        except ValueError:
            print("Invalid synatax")
        else:
            coords = (x, y, z)
            return coords


def main() -> None:
    print("=== Game Coordinate System ===")
    print("\nGet a first set of coordinates")
    first_set = get_player_pos()
    print(f"Got a first tuple: {first_set}")
    print(f"It includes: X={first_set[0]}, Y={first_set[1]}, Z={first_set[2]} ")
    print(f"Distance to center: "
          f"{math.sqrt(first_set[0]**2 + first_set[1]**2 + first_set[2]**2):.4f}")
    print("\nGet a second set of coordinates")
    second_set = get_player_pos()
    distance = math.sqrt(
        (second_set[0] - first_set[0]) ** 2 +
        (second_set[1] - first_set[1]) ** 2 +
        (second_set[0] - first_set[0]) ** 2
    )
    print(f"Distance between the 2 sets of coordinates: {distance:.4f}")



if __name__=="__main__":
    main()