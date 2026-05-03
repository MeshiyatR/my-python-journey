#DAY 2 PROJECT - Username Generator
#3rd May 2026

print("=" * 40) 
print("USERNAME GENERATOR")
print("=" * 40) 

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = input("Enter your birth year: ")

#Generate different usernames
username1 = first_name.lower() + last_name.lower()
username2 = first_name.lower() + birth_year
username3 = first_name[0]. lower() + last_name. lower() + birth_year
username4 = first_name. lower() + "_" + last_name.lower()

print("\n" + "=" * 40)
print("     YOUR USERNAME OPTIONS")
print("=" * 40)
print(f"   Otion 1: {username1}")
print(f"   Otion 2: {username2}")
print(f"   Otion 3: {username3}")
print(f"   Otion 4: {username4}")
print("=" * 40)
print(f"   Name length: {len(first_name + last_name)} characters")
print(f"   Uppercase:  {username1.upper()}")
print("=" * 40)