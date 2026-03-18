def calculator(a, b, op):
    if op == "+": 
        return(a + b)
    elif op == "-": 
        return(a - b)
    elif op == "*": 
        return(a * b)
    elif op == "/": 
        return(a / b)
    else: 
        return "Invalid"

num1 = int(input("Enter first number: "))    
num2 = int(input("Enter second number: "))
op = input("Enter operator: ")

result = calculator(num1, num2, op)
print("Result: ", result)    