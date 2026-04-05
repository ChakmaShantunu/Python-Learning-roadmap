try:
    num = int(input("Enter number: "))
    print(num)
except: 
    print("Invalid input")

try: 
    num2 = int(input("Enter number: "))
    print(num2)
except ValueError: 
    print("Please enter a number: ")        

try: 
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(a / b)
except ZeroDivisionError: 
    print("Cannot divided by zero")

try: 
    c = int("Enter a number: ")
    print(c)
except: 
    print("Error")
finally: 
    print("Program finished")            