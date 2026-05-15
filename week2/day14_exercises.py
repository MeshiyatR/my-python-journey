# DAY 14 EXERCISES - 15th May 2026
# Topic: Decorators + Generators + Iterators

# Exercise 1: Basic Decorator
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello Meshiyat!")

say_hello()

# Exercise 2: Decorator with arguments
def bold_decorator(func):
    def wrapper(*args, **kwargs):
        print("=" * 30)
        result = func(*args, **kwargs)
        print("=" * 30)
        return result
    return wrapper

@bold_decorator
def greet(name, age):
    print(f"Name: {name}")
    print(f"Age : {age}")
    return "Done!"

greet("Meshiyat", 28)

# Exercise 3: Timer decorator
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end-start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def count_numbers():
    total = 0
    for i in range(1000000):
        total += i
    print(f"Sum: {total}")

count_numbers()

# Exercise 4: Basic Generator
def count_up(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

counter = count_up(1, 10)
print("\nGenerator output:")
for num in counter:
    print(num, end=" ")
print()

def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("\nFibonacci sequence:")
for num in fibonacci_generator(10):
    print(num, end=" ")
print()

# Exercise 5: Generator expressions
numbers = range(1, 21)

even_gen = (x for x in numbers if x % 2 == 0)
print("\nEven numbers from generator:")
for num in even_gen:
    print(num, end=" ")
print()

squares_gen = (x**2 for x in range(1, 11))
print("\nSquares from generator:")
for sq in squares_gen:
    print(sq, end=" ")
print()
