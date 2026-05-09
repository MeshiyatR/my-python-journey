# DAY 8 PROJECT - Personal Diary App
# 9th May 2026

from datetime import datetime

def write_entry(entry):
    with open("my_diary.txt", "a") as file:
        date = datetime.now().strftime("%d-%m-%Y %H:%M")
        file.write("=" * 40 + "\n")
        file.write(f"Date: {date}\n")
        file.write(f"{entry}\n")
        file.write("=" * 40 + "\n")
    print("Entry saved successfully!")

def read_all_entries():
    try:
        with open("my_diary.txt", "r") as file:
            content = file.read()
            if content == "":
                print("No entries yet!")
            else:
                print(content)
    except FileNotFoundError:
        print("No diary found yet!")

def count_entries():
    try:
        with open("my_diary.txt", "r") as file:
            content = file.read()
            count = content.count("Date:")
            print(f"Total diary entries: {count}")
    except FileNotFoundError:
        print("No diary found yet!")

# Main program
print("=" * 40)
print("       MY PERSONAL DIARY")
print("=" * 40)

while True:
    print("\n1 - Write new entry")
    print("2 - Read all entries")
    print("3 - Count entries")
    print("4 - Quit")

    choice = input("\nEnter choice (1/2/3/4): ")

    if choice == "1":
        print("Write your diary entry:")
        entry = input("> ")
        write_entry(entry)

    elif choice == "2":
        print("\n--- MY DIARY ---")
        read_all_entries()

    elif choice == "3":
        count_entries()

    elif choice == "4":
        print("Goodbye! Keep writing!")
        break

    else:
        print("Invalid choice!")