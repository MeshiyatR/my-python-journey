# DAY 14 PROJECT - Smart Task Manager with Decorators
# 15th May 2026

import time
from datetime import datetime

# Decorators
def logger(func):
    def wrapper(*args, **kwargs):
        now = datetime.now().strftime("%H:%M:%S")
        print(f"[{now}] Running: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Completed in {end-start:.4f}s")
        return result
    return wrapper

def validator(func):
    def wrapper(task_name, *args, **kwargs):
        if len(task_name.strip()) == 0:
            print("Error: Task name cannot be empty!")
            return None
        if len(task_name) > 50:
            print("Error: Task name too long!")
            return None
        return func(task_name, *args, **kwargs)
    return wrapper

# Task Manager class
class SmartTaskManager:
    def __init__(self):
        self.tasks = []
        self.completed = []

    @logger
    @validator
    def add_task(self, task_name,
                 priority="medium"):
        task = {
            "name": task_name,
            "priority": priority,
            "created": datetime.now().strftime(
                "%d-%m-%Y %H:%M"),
            "status": "pending"
        }
        self.tasks.append(task)
        print(f"Task added: {task_name}")

    @logger
    def complete_task(self, task_name):
        for task in self.tasks:
            if task["name"].lower() == \
               task_name.lower():
                task["status"] = "completed"
                self.completed.append(task)
                self.tasks.remove(task)
                print(f"Task completed: {task_name}")
                return
        print(f"Task not found: {task_name}")

    @timer
    def display_tasks(self):
        print("\n" + "=" * 45)
        print("         PENDING TASKS")
        print("=" * 45)
        if not self.tasks:
            print("  No pending tasks!")
        else:
            high = [t for t in self.tasks
                    if t["priority"] == "high"]
            medium = [t for t in self.tasks
                      if t["priority"] == "medium"]
            low = [t for t in self.tasks
                   if t["priority"] == "low"]

            if high:
                print("  🔴 HIGH PRIORITY:")
                for t in high:
                    print(f"     → {t['name']}")
            if medium:
                print("  🟡 MEDIUM PRIORITY:")
                for t in medium:
                    print(f"     → {t['name']}")
            if low:
                print("  🟢 LOW PRIORITY:")
                for t in low:
                    print(f"     → {t['name']}")

        print(f"\n  Pending  : {len(self.tasks)}")
        print(f"  Completed: {len(self.completed)}")
        print("=" * 45)

    def task_generator(self):
        for task in self.tasks:
            yield task

# Main program
manager = SmartTaskManager()

print("=" * 45)
print("    SMART TASK MANAGER")
print("    With Decorators + Generators")
print("=" * 45)

manager.add_task("Learn Python Decorators", "high")
manager.add_task("Build AI Project", "high")
manager.add_task("Upload to GitHub", "medium")
manager.add_task("Post on LinkedIn", "medium")
manager.add_task("Read Python docs", "low")

while True:
    print("\n1 - View all tasks")
    print("2 - Add new task")
    print("3 - Complete a task")
    print("4 - Show tasks one by one")
    print("5 - Quit")

    choice = input("\nEnter choice: ")

    if choice == "1":
        manager.display_tasks()

    elif choice == "2":
        name = input("Task name: ")
        print("Priority: 1-High 2-Medium 3-Low")
        p = input("Choose: ")
        priority = ("high" if p == "1"
                    else "medium" if p == "2"
                    else "low")
        manager.add_task(name, priority)

    elif choice == "3":
        name = input("Task name to complete: ")
        manager.complete_task(name)

    elif choice == "4":
        print("\nTasks one by one:")
        for task in manager.task_generator():
            print(f"→ {task['name']} "
                  f"({task['priority']})")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
