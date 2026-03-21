# num = int(input("Enter number: "))
# print(num)

#Solution

try: 
    num = int(input("Enter number: "))
    print(10/num)
    
except ValueError: 
    print("Please enter a number")  

except ZeroDivisionError: 
    print("Cannot divide by zero")      