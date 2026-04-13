class Plant:
    def __init__(self, name: str, _height: float, _age: int) -> None:
        self.name = name.capitalize()
        self._height = _height
        self._age = _age

    def grow(self) -> float:
        self.grow_by = 0.8
        self._height += self.grow_by
        return self._height

    def age(self) -> int:
        self._age += 1
        return self._age

    def show(self) -> str:
        return (f"{self.name}: {self._height:.1f}cm,"
                f" {self._age} days old")


def main() -> None:
    plant = Plant("Rose", 25, 30)
    total_growth = 0.0
    print(" === Garden Plant Growth ===")
    print(f"{plant.show()}")
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        plant.grow()
        plant.age()
        print(f"{plant.show()}")
        total_growth += plant.grow_by
    print(f"Growth this week: {total_growth:.1f}cm")


if __name__ == "__main__":
    main()
