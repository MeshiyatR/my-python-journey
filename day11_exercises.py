# DAY 11 EXERCISES - 12th May 2026
# Topic: Inheritance and Polymorphism

# Exercise 1: Basic Inheritance
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def introduce(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

    def introduce(self):
        super().introduce()
        print(f"I am a {self.breed} dog")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def meow(self):
        print(f"{self.name} says: Meow!")

    def introduce(self):
        super().introduce()
        print(f"I am a {self.color} cat")

dog = Dog("Bruno", 3, "German Shepherd")
cat = Cat("Whiskers", 2, "white")

dog.introduce()
dog.eat()
dog.bark()
print("---")
cat.introduce()
cat.sleep()
cat.meow()

# Exercise 2: Multilevel Inheritance
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university

    def study(self):
        print(f"{self.name} is studying at {self.university}")

class GraduateStudent(Student):
    def __init__(self, name, age, university, research):
        super().__init__(name, age, university)
        self.research = research

    def research_topic(self):
        print(f"{self.name} is researching: {self.research}")

grad = GraduateStudent("Meshiyat", 28,
                        "Virtual University",
                        "AI Engineering")
grad.introduce()
grad.study()
grad.research_topic()

# Exercise 3: Polymorphism
class Shape:
    def area(self):
        pass

    def describe(self):
        print(f"Area: {self.area()}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
for shape in shapes:
    print(f"{shape.__class__.__name__}: Area = {shape.area():.2f}")

# Exercise 4: Method Overriding
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        print(f"{self.brand} is moving at {self.speed} km/h")

    def describe(self):
        print(f"Vehicle: {self.brand}")

class Car(Vehicle):
    def move(self):
        print(f"{self.brand} car is driving at {self.speed} km/h")

class Boat(Vehicle):
    def move(self):
        print(f"{self.brand} boat is sailing at {self.speed} km/h")

class Airplane(Vehicle):
    def move(self):
        print(f"{self.brand} airplane is flying at {self.speed} km/h")

vehicles = [Car("Toyota", 120),
            Boat("Yamaha", 60),
            Airplane("Boeing", 900)]

for v in vehicles:
    v.move()

# Exercise 5: super() method
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name   : {self.name}")
        print(f"Salary : Rs {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Dept   : {self.department}")
        print(f"Bonus  : Rs {self.salary * 0.2:.0f}")

class Director(Manager):
    def __init__(self, name, salary, department, company):
        super().__init__(name, salary, department)
        self.company = company

    def display(self):
        super().display()
        print(f"Company: {self.company}")

director = Director("Meshiyat", 500000,
                    "AI Engineering", "Google")
director.display()