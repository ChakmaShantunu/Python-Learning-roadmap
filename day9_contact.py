# Simple Contact Program

contacts = []

name = input("Enter name: ")
phone = input("Enter phone: ")

contacts.append({
    "name": name,
    "phone": phone
})

print("Saved Contacts:")
print(contacts)