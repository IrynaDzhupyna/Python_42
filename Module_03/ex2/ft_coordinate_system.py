import math

def get_player_pos():
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    while True:
        player_coordinates = input("Enter player coordinates as floats in format 'x, y, z': ")
        try:
            x, y, z = map(float, player_coordinates.split(','))
        except ValueError:
            print("Invalid syntax")
        else:
            print(f"Got first tuple: ({x}, {y}, {z})")
            print(f"It includes: X = {x}, Y = {y}, Z = {z}")
            print(f"Distance to center: {math.sqrt(x**2 + y**2 + z**2):.4f}")
            break
    while True:
        print("Get a second set of coordinates")
        player_coordinates = input("Enter new coordinates as floats in format 'x, y, z': ")
        try:
            x, y, z = map(float, player_coordinates.split(','))
        except ValueError:
            print("Error on parameters 'abc': could not convert string to float: 'abc'")
        else:
            # print(f"Got second tuple: ({x}, {y}, {z})")
            # print(f"It includes: X = {x}, Y = {y}, Z = {z}")
            print(f"Distance between the 2 sets of coordinates: {math.sqrt(x**2 + y**2 + z**2):.4f}")
            break

def main():
    get_player_pos()

if __name__ == "__main__":
    main()