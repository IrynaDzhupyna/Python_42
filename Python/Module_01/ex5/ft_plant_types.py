class Plant:
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

    def grow(self, days, per_day) -> float:
        self.height = self.get_height()
        self.grow_by = per_day
        i = 0
        while i < days:
            self.height += self.grow_by
            i += 1
        return self.height

    def age(self, days) -> int:
        i = 0
        while i < days:
            self.__age += 1
            i += 1
        return self.__age

    def show(self) -> str:
        return (f"{self.name}: {self.__height:.1f}cm, {self.__age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color, is_blooming) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> str:
        general = super().show()
        if self.is_blooming is True:
            status = "is blooming beautifully!"
        else:
            status = "has not bloomed yet"
        return (f"{general}\n"
                f"Color: {self.color}\n"
                f"{self.name} {status}")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> str:
        return (f"Tree {self.name} "
                f"now produces a shade of {self.get_height():.1f}cm long "
                f"and {self.trunk_diameter}cm wide.")

    def show(self) -> str:
        general = super().show()
        return (f"{general}\n"
                f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def nutritional_value_increase(self, days) -> int:
        i = 0
        while i < days:
            self.nutritional_value += 1
            i += 1
        return self.nutritional_value


def main() -> None:
    print("=== Garden Plant Types ===""\n=== Flower")
    flower = Flower("Rose", 15, 10, "red", False)
    print(f"{flower.show()}")
    print("[asking the rose to bloom]")
    flower.bloom()
    print(f"{flower.show()}")

    tree = Tree("Oak", 200, 365, 5.0)
    print("\n=== Tree")
    print(f"{tree.show()}")
    print("[asking the oak to produce shade]")
    print(tree.produce_shade())

    vegetable = Vegetable("Tomato", 5, 10, "April")
    print("\n=== Vegetable")
    print(f"{vegetable.show()}")
    print("[make tomato grow and age for 20 days]")
    vegetable.set_height(vegetable.grow(20, 2.1))
    vegetable.set_age(vegetable.age(20))
    print(f"{vegetable.show()}\nHarvest season: {vegetable.harvest_season}\n"
          f"Nutritonal value: {vegetable.nutritional_value_increase(20)}")


if __name__ == "__main__":
    main()
