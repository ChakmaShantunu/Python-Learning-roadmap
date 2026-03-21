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

try: 
    num2 = int(input("Enter number: "))
    print(num2)
except: 
    print("Error Occured")

finally: 
    print("Program Finished")                