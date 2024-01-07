# This is a number guessing game in Python.
# Create a random number between 1 - 10 (level 1 difficulty)
# Request user to provide an input and then give a hint based on the same.
# If correct, give a congratulations note and ask user option to exit or retry again of different level.

import random
import sys

_a = [1, -1000]
_b = [10, 100, 1000]
_exit_game = 1
while _exit_game != 0 :
    print("Welcome to the number guessing game. We have 3 levels of difficulty\n"
          "1 --> guess between 1 to 10\n"
          "2 --> guess between 1 to 100\n"
          "3 --> guess between -1000 to 1000\n")
    _level = int(input("Enter the level of difficulty: "))
    if _level not in [1, 2, 3]:
        print("Invalid choice! Program will now exit.")
        sys.exit(1)
    # _n = random.randint(1, 10)
    if _level == 1:
        _n = random.randint(_a[0], _b[0])
    elif _level == 2:
        _n = random.randint(_a[0], _b[1])
    elif _level == 3:
        _n = random.randint(_a[1], _b[2])
    print("The default range for this game is 1 to 10")
    print("The Random number is ", _n) # revealing the answer for testing.
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

    try:
        _continue = int(input("Enter 1 to continue, others to exit: "))
        if _continue == 1:
            print("Lets try your luck again. New game starts now.")
        else:
            print("Bye!")
            break
    except ValueError:
        print("Bye!")
        break
