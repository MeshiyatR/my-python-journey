# DAY 12 PROJECT - Personal Life Dashboard
# 13th May 2026

from datetime import datetime, date
import math
import random
import os

def show_datetime_info():
    now = datetime.now()
    today = date.today()
    print("=" * 45)
    print("         DATE AND TIME INFO")
    print("=" * 45)
    print(f"  Date     : {now.strftime('%d %B %Y')}")
    print(f"  Time     : {now.strftime('%I:%M %p')}")
    print(f"  Day      : {now.strftime('%A')}")
    print(f"  Week No  : {now.strftime('%W')}")
    print("=" * 45)

def calculate_age():
    print("\n" + "=" * 45)
    print("          AGE CALCULATOR")
    print("=" * 45)
    try:
        year = int(input("  Enter birth year: "))
        month = int(input("  Enter birth month: "))
        day = int(input("  Enter birth day: "))
        birthday = date(year, month, day)
        today = date.today()
        age = today.year - birthday.year
        if today < date(today.year,
                        birthday.month,
                        birthday.day):
            age -= 1
        days_lived = (today - birthday).days
        next_birthday = date(today.year,
                             birthday.month,
                             birthday.day)
        if next_birthday < today:
            next_birthday = date(today.year + 1,
                                 birthday.month,
                                 birthday.day)
        days_to_birthday = (next_birthday - today).days
        print(f"  Age            : {age} years")
        print(f"  Days lived     : {days_lived:,}")
        print(f"  Next birthday  : {days_to_birthday} days")
        print("=" * 45)
    except ValueError:
        print("  Invalid date entered!")

def math_toolkit():
    print("\n" + "=" * 45)
    print("           MATH TOOLKIT")
    print("=" * 45)
    try:
        num = float(input("  Enter a number: "))
        print(f"  Square root  : {math.sqrt(abs(num)):.4f}")
        print(f"  Square       : {num ** 2:.4f}")
        print(f"  Cube         : {num ** 3:.4f}")
        print(f"  Log10        : {math.log10(abs(num)):.4f}"
              if num > 0 else "  Log10: N/A")
        print(f"  Ceiling      : {math.ceil(num)}")
        print(f"  Floor        : {math.floor(num)}")
        print("=" * 45)
    except ValueError:
        print("  Invalid number!")

def motivation_generator():
    quotes = [
        "Every expert was once a beginner!",
        "Code today. Change the world tomorrow.",
        "One day or day one. You decide.",
        "The best time to start was yesterday.",
        "Keep going. You are closer than you think.",
        "Dream big. Start small. Act now.",
        "Your only limit is your mind.",
        "Success is built one day at a time."
    ]
    print("\n" + "=" * 45)
    print("       MOTIVATION FOR TODAY")
    print("=" * 45)
    print(f"  {random.choice(quotes)}")
    print("=" * 45)

def save_daily_note():
    print("\n" + "=" * 45)
    print("         SAVE DAILY NOTE")
    print("=" * 45)
    note = input("  Write your note: ")
    now = datetime.now()
    filename = "daily_notes.txt"
    with open(filename, "a") as file:
        file.write("=" * 40 + "\n")
        file.write(f"Date: {now.strftime('%d-%m-%Y %H:%M')}\n")
        file.write(f"Note: {note}\n")
    print(f"  Note saved to {filename}!")
    print("=" * 45)

# Main program
print("=" * 45)
print("      PERSONAL LIFE DASHBOARD")
print("=" * 45)

while True:
    print("\n1 - Date and time info")
    print("2 - Age calculator")
    print("3 - Math toolkit")
    print("4 - Daily motivation")
    print("5 - Save daily note")
    print("6 - Quit")

    choice = input("\nEnter choice (1/2/3/4/5/6): ")

    if choice == "1":
        show_datetime_info()
    elif choice == "2":
        calculate_age()
    elif choice == "3":
        math_toolkit()
    elif choice == "4":
        motivation_generator()
    elif choice == "5":
        save_daily_note()
    elif choice == "6":
        print("Goodbye! Have a great day!")
        break
    else:
        print("Invalid choice!")