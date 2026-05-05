#DAY 4 EXERCISES N- 5TH May 2026
#Topic: For Loop and While Loop 

#Exercise 1: Basic for loop
for i in range(1, 11):
    print(i) 

#Exercise 2: For loop with string
name = "Meshiyat"
for letter in name:
    print(letter)

#Exercise 3: Multiplication table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")

#Exercise 4: While loop
count = 1
while count <= 5:
    print(f"Count is :{count}")
    count += 1

#Exercise 5: While loop with user input
while True:
    answer = input("Type 'quit' to exit or anything to continue")
    print("Goodbye")
    break
else:
    print(F"You typed: {answer}")