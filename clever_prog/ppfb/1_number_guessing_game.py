# This is a number guessing game in Python.
# Create a random number between 1 - 10 (level 1 difficulty)
# Request user to provide an input and then give a hint based on the same.
# If correct, give a congratulations note and ask user option to exit or retry again of different level.

import random

_n = random.randint(1, 10)

print("The default range for this game is 1 to 10")
print("The Random number is ", _n)
_guess = int(input("Enter a number you are guessing in range: "))
while _guess != _n:
    if _guess < _n:
        print("Too low!")
        _guess = int(input("Enter again: "))
    elif _guess > _n:
        print("Too high!")
        _guess = int(input("Enter again: "))
    else:
        break
print("You guessed it right! You won!")
