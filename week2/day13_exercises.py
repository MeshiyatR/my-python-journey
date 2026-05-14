# DAY 13 EXERCISES - 14th May 2026
# Topic: List Comprehensions + Lambda + Map/Filter

# Exercise 1: Basic List Comprehension
# Old way
squares_old = []
for i in range(1, 11):
    squares_old.append(i ** 2)
print(f"Old way: {squares_old}")

# New way - List Comprehension
squares_new = [i ** 2 for i in range(1, 11)]
print(f"New way: {squares_new}")

# More examples
evens = [i for i in range(1, 21) if i % 2 == 0]
print(f"Even numbers: {evens}")

words = ["python", "ai", "google", "germany"]
upper_words = [word.upper() for word in words]
print(f"Uppercase: {upper_words}")

lengths = [len(word) for word in words]
print(f"Lengths: {lengths}")

# Exercise 2: List Comprehension with condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15]

divisible_by_3 = [n for n in numbers if n % 3 == 0]
print(f"Divisible by 3: {divisible_by_3}")

greater_than_10 = [n for n in numbers if n > 10]
print(f"Greater than 10: {greater_than_10}")

even_squares = [n**2 for n in numbers if n % 2 == 0]
print(f"Even squares: {even_squares}")

# Exercise 3: Lambda functions
# Old way
def add(a, b):
    return a + b

# Lambda way
add_lambda = lambda a, b: a + b
print(f"\nAdd: {add_lambda(10, 20)}")

multiply = lambda x, y: x * y
print(f"Multiply: {multiply(5, 6)}")

square = lambda x: x ** 2
print(f"Square of 7: {square(7)}")

greet = lambda name: f"Hello {name}!"
print(greet("Meshiyat"))

is_even = lambda n: n % 2 == 0
print(f"Is 8 even: {is_even(8)}")
print(f"Is 7 even: {is_even(7)}")

# Exercise 4: Map function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = list(map(lambda x: x**2, numbers))
print(f"\nSquared: {squared}")

doubled = list(map(lambda x: x*2, numbers))
print(f"Doubled: {doubled}")

names = ["meshiyat", "sara", "ahmed", "bilal"]
capitalized = list(map(lambda n: n.capitalize(), names))
print(f"Capitalized: {capitalized}")

# Exercise 5: Filter function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\nEvens: {evens}")

greater_10 = list(filter(lambda x: x > 10, numbers))
print(f"Greater than 10: {greater_10}")

names = ["Ali", "Sara", "Muhammad", "A", "Bob",
         "Meshiyat", "Jo"]
long_names = list(filter(lambda n: len(n) > 3, names))
print(f"Long names: {long_names}")
