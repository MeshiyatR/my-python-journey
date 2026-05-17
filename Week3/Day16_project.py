# DAY 16 PROJECT - Personal Data Manager
# 17th May 2026

import json
import os
from datetime import datetime

DATA_FILE = "personal_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {
        "profile": {},
        "goals": [],
        "skills": [],
        "daily_logs": []
    }

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
    print("Data saved successfully!")

def update_profile(data):
    print("\n" + "=" * 45)
    print("        UPDATE PROFILE")
    print("=" * 45)
    data["profile"]["name"] = input("  Name: ")
    data["profile"]["age"] = input("  Age: ")
    data["profile"]["city"] = input("  City: ")
    data["profile"]["goal"] = input("  Goal: ")
    data["profile"]["updated"] = datetime.now(
    ).strftime("%d-%m-%Y %H:%M")
    save_data(data)

def view_profile(data):
    print("\n" + "=" * 45)
    print("           MY PROFILE")
    print("=" * 45)
    if not data["profile"]:
        print("  No profile yet! Add one first.")
    else:
        for key, value in data["profile"].items():
            print(f"  {key.capitalize():<10}: {value}")
    print("=" * 45)

def add_goal(data):
    print("\n" + "=" * 45)
    print("           ADD GOAL")
    print("=" * 45)
    goal = input("  Enter your goal: ")
    deadline = input("  Deadline (DD-MM-YYYY): ")
    data["goals"].append({
        "goal": goal,
        "deadline": deadline,
        "status": "pending",
        "added": datetime.now().strftime(
            "%d-%m-%Y")
    })
    save_data(data)

def view_goals(data):
    print("\n" + "=" * 45)
    print("            MY GOALS")
    print("=" * 45)
    if not data["goals"]:
        print("  No goals yet!")
    else:
        for i, goal in enumerate(
                data["goals"], 1):
            status = "✅" if goal[
                "status"] == "completed" else "⏳"
            print(f"  {i}. {status} {goal['goal']}")
            print(f"     Deadline: {goal['deadline']}")
    print("=" * 45)

def add_skill(data):
    print("\n" + "=" * 45)
    print("           ADD SKILL")
    print("=" * 45)
    skill = input("  Skill name: ")
    level = input("  Level (beginner/intermediate"
                  "/advanced): ")
    data["skills"].append({
        "skill": skill,
        "level": level,
        "added": datetime.now().strftime(
            "%d-%m-%Y")
    })
    save_data(data)

def view_skills(data):
    print("\n" + "=" * 45)
    print("           MY SKILLS")
    print("=" * 45)
    if not data["skills"]:
        print("  No skills added yet!")
    else:
        for skill in data["skills"]:
            print(f"  → {skill['skill']:<20}"
                  f"Level: {skill['level']}")
    print("=" * 45)

def add_daily_log(data):
    print("\n" + "=" * 45)
    print("         ADD DAILY LOG")
    print("=" * 45)
    what_learned = input("  What did you learn: ")
    what_built = input("  What did you build: ")
    mood = input("  Mood (great/good/okay/bad): ")
    data["daily_logs"].append({
        "date": datetime.now().strftime(
            "%d-%m-%Y"),
        "learned": what_learned,
        "built": what_built,
        "mood": mood
    })
    save_data(data)

def view_logs(data):
    print("\n" + "=" * 45)
    print("          DAILY LOGS")
    print("=" * 45)
    if not data["daily_logs"]:
        print("  No logs yet!")
    else:
        for log in data["daily_logs"][-5:]:
            print(f"  Date   : {log['date']}")
            print(f"  Learned: {log['learned']}")
            print(f"  Built  : {log['built']}")
            print(f"  Mood   : {log['mood']}")
            print("  " + "-" * 35)
    print(f"  Total logs: {len(data['daily_logs'])}")
    print("=" * 45)

def show_summary(data):
    print("\n" + "=" * 45)
    print("        COMPLETE SUMMARY")
    print("=" * 45)
    name = data["profile"].get("name", "Unknown")
    print(f"  Name      : {name}")
    print(f"  Goals     : {len(data['goals'])}")
    print(f"  Skills    : {len(data['skills'])}")
    print(f"  Daily Logs: {len(data['daily_logs'])}")

    if data["goals"]:
        pending = [g for g in data["goals"]
                   if g["status"] == "pending"]
        completed = [g for g in data["goals"]
                     if g["status"] == "completed"]
        print(f"  Pending   : {len(pending)}")
        print(f"  Completed : {len(completed)}")
    print("=" * 45)

# Main program
data = load_data()

print("=" * 45)
print("      PERSONAL DATA MANAGER")
print("    All data saved in JSON! 💾")
print("=" * 45)

while True:
    print("\n1 - Update profile")
    print("2 - View profile")
    print("3 - Add goal")
    print("4 - View goals")
    print("5 - Add skill")
    print("6 - View skills")
    print("7 - Add daily log")
    print("8 - View daily logs")
    print("9 - Show summary")
    print("0 - Quit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        update_profile(data)
    elif choice == "2":
        view_profile(data)
    elif choice == "3":
        add_goal(data)
    elif choice == "4":
        view_goals(data)
    elif choice == "5":
        add_skill(data)
    elif choice == "6":
        view_skills(data)
    elif choice == "7":
        add_daily_log(data)
    elif choice == "8":
        view_logs(data)
    elif choice == "9":
        show_summary(data)
    elif choice == "0":
        print("Goodbye! Keep learning!")
        break
    else:
        print("Invalid choice!")
