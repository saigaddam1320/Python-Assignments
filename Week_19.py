
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

    def start(self):
        print(f"{self.brand} {self.model} is starting...")

class Bike (Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def display_info(self):
        super().display_info()
        print(f"Engine: {self.engine_cc}cc")

    def wheelie(self):
        print(f"{self.brand} {self.model} is doing a wheelie!")




class Bus(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def display_info(self):
        super().display_info()
        print(f"Seating Capacity: {self.capacity} passengers")

    def honk(self):
        print(f"{self.brand} {self.model} is honking: Honk! Honk!")


bike1 = Bike("Yamaha", "R15", 155)
bus1 = Bus("Volvo", "9400", 50)

print("\nBike Details:")
bike1.display_info()
bike1.start()
bike1.wheelie()

print("\nBus Details:")
bus1.display_info()
bus1.start()
bus1.honk()
