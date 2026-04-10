class Plant:
    def __init__(self, name: str, height_original: float, age_original: int):
        self.name = name.capitalize()
        self.height_original = height_original
        self.age_original = age_original

    def grow(self) -> float:
        self.grow_by = 0.8
        self.height_original += self.grow_by
        return self.height_original

    def age(self) -> int:
        self.age_original += 1
        return self.age_original

    def show(self) -> None:
        print(f"{self.name}: {self.height_original:.1f}cm, {self.age_original} days old")

def main() -> None:
    plant = Plant("Rose", 25, 30)
    total_growth = 0
    print(" === Garden Plant Growth ===")
    for i in range(1, 8):
        print(f"=== Day {i}===")
        plant.grow()
        plant.age()
        plant.show()
        total_growth += plant.grow_by
    print(f"Growth this week: {total_growth:.1f}cm")

if __name__ == "__main__":
    main()
