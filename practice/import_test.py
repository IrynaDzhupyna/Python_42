import sys
sys.path.append("../ex1")

from ft_garden_data import Plant

class   GrowingPlant(Plant):
    def __init__(self, name, height, age):
        super().__init__(name, height, age)
        self.grow = 0.8

    def grow(self):
        self.height = self.grow_by
        return self.height

    def age_up(self):
        self.age += 1
        return self.age

def main() -> None:
    plant = GrowingPlant("Rose", 25, 30)
    total_growth = 0
    print("=== Garten Plant Growth ===")
    plant.show()
    for i in range(8):
        print(f"=== Day {i} ===")
        plant.grow()
        plant.age_up()
        total_growth += plant.grow_by
        plant.show()
    print(f"Grows this week {total_growth:.1f}cm")

if __name__ == "__main__":
    main()
