# Day 2 - Multiple Contact Add

contacts = []

for i in range(3):
    print("Add Contact", i+1)

    name = input("Enter name: ")
    phone = input("Enter phone: ")

    contact = {
        "name": name,
        "phone": phone
    }

    contacts.append(contact)

print("All Contacts:")
print(contacts)