a = 15
b = 30
print(a + b)
print(a - b)
print(a * b)
print(a / b)

name = input("Enter your name: ")
print("Hello", name)

number = int(input("Enter your number: "))
if number % 2 == 0: 
    print("Even")
else: 
    print("Odd")

number2 = int(input("Enter your number: "))
if number2 > 0: 
    print("Positive")
else: 
    print("Negative")

number3 = int(input("Enter your number: "))
if number3 > 15: 
    print("Greater than 10")
else: 
    print("Not greater than 10")           
        

for i in range(1, 11): 
    print(i)
    
def add(a, b):
    print(a + b)
add(5, 6)        