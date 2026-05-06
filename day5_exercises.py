#DAY 5 EXERCISES - 6TH May 2026
#Topic: Lists

#Exercise 1: Create and print list
fruits = ["aaple", "banana", "mango", "orange", "grapes"]
print(fruits)
print(fruits[0])       #first item
print(fruits[-1])      #last item
print(fruits[1:3])     #slicing

#Exercise 2: List Methods
skills = ["Python", "AI", "GitHub", "Linkedin"]
skills.append("Google Cloud")
print(skills)
skills.remove("Linkedin")   #Fixed: remove actual item
print(skills)
print(len(skills))
print(skills.count("Python"))

#Exercise 3: Loop through Lists
goals = ["Learn Python", "Build AI apps", 
        "Study in Germany", "Work at Google"]

for goal in goals:
    print(f"My goal: {goal}")

#Exercise 4: Lists operations
numbers = [5, 2, 8, 1, 9, 3, 7,4,6]
print(f"Original: {numbers}")
print(f"SDorted: {sorted(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Sum: {sum(numbers)}")

#Exercise 5: Lists with user input
my_lists = []
print("Enter 5 items:")
for i in range(5):
    item = input(F"item{i+1}:")
    my_lists.append(item)
print(f"\nYour list: {my_lists}")
print(f"Total item: {len(my_lists)}")
