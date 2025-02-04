# Python Fundamentals - Learn Python from Scratch

# 1. VARIABLES & DATA TYPES
name = "Alice"  # String
age = 25  # Integer
height = 5.6  # Float
is_student = True  # Boolean
hobbies = ["reading", "gaming", "coding"]  # List
person = {"name": "Alice", "age": 25, "city": "New York"}  # Dictionary

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")
print("Hobbies:", hobbies)
print("Person Details:", person)

# 2. CONDITIONAL STATEMENTS
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 3. LOOPS (FOR & WHILE)
print("\nFor Loop Example:")
for hobby in hobbies:
    print(f"- {hobby}")

print("\nWhile Loop Example:")
count = 3
while count > 0:
    print(f"Countdown: {count}")
    count -= 1

# 4. FUNCTIONS
def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}!"

print(greet("Alice"))

# Function with multiple parameters
def add_numbers(a, b):
    return a + b

print(f"Sum: {add_numbers(5, 10)}")

# 5. CLASSES & OBJECT-ORIENTED PROGRAMMING (OOP)
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Create an object
my_car = Car("Toyota", "Camry", 2022)
print("\nCar Details:", my_car.car_info())

# 6. FILE HANDLING
try:
    with open("sample.txt", "w") as file:
        file.write("Hello, this is a test file.\nPython is awesome!")
    with open("sample.txt", "r") as file:
        content = file.read()
        print("\nFile Content:\n", content)
except Exception as e:
    print("Error reading file:", e)

# 7. EXCEPTION HANDLING
try:
    result = 10 / 0  # This will cause an error
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("End of error handling example.")

# 8. LIST COMPREHENSION
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print("\nSquared Numbers:", squared_numbers)

# 9. IMPORTING MODULES (MATH & RANDOM)
import math
import random

print("\nMath Example:")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Random number (1-100): {random.randint(1, 100)}")

# 10. SIMPLE DATA VISUALIZATION USING MATPLOTLIB
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [10, 20, 30, 40, 50]

plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
plt.title("Simple Data Visualization")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
