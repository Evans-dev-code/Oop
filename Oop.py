# Example Python program demonstrating OOP

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_car(self):
        print(f"Car Brand: {self.brand}")
        print(f"Speed: {self.speed} km/h")

# Creating an object of Car class
my_car = Car("Tesla", 200)
my_car = Car("Toyota", 400)

# Calling method
my_car.display_car()
