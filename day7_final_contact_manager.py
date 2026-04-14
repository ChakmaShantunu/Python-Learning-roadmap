# Day 7 - Final Contact Manager with File Save

import json

# Load contacts from file
try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except:
    contacts = []

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

while True:
    print("\n===== Contact Manager =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Update Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")

        contact = {
            "name": name,
            "phone": phone
        }

        contacts.append(contact)
        save_contacts()
        print("✅ Contact Added!")

    elif choice == "2":
        print("\n📋 Contact List:")
        if len(contacts) == 0:
            print("No contacts found!")
        else:
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")

    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"] == search_name:
                print("🔍 Found:", contact)
                found = True

        if not found:
            print("❌ Contact not found!")

    elif choice == "4":
        delete_name = input("Enter name to delete: ")

        for contact in contacts:
            if contact["name"] == delete_name:
                contacts.remove(contact)
                save_contacts()
                print("🗑️ Deleted!")
                break
        else:
            print("❌ Contact not found!")

    elif choice == "5":
        update_name = input("Enter name to update: ")
        found = False

        for contact in contacts:
            if contact["name"] == update_name:
                new_name = input("Enter new name: ")
                new_phone = input("Enter new phone: ")

                contact["name"] = new_name
                contact["phone"] = new_phone

                save_contacts()
                print("✏️ Contact Updated!")
                found = True
                break

        if not found:
            print("❌ Contact not found!")

    elif choice == "6":
        print("💾 Data saved. Goodbye!")
        break

    else:
        print("❌ Invalid choice!")