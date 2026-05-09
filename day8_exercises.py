# DAY 8 EXERCISES - 9th May 2026
# Topic: File Handling

# Exercise 1: Write to a file
file = open("my_notes.txt", "w")
file.write("My name is Meshiyat Rubab\n")
file.write("I am learning Python\n")
file.write("My goal is AI Engineering\n")
file.write("I want to study in Germany\n")
file.close()
print("File written successfully!")

# Exercise 2: Read from file
file = open("my_notes.txt", "r")
content = file.read()
file.close()
print("\nFile content:")
print(content)

# Exercise 3: Read line by line
file = open("my_notes.txt", "r")
print("Reading line by line:")
for line in file:
    print(line.strip())
file.close()

# Exercise 4: Append to file
file = open("my_notes.txt", "a")
file.write("Day 8 - Learning File Handling\n")
file.write("Every day I am getting better!\n")
file.close()
print("\nContent added successfully!")

# Exercise 5: Using 'with' statement
with open("my_notes.txt", "r") as file:
    lines = file.readlines()
    print(f"\nTotal lines in file: {len(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")