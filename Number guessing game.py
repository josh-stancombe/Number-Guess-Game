import random

minNumber = 1
maxNumber = 100
magicNumber = random.randint(minNumber , maxNumber)

found = False

message = "The magic number is between {0} and {1}"
print(message.format(minNumber , maxNumber), "\nCan you guess what it is?")

while not found:
    guess = int(input())

    if guess == magicNumber:
        print("You Got It!")
        found = True
        
    elif guess <  magicNumber:
        print("Too low")
        
    elif guess > magicNumber:
        print("Too High")
    
input("\nThanks for playing! - Press Return to exit")
exit()
