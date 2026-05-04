#DAY 3 PROJECT - Smart Calculator
#4th May 2026

print("=" * 40)
print("    SMART CALCULLATOR")
print("=" * 40)

num1 = float(input("Enter first number: "))
operator = input("enter operator (+, -, *, /): ")
num2 = float(input("Enter second num: "))

if operator == "+":
    result = num1 = num2
    print(f"\n{num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"\n{num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"\n{num1} * {num2} = {result}")
elif operator == "/":
    if num2 == 0:
        print("\nError: Cannot divide by zero!")
else:
    result = num1 / num2
    print(f"\nInvalid operator!")

print("=" * 40)
print("Thank you for using Smart Calculator!")
print("=" * 40)