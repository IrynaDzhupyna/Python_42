class   Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age

    def get_height(self) -> float:
        return self.__height

    def set_height(self, height) -> str:
        if height <= 0:
            return (f"{self.name}: Error, height can't be negative\n"
                    "Height update rejected")
        else:
            self.__height = height
            return (f"Height updated: {self.__height}cm")

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age) -> None:
        if age <= 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days")

    def show(self) -> str:
        return (f"{self.name}: {self.__height:.1f}cm, {self.__age} days old")

class Flower(Plant):
    def __init__(self, name, height, age, color, is_blooming):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self):
        self.is_blooming = True
    
    def show(self) -> str:
        general = super().show()
        status = "is blooming beautifully!" if self.is_blooming else "has not bloomed yet"
        return (f"{general}\n"
                f"Color: {self.color}\n"
                f"{self.name} {status}")

class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter, shade):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = False

    def produce_shade(self):
        self.shade = True

    def show(self) -> str:
        general = super().show()
        status = "now produces a shade of" if self.shade else "does not produce shade"
        return (f"Tree {self.name} {status} {self.height}cm long and {self.trunk_diameter}cm wide.")

class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self) -> str:
        general = super().show()
        return (f"Vegetable {general}\n"
                f"Harvest season: {self.harvest_season}\n"
                f"Nutritional value: {self.nutritional_value}") 


def main():
    print("=== Garden Plant Types ===\n""=== Flower ===")
    flower = Flower("Rose",15, 10, "red", False)
    print(f"{flower.show()}")
    print("[asking the rose to bloom]")
    flower.bloom()
    print(f"{flower.show()}\n")

    tree = Tree("Oak", 200, 365, 5.0, False)
    print("=== Tree ===")
    print(f"{tree.show()}")
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    vegetable = Vegetable("Tomato", 5, 10, "April", 0)
    print(f"{vegetable.show()}\n")
    print("[make tomato grow and age for 20 days]")
    


if __name__ == "__main__":
    main()