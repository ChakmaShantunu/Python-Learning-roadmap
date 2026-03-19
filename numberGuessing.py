import random

number = random.randint(1, 10)

attempts = 5
    
for i in range(attempts): 
    guess = int(input("Guess the number between(1 - 10): "))
    
    if guess == number: 
        print("You guessed it right")
        break
    elif guess > number: 
        print("Too high")   
    else: 
        print("Too low")
    print("Chance left: ", attempts - 1 - i )  
    
else: 
    print("Game Over. The number was: ", number) 