class Plant:
    @staticmethod
    def age_checker(days: int):
        if days > 365:
            return True
        else:
            return False

    @classmethod
    def default_plant(cls):
        name = "Unknown plant"
        height = 0
        age = 0
        return cls(name, height, age)

    def __init__(self, name: str, height: float, _age: int):
        self.name = name
        self.__height = height
        self.__age = _age
        self.grow_count = 0
        self.age_count = 0
        self.show_count = 0

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

    def set_age(self, age):
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
            self.grow_count += 1
        return self.height

    def age(self, days) -> int:
        self._age = self.get_age() + days
        i = 0
        while i < days:
            self._age += 1
            i += 1
            self.age_count += 1
        return self._age

    def show(self):
        self.show_count += 1
        return (f"{self.name}: {self.__height:.1f}cm, {self.__age} days old")

    def statistics(self):
        print(f"[statistics for {self.name}]")
        print(f"Status: {self.grow_count} grow, "
              f"{self.age_count} age, {self.show_count} show")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True
        print(f"{self.name} is blooming beautifully!")

    def show(self):
        general = super().show()
        if self.is_blooming is True:
            status = "is blooming beautifully!"
        else:
            status = "has not bloomed yet"
        return (f"{general}\n"
                f"Color: {self.color}\n"
                f"{self.name} {status}")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.is_blooming = False
        self.seeds = 0

    def show(self):
        general = super().show()
        self.seeds = 42
        return (f"{general}\nSeeds: {self.seeds}")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_count = 0

    def produce_shade(self):
        self.shade_count += 1
        return (f"Tree {self.name} "
                f"now produces a shade of {self.get_height()}cm long "
                f"and {self.trunk_diameter}cm wide.")

    def show(self) -> str:
        general = super().show()
        return (f"{general}\nTrunk diameter: {self.trunk_diameter}")

    def statistics(self):
        print(f"[statistics for {self.name}]")
        print(f"Status: {self.grow_count} grow, "
              f"{self.age_count} age, {self.show_count} show, "
              f"{self.shade_count} shade")


def main():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    days = 30
    result = Plant.age_checker(days)
    print(f"Is {days} days more than a year? -> {result}")

    days = 400
    result = Plant.age_checker(days)
    print(f"Is {days} days more than a year? -> {result}")

    flower = Flower("Rose", 15, 10, "red")
    print("\n=== Flower")
    print(f"{flower.show()}")
    flower.statistics()
    print("[asking the rose to grow and bloom]")
    flower.set_height(flower.grow(10, 0.8))
    flower.bloom()
    print(f"{flower.show()}")
    flower.statistics()

    tree = Tree("Oak", 200, 365, 5)
    print("\n=== Tree")
    print(f"{tree.show()}")
    tree.statistics()
    print("[asking the oak to produce shade]")
    print(f"{tree.produce_shade()}")
    tree.statistics()

    seed = Seed("Sunflower", 80, 45, "yellow")
    print("\n=== Seed")
    print(f"{seed.show()}")
    print("[make sunflower grow, age and bloom]")
    seed.set_height(seed.grow(20, 1.5))
    seed.set_age(seed.age(20))
    seed.bloom()
    print(f"{seed.show()}")
    seed.statistics()

    anonymous = Plant.default_plant()
    print("\n=== Anonymous")
    print(f"{anonymous.show()}")
    anonymous.statistics()


if __name__ == "__main__":
    main()
