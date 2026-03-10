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

# Problem 6 
# Create a list:
# [5, 10, 15, 20]
# Use a loop to print all the numbers in the list.

numbers = [5, 10, 15, 20]

for number in numbers:
    print(number)

# Problem 7
# Given the list:
# [10, 20, 30, 40]
# Find the sum of all the numbers in the list.  

counts = [10, 20, 30, 40]
total = 0
for count in counts:
    total += count
print(total)    