# DAY 10 EXERCISES - 11th May 2026
# Topic: Object Oriented Programming

# Exercise 1: Basic class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")
        print(f"My grade is {self.grade}")

# Create objects
student1 = Student("Meshiyat", 28, "A")
student2 = Student("Sara", 22, "B")

student1.introduce()
print("---")
student2.introduce()

# Exercise 2: Class with methods
class Calculator:
    def __init__(self, name):
        self.name = name
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def show_history(self):
        print(f"\n{self.name} History:")
        for item in self.history:
            print(f"  {item}")

calc = Calculator("My Calculator")
print(calc.add(10, 5))
print(calc.subtract(20, 8))
print(calc.add(100, 200))
calc.show_history()

# Exercise 3: Class attributes
class Phone:
    brand = "Samsung"  # class attribute

    def __init__(self, model, price):
        self.model = model  # instance attribute
        self.price = price

    def display(self):
        print(f"Brand: {Phone.brand}")
        print(f"Model: {self.model}")
        print(f"Price: Rs {self.price}")

phone1 = Phone("Galaxy S24", 150000)
phone2 = Phone("Galaxy A54", 80000)
phone1.display()
print("---")
phone2.display()

# Exercise 4: Class with validation
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs {amount}")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid amount!")
        else:
            self.balance -= amount
            print(f"Withdrawn Rs {amount}")

    def show_balance(self):
        print(f"{self.owner}'s balance: Rs {self.balance}")

account = BankAccount("Meshiyat", 5000)
account.show_balance()
account.deposit(3000)
account.withdraw(2000)
account.withdraw(10000)
account.show_balance()

# Exercise 5: Multiple objects
class Employee:
    company = "MyTech"

    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary

    def display(self):
        print(f"Company : {Employee.company}")
        print(f"Name    : {self.name}")
        print(f"Role    : {self.role}")
        print(f"Salary  : Rs {self.salary}")
        print("-" * 30)

emp1 = Employee("Meshiyat", "AI Engineer", 150000)
emp2 = Employee("Sara", "Python Developer", 120000)
emp3 = Employee("Ahmed", "Data Scientist", 180000)

emp1.display()
emp2.display()
emp3.display()