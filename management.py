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
        marks = int(input("Enter mark: "))
        
        student = {
            name: name,
            marks: marks
        }
        students.append(student)
        print("Students added")
    
    elif choice == "2": 
        for s in students: 
            print(s["name"], s["marks"])   
             
    elif choice == "3": 
        total = 0
        for s in students: 
            total += s["marks"]
            
        if len(students) > 0: 
            print("Average:", total/len(students))  
        else: 
            print("No data")     
    