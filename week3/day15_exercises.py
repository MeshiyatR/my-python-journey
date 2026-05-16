# DAY 15 EXERCISES - 16th May 2026
# Topic: APIs and Requests Library

import requests
import json

# Exercise 1: Basic GET request
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(f"Status code: {response.status_code}")
print(f"Response type: {type(response.json())}")
data = response.json()
print(f"Post title: {data['title']}")
print(f"Post body: {data['body'][:50]}...")

# Exercise 2: Get multiple items
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
posts = response.json()

print(f"\nTotal posts: {len(posts)}")
print("\nFirst 3 posts:")
for post in posts[:3]:
    print(f"  ID: {post['id']} — {post['title'][:40]}")

# Exercise 3: Get with parameters
url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}
response = requests.get(url, params=params)
user_posts = response.json()

print(f"\nUser 1 posts: {len(user_posts)}")
for post in user_posts[:3]:
    print(f"  → {post['title'][:40]}")

# Exercise 4: Error handling with API
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/999",
    "https://jsonplaceholder.typicode.com/users/1"
]

for url in urls:
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"\n✓ Success: {url[-20:]}")
        else:
            print(f"\n✗ Failed: Status {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Connection error!")
    except requests.exceptions.Timeout:
        print("Request timed out!")

# Exercise 5: Working with users API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()

print(f"\nAll users:")
for user in users[:5]:
    print(f"  Name  : {user['name']}")
    print(f"  Email : {user['email']}")
    print(f"  City  : {user['address']['city']}")
    print(f"  Company: {user['company']['name']}")
    print("  " + "-" * 30)
