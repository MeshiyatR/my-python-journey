# DAY 9 EXERCISES - 10th May 2026
# Topic: Error Handling and Modules

# Exercise 1: Basic try/except
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("Error! Please enter a valid number!")

# Exercise 2: Multiple exceptions
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print(f"Result: {result}")
except ValueError:
    print("Error! Enter numbers only!")
except ZeroDivisionError:
    print("Error! Cannot divide by zero!")

# Exercise 3: try/except/else/finally
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age entered!")
else:
    print(f"Your age is {age}")
    if age >= 18:
        print("You are an adult!")
    else:
        print("You are a minor!")
finally:
    print("Program completed!")

# Exercise 4: Math module
import math
print(f"Pi value: {math.pi}")
print(f"Square root of 144: {math.sqrt(144)}")
print(f"Power 2^10: {math.pow(2, 10)}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")
print(f"Floor of 4.9: {math.floor(4.9)}")

# Exercise 5: Random module
import random
print(f"\nRandom number 1-100: {random.randint(1, 100)}")
print(f"Random choice: {random.choice(['Python', 'AI', 'Google', 'Germany'])}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")