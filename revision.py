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

num = int(input("Enter your first number: "))
num2 = int(input("Enter your second number"))
print(num + num2)

person = {
    "name" : "Rahim",
    "age" : 20,
    "city" : "Dhaka"
}
    
print(person["name"])

fruits = {
"apple":10,
"banana":5,
"mango":8
}

for fruit in fruits:
    print(fruit)
    
students = [
{"name":"Rahim","age":20},
{"name":"Karim","age":25}
]

print(students[0]["name"])    
print(students[1]["name"])

text = "Python"
for i in text: 
    print(i)

text2 = "I love Java"
print(text2.replace("Java", "Python"))     