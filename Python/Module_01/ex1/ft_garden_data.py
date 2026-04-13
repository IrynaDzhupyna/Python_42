class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name.capitalize()
        self.height: float = height
        self.age: int = age

    def show(self) -> str:
        return (f"{self.name}: {self.height:.0f}cm, {self.age} days old")


def main() -> None:
    print("=== Garden Plant Registry ===")
    rose = Plant("rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)

    print(f"{rose.show()}")
    print(f"{sunflower.show()}")
    print(f"{cactus.show()}")


if __name__ == "__main__":
    main()
