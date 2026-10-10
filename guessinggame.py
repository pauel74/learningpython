import random
import os

clear = lambda: os.system('clear')

target = random.randint(0, 100)
guess = 11

print("Input a random number (0-100)")

while guess != target:
    guess = int(input())
    clear()
    if guess != target:
        print("wrong number, try again")
        if guess > target:
            print("hint: the number is lower " + str(guess))
        else:
            print("hint: the number is higher than " + str(guess))
    else:
        print("you won! the number was " + str(target))
    
