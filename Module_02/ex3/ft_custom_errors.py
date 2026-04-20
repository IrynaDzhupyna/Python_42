class GardenError(Exception):
    '''basic error for garden problems'''
    def __init__(self, message="Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    #For problems with plants (inherits from GardenError)
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    #For problems with plants (inherits from GardenError)
    def __init__(self, message="Unknown watering error") -> None:
        super().__init__(message)

# Example usage of custom exceptions
#PlantError is raised when the plant name is empty
def add_plant(plant_name):
    if plant_name is None or plant_name =="":
        raise PlantError("Name is not valid")
    else:
        print(f"Plant '{plant_name}' added to the garden.")

def water_plant(plant_name, amount):
    if amount <= 0:
        raise WaterError("Amount of water must be greater than zero")
    elif amount > 10:
        raise WaterError(f"The {plant_name} is wilting!")
    else:
        print(f"Watered plant '{plant_name}' with {amount} liters of water.")

def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    try:
        add_plant("")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    try:
        water_plant("Rose", -5) 
    except WaterError as e:
        print(f"Caught WaterError: {e}")

def main() -> None:
    test_custom_errors()

if __name__ == "__main__":
    main() 