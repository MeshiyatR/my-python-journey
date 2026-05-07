# DAY 6 PROJECT - Simple Contact Book
# 7th May 2026

contacts = {
    "Hina": "923456789",
    "Ali": "9298765432",
    "Hira": "943536366",
    "hasan": "9000004345",
    "umar": "9521111999"
}

print("=" * 40)
print("        CONTACT BOOK")
print("=" * 40)

while True:
    print("\n1 - Search contact")
    print("2 - View all contacts")
    print("3 - Add contact")
    print("4 - Quit")

    choice = input("\nEnter choice (1/2/3/4): ")

    if choice == "1":
        name = input("Enter name to search: ")
        if name in contacts:
            print(f"✓ Found! {name}: {contacts[name]}")
        else:
            print(f"✗ '{name}' not found in contacts!")

    elif choice == "2":
        print("\nAll Contacts:")
        print("-" * 40)
        for name, phone in contacts.items():
            print(f"  {name}: {phone}")

    elif choice == "3":
        new_name = input("Enter name: ")
        new_phone = input("Enter phone: ")
        contacts[new_name] = new_phone
        print(f"✓ {new_name} added successfully!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")