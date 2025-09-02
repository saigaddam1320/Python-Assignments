class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_details(self):
        print(f"Brand: {self.brand}, Speed: {self.speed}")

    def check_speed(self):
        if self.speed > 100:
            return "Speeding!"
        else:
            return "Within limit"


car1 = Car("Toyota", 90)
car2 = Car("BMW", 120)

car1.display_details()
print(car1.check_speed())   # Output: Within limit

car2.display_details()
print(car2.check_speed())   # Output: Speeding!
