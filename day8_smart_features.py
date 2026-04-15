# Day 8 - Smart Features

import json

try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except:
    contacts = []

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def is_duplicate(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return True
    return False

def valid_phone(phone):
    return phone.isdigit() and len(phone) >= 3

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        name = input("Enter name: ")

        if is_duplicate(name):
            print("⚠️ Contact already exists!")
            continue

        phone = input("Enter phone: ")

        if not valid_phone(phone):
            print("❌ Invalid phone number!")
            continue

        contacts.append({"name": name, "phone": phone})
        save_contacts()
        print("✅ Added!")

    elif choice == "2":
        search = input("Search name: ").lower()

        found = False
        for contact in contacts:
            if search in contact["name"].lower():
                print(contact)
                found = True

        if not found:
            print("❌ Not found")

    elif choice == "3":
        break