class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.__height = height
        self.__age = age

    def get_height(self) -> float:
        return self.__height

    def set_height(self, height) -> None:
        if height <= 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.__height = height
            print(f"Height updated: {self.__height}cm")

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


def main():
    plant = Plant("Rose", 15, 10)
    print("=== Garden Security System ===")
    print(f"Plant created: {plant.show()}\n")
    plant.set_height(25)
    plant.set_age(30)
    print()
    plant.set_height(-1)
    plant.set_age(-3)
    print()
    print(f"Current state: {plant.show()}")


if __name__ == "__main__":
    main()
