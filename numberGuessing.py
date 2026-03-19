import random

number = random.randint(1, 10)

while True:
    guess = int(input("Guess the number between(1 - 10): "))
    
    if guess == number: 
        print("You guessed it right")
        break
    elif guess > number: 
        print("Too high")    
    else: 
        print("Too low")    
