class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")
    rose = Plant("rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    rose.show()
    sunflower.show()
    cactus.show()


if __name__ == "__main__":
    main()
