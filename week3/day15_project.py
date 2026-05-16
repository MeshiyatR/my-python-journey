# DAY 15 PROJECT - World Information App
# 16th May 2026

import requests
import json
from datetime import datetime

def get_joke():
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            joke = response.json()
            print("\n" + "=" * 45)
            print("          RANDOM JOKE")
            print("=" * 45)
            print(f"  Setup    : {joke['setup']}")
            print(f"  Punchline: {joke['punchline']}")
            print("=" * 45)
        else:
            print("Could not fetch joke!")
    except Exception as e:
        print(f"Error: {e}")

def get_user_info(user_id):
    try:
        url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            user = response.json()
            print("\n" + "=" * 45)
            print("          USER INFORMATION")
            print("=" * 45)
            print(f"  Name    : {user['name']}")
            print(f"  Username: {user['username']}")
            print(f"  Email   : {user['email']}")
            print(f"  Phone   : {user['phone']}")
            print(f"  City    : {user['address']['city']}")
            print(f"  Company : {user['company']['name']}")
            print(f"  Website : {user['website']}")
            print("=" * 45)
        else:
            print(f"User {user_id} not found!")
    except Exception as e:
        print(f"Error: {e}")

def get_posts(user_id):
    try:
        url = "https://jsonplaceholder.typicode.com/posts"
        params = {"userId": user_id}
        response = requests.get(url,
                                params=params,
                                timeout=5)
        if response.status_code == 200:
            posts = response.json()
            print("\n" + "=" * 45)
            print(f"     POSTS BY USER {user_id}")
            print("=" * 45)
            for i, post in enumerate(posts[:5], 1):
                print(f"  {i}. {post['title'][:40]}")
            print(f"\n  Total posts: {len(posts)}")
            print("=" * 45)
        else:
            print("Could not fetch posts!")
    except Exception as e:
        print(f"Error: {e}")

def get_todos(user_id):
    try:
        url = "https://jsonplaceholder.typicode.com/todos"
        params = {"userId": user_id}
        response = requests.get(url,
                                params=params,
                                timeout=5)
        if response.status_code == 200:
            todos = response.json()
            completed = [t for t in todos
                        if t["completed"]]
            pending = [t for t in todos
                      if not t["completed"]]

            print("\n" + "=" * 45)
            print(f"     TODOS FOR USER {user_id}")
            print("=" * 45)
            print(f"  Total     : {len(todos)}")
            print(f"  Completed : {len(completed)}")
            print(f"  Pending   : {len(pending)}")
            print("\n  Pending tasks:")
            for todo in pending[:3]:
                print(f"  ✗ {todo['title'][:40]}")
            print("\n  Completed tasks:")
            for todo in completed[:3]:
                print(f"  ✓ {todo['title'][:40]}")
            print("=" * 45)
        else:
            print("Could not fetch todos!")
    except Exception as e:
        print(f"Error: {e}")

def check_api_status():
    apis = {
        "JSONPlaceholder": "https://jsonplaceholder.typicode.com/posts/1",
        "Joke API": "https://official-joke-api.appspot.com/random_joke"
    }

    print("\n" + "=" * 45)
    print("        API STATUS CHECK")
    print("=" * 45)
    for name, url in apis.items():
        try:
            response = requests.get(url, timeout=5)
            status = "✓ Online" if response.status_code == 200 else "✗ Error"
            print(f"  {name:<20}: {status}")
        except:
            print(f"  {name:<20}: ✗ Offline")
    print("=" * 45)

# Main program
print("=" * 45)
print("      WORLD INFORMATION APP")
print("    Powered by Real APIs! 🌐")
print("=" * 45)

while True:
    print("\n1 - Get random joke")
    print("2 - Get user information")
    print("3 - Get user posts")
    print("4 - Get user todos")
    print("5 - Check API status")
    print("6 - Quit")

    choice = input("\nEnter choice (1/2/3/4/5/6): ")

    if choice == "1":
        get_joke()

    elif choice == "2":
        try:
            user_id = int(input("Enter user ID (1-10): "))
            get_user_info(user_id)
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "3":
        try:
            user_id = int(input("Enter user ID (1-10): "))
            get_posts(user_id)
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "4":
        try:
            user_id = int(input("Enter user ID (1-10): "))
            get_todos(user_id)
        except ValueError:
            print("Please enter a valid number!")

    elif choice == "5":
        check_api_status()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
