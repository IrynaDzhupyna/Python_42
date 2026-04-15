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


def add_plant(plant_name):
    if plant_name == "":
        raise PlantError("Name is not valid")
    else:
        pass


def main() -> None:

raise GardenError("message", 0)