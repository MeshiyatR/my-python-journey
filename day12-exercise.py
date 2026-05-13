# DAY 12 EXERCISES - 13th May 2026
# Topic: Modules and Libraries

# Exercise 1: datetime module
from datetime import datetime, date

now = datetime.now()
print(f"Current date: {now.strftime('%d-%m-%Y')}")
print(f"Current time: {now.strftime('%H:%M:%S')}")
print(f"Day: {now.strftime('%A')}")
print(f"Month: {now.strftime('%B')}")

today = date.today()
birthday = date(2026, 12, 25)
days_left = (birthday - today).days
print(f"Days until Christmas: {days_left}")

# Exercise 2: math module
import math

numbers = [16, 25, 36, 49, 64, 81, 100]
print("\nSquare roots:")
for num in numbers:
    print(f"  √{num} = {math.sqrt(num):.1f}")

print(f"\nPi = {math.pi:.5f}")
print(f"E  = {math.e:.5f}")
print(f"log(100) = {math.log10(100)}")

# Exercise 3: random module
import random

print("\nRandom numbers:")
print(f"Integer 1-100: {random.randint(1, 100)}")
print(f"Float 0-1: {random.random():.4f}")

fruits = ["apple", "mango", "banana",
          "orange", "grapes"]
print(f"Random fruit: {random.choice(fruits)}")

random.shuffle(fruits)
print(f"Shuffled: {fruits}")

sample = random.sample(fruits, 3)
print(f"Random 3: {sample}")

# Exercise 4: os module
import os

print(f"\nCurrent directory: {os.getcwd()}")
print(f"Files here: {os.listdir('.')[:5]}")

# Create a folder
os.makedirs("test_folder", exist_ok=True)
print("Folder created!")

# Check if exists
print(f"Folder exists: {os.path.exists('test_folder')}")

# Exercise 5: sys module
import sys

print(f"\nPython version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Path separator: {os.sep}")