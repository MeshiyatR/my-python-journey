# DAY 6 EXERCISES - 7th May 2026
# Topic: Tuples and Dictionaries

# Exercise 1: Tuples
countries = ("Germany", "Poland", "Finland",
             "UK", "Australia")
print(countries)
print(countries[0])
print(countries[-1])
print(len(countries))

# Exercise 2: Loop through tuple
print("\nCountries I want to visit:")
for country in countries:
    print(f"→ {country}")

# Exercise 3: Basic dictionary
person = {
    "name": "Meshiyat Rubab",
    "age": 28,
    "city": "Lahore",
    "goal": "AI Engineer",
    "skill": "Python"
}
print(person)
print(person["name"])
print(person["goal"])

# Exercise 4: Dictionary methods
print(person.keys())
print(person.values())
print(person.items())

# Loop through dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Exercise 5: Update dictionary
person["skill"] = "Python + AI Engineering"
person["dream"] = "Work at Google"
print(person)
print(f"Updated skill: {person['skill']}")