# DAY 5 PROJECT - To Do List App 
# 6th May 2026

tasks = []

print("=" * 40)
print("       TO DO LIST APP")
print("=" * 40)

while True:
    print("\n1 - Add tas")
    print("2 - View all tasks")
    print("3 - Remove task")
    print("4 - Quit")

    choice = input("Enter task: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks yet!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove!")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
                num = int(input("Enter task number: "))
                removed = tasks.pop(num - 1)
                print(f"Task '{removed}' removed!")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
    