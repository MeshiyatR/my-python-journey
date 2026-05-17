# DAY 16 EXERCISES - 17th May 2026
# Topic: JSON and Data Handling

import json
import os

# Exercise 1: Basic JSON
# Convert dictionary to JSON string
person = {
    "name": "Meshiyat Rubab",
    "age": 28,
    "city": "Gilgit Baltistan",
    "skills": ["Python", "AI", "GitHub"],
    "goals": {
        "study": "Germany",
        "work": "Google"
    }
}

json_string = json.dumps(person)
print("JSON String:")
print(json_string)
print(f"Type: {type(json_string)}")

# Pretty print JSON
pretty_json = json.dumps(person, indent=4)
print("\nPretty JSON:")
print(pretty_json)

# Exercise 2: JSON to dictionary
json_data = '{"name": "Sara", "age": 22, "city": "Lahore"}'
dictionary = json.loads(json_data)
print(f"\nName: {dictionary['name']}")
print(f"Age: {dictionary['age']}")
print(f"Type: {type(dictionary)}")

# Exercise 3: Save JSON to file
students = [
    {"id": 1, "name": "Meshiyat",
     "marks": 95, "grade": "A"},
    {"id": 2, "name": "Sara",
     "marks": 78, "grade": "B"},
    {"id": 3, "name": "Ahmed",
     "marks": 88, "grade": "A"},
    {"id": 4, "name": "Bilal",
     "marks": 65, "grade": "C"}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)
print("\nStudents saved to students.json!")

# Exercise 4: Read JSON from file
with open("students.json", "r") as file:
    loaded_students = json.load(file)

print("\nLoaded from file:")
for student in loaded_students:
    print(f"  {student['name']}: "
          f"{student['marks']} ({student['grade']})")

# Exercise 5: Update JSON file
with open("students.json", "r") as file:
    data = json.load(file)

new_student = {
    "id": 5,
    "name": "Ayesha",
    "marks": 92,
    "grade": "A"
}
data.append(new_student)

with open("students.json", "w") as file:
    json.dump(data, file, indent=4)

print(f"\nUpdated! Total students: {len(data)}")
for student in data:
    print(f"  {student['id']}. {student['name']}")
