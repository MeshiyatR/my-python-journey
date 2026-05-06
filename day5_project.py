# DAY 5 PROJECT - To Do List App 
# 6th May 2026

tasks = []

print("=" * 40)
print("         TO DO LIST APP")
print("=" * 40)

while True:
    print("\nWhat do you want to do?")
    print("1 - Add task")
    print("2 - View all tasks")
    print("3 - Remove task")
    print("4 - Quit")
    print("=" * 40)

choice = input("Enter your choice (1/2/3/4): ")

if choice == "1":
    task = input("Enter task")
    tasks.append(task)
    print(f"Task  '{task}' added successfully!")

elif choice == "2":
    if len(tasks) == 0:
        print("No tasks yet!")
    else:
        print("\nYour Task:")
        for i, task in enumerate(task, 1):
            print(f"{i}. {task}")
elif choice == "3":
    if len(tasks) == 0:
        print("No tasks to remove!")
    else:
        print("\nYour Task:")
        for i, task in enumerate(task, 1):
            print(f"{i}. {task}")
        num = int(input("Enter task number to remove: "))
        print(f"Task '{removed}' removed!")

elif choice == "4":
    print("Goodbye1 Keep being productive!")
    
else:
    print|("Invalid choice! Try again. ")