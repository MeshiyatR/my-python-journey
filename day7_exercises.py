# DAY 7 EXERCISES - 8th May 2026
# Topic: Functions

# Exercise 1: Basic function
def greet():
    print("Hello! Welcome to my Python journey!")
    print("My name is Meshiyat Rubab")
    print("I am learning Python and AI Engineering")

greet()

# Exercise 2: Function with parameter
def greet_person(name):
    print(f"Hello {name}!")
    print(f"Welcome to Python world!")

greet_person("Sana")
greet_person("Ali")
greet_person("Sara")

# Exercise 3: Function with return
def add_numbers(a, b):
    result = a + b
    return result

answer = add_numbers(10, 20)
print(f"10 + 20 = {answer}")
print(f"50 + 75 = {add_numbers(50, 75)}")

# Exercise 4: Function with default parameter
def introduce(name, goal="AI Engineer", country="Germany"):
    print(f"My name is {name}")
    print(f"My goal is to become {goal}")
    print(f"I want to study in {country}")

introduce("Meshiyat")
introduce("Sara", "Data Scientist", "UK")

# Exercise 5: Multiple return values
def calculator(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    return addition, subtraction, multiplication

add, sub, mul = calculator(10, 5)
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")