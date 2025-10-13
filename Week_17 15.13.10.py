# Define the Car class
class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def display_details(self):
        print(f"Car Details:")
        print(f" Brand : {self.brand}")
        print(f" Model : {self.model}")
        print(f" Year  : {self.year}")
        print(f" Color : {self.color}")


my_car = Car("BMW ", "430i", 2024, "Blue")


my_car.display_details()
