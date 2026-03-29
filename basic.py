print("hello world");
# name = input("Enter your name: ")
# age = input("Enter your age: ")
height = 5.6
isStudent = True
a = 5
b = 6

age = 30

if(age >= 18): print("You can vote")
else: print("You cannot vote")

# print("Hello", name)
# print(age)
print(height)
print(isStudent)
print(a > b)

# Day 2 python learning
for i in range(5): print("hello boss. welcome to python")
for i in range(5): print(i)
for i in range(1,11): print(i)

i = 5
while i <= 5: 
    print(i) 
    i = i + 1

total = 0

for i in range(1,6):
    total = total + i 
print(total)

for i in range(1, 11): 
    if(i % 2 ==0): 
        print(i)

numbers = [10, 20, 30]
print(numbers)

fruits = ["apple", "banana", "mango"]
print(fruits[0])       
print(fruits[1])       
print(fruits[2])     
print(len(fruits))


fruits.append("grapes")
print(fruits) 

fruits.remove("grapes")
print(fruits)

for fruit in fruits:
    print(fruit)   

def greet(): 
    print("Hello boss welcome to python")
greet()       
 
def greet(name): 
    print("Hello boss welcome to python", name)
greet("Shantunu")

def add(a, b):
    print(a + b)
add(5, 3) 
         
def add(a, b):
    return a + b
result = add(12, 3)
print(result)  

def print_numbers(n):
    for i in range(1, n+1):
        print(i)
        
print_numbers(5)  

student = {
    "name": "student",
    "age": 30,
    "city": "Rangamati"
}   
print(student)  
print(student["age"]) 
student["study"]= "BSS"
print(student)
student["age"] = 31
print(student)

for key, value in student.items(): 
    print(key, value)

students = [
    {"name":"Jenia", "age": 15},
    {"name":"Tiptip", "age": 12},
    {"name":"Choto", "age": 11},
]  
print(students)
print(students[0]["name"])
print(students[1]["name"])

for student in students:
    print(student["name"],"is", student["age"], "years old")

student = {
    "name": "Shantunu Chakma",
    "mark": [80, 85, 95]
}    
print(student["mark"])

for mark in student["mark"]:
    print(mark)

text = "   Python   "
print(text[0])    
print(text[1])    
print(text[2])
print(text[0:3])     
print(text[2:len(text)])
print(text.upper())  
print(text.lower())
print(text.strip())

text2 = "I love Java"
print(text2.replace("Java", "Python"))

text3 = "apple banana mango"
print(text3.split())

#Mini Project -- Basic Calculator

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# print("Add: ", num1 + num2)
# print("Sub: ", num1 - num2)
# print("Mul: ", num1 * num2)
# print("Div: ", num1 / num2)

#User choice add
op = input("Enter Operator (+, -, *, /): ")

if op == '+': 
    print(num1 + num2)
elif op == '-': 
    print(num1 - num2)    
elif op == '*': 
    print(num1 * num2)    
elif op == '/': 
    print(num1 / num2)
else: 
    print("Invalid Operator")   

fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)
fruits.insert(1, "pineaple")
print(fruits)
fruits.remove("pineaple")
print(fruits)
fruits.pop(1)
print(fruits)

numbers = [5, 1, 9, 3]
numbers.sort()
print(numbers)

text = "python"
print(text.upper())
print(text.lower())
print("py" in text)

name = input("Enter your name: ")
print(name.upper())

#tuple
numbers = (10, 20, 30)
print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[2])