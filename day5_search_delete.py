# Day 5 - Search & Delete Contact

contacts = []

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

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
        search_name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"] == search_name:
                print("Found:", contact)
                found = True

        if not found:
            print("Contact not found!")

    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        for contact in contacts:
            if contact["name"] == delete_name:
                contacts.remove(contact)
                print("Deleted!")
                break
        else:
            print("Contact not found!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")