class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        # __preffix make the attribute private
        self.__age = age
    
    def show(self):
        return f"{self.name}: {self.height:.1f} cm, {self._age} days old"

plant = Plant("Rose", 25, 30)
print(f"{plant.show()}")
print(plant.__age)
print(f"{plant.show()}")