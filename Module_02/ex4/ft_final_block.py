def water_plant(plant_name):
    plant = str.capitalize(plant_name)
    if plant_name == plant:
        print("[OK]")
    else:
        print("Caught PlantError: Invalid plant name to water:"
              "'lettuce'\n.. ending tests and returning to main")

def main()