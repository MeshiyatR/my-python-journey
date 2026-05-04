#DAY 3 EXERCISE - 4TH May 2026
#Topic: Operators and Conditions

#Exercise 1: Arithmetic Operators
a = 20
b = 6

print(a + b)        #addition
print(a - b)        #subtraction
print(a * b)        #multiplication
print(a / b)        #division
print(a // b)       #floor division
print(a % b)        #remainder
print(a ** b)       #power


#Exercise 3: Simple if/else
age = int(input("Enter your age: "))
if age >= 18:
    print("You are an adult")
else:
    print("Your are a minor")


#Exercise 4: if/elif/else
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#Exercise 5: Logical Operators
username = input("Enter username: ")
password = input("Enter password: ")
if username == "Meshiyat" and password == "python123":
    print("Login successful!")
else:
    print("Wrong username or password!")
