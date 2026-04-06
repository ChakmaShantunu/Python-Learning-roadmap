
contacts = []

print("1. Add Contact")
print("2. View Contacts")
print("3. Exit")

name = input("Enter your name: ")
phone = int(input("Enter your number: "))

contact = {
    "name": name,
    "phone": phone
}

contacts.append(contact)
print("Data Saved")