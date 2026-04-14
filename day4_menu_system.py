# Day 4 - Menu System

contacts = []

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")

        contact = {
            "name": name,
            "phone": phone
        }

        contacts.append(contact)
        print("Contact Added!")

    elif choice == "2":
        print("Contact List:")

        for contact in contacts:
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("------")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")