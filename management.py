students = []

while True: 
    print("\n1. add students")
    print("2. view students")
    print("3. average marks")
    print("4. top students")
    print("5. exist")
    
    choice = input("Enter choice: ")
    
    if choice == "1": 
        name = input("Enter name: ")
        mark = int(input("Enter mark: "))
        
        student = {
            name: name,
            mark: mark
        }
        students.append(student)
        print("Students added")
    
    elif choice == "2": 
        for s in students: 
            print(s[name], s[mark])    
    