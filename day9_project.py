# DAY 9 PROJECT - Safe Bank Account
# 10th May 2026

import random

def generate_account_number():
    return random.randint(10000000, 99999999)

def deposit(balance, amount):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        balance += amount
        print(f"Successfully deposited Rs {amount:.2f}")
        return balance
    except ValueError as e:
        print(f"Error: {e}")
        return balance

def withdraw(balance, amount):
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive!")
        if amount > balance:
            raise ValueError("Insufficient balance!")
        balance -= amount
        print(f"Successfully withdrawn Rs {amount:.2f}")
        return balance
    except ValueError as e:
        print(f"Error: {e}")
        return balance

def show_balance(balance, name):
    print("\n" + "=" * 40)
    print("        ACCOUNT SUMMARY")
    print("=" * 40)
    print(f"  Account Holder : {name}")
    print(f"  Balance        : Rs {balance:.2f}")
    print("=" * 40)

# Main program
print("=" * 40)
print("      SAFE BANK ACCOUNT APP")
print("=" * 40)

name = input("Enter your name: ")
account = generate_account_number()
balance = 0.0

print(f"\nWelcome {name}!")
print(f"Your account number: {account}")

while True:
    print("\n1 - Deposit")
    print("2 - Withdraw")
    print("3 - Check balance")
    print("4 - Quit")

    choice = input("\nEnter choice (1/2/3/4): ")

    if choice == "1":
        amount = input("Enter deposit amount: Rs ")
        balance = deposit(balance, amount)

    elif choice == "2":
        amount = input("Enter withdrawal amount: Rs ")
        balance = withdraw(balance, amount)

    elif choice == "3":
        show_balance(balance, name)

    elif choice == "4":
        show_balance(balance, name)
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice!")