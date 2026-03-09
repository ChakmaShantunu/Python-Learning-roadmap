# Problem 1
# Print numbers from 1 to 10

for i in range(1,11): 
    print(i)

# Problem 2  
# Print even numbers from 1 to 20.    

for i in range(1, 21): 
    if(i % 2 == 0): 
        print(i)

# Problem 3  
# Take a number from the user and print numbers up to that number.   

user = int(input("Enter your number: "))
for i in range(1, user+1): 
    print(i)

# Problem 4
# Print odd numbers from 1 to 30

for i in range(1, 16):
    if(i % 2 != 0):
        print(i)  


# Problem 5 
# Find the sum of all numbers from 1 to 10       

sum = 0
for i in range(1, 11):
      sum += i
print(sum)