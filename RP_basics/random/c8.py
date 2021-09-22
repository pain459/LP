# Conditional logic and workflow.
# python orders alphabets lexicographically.
# some samples.
# >>> "a" < "b"
# True
# >>> "apple" > "badgers"
# False
# >>> 1 <= 1
# True
# >>> 1 != 1
# False
# >>> 1 != 2
# True
# >>> "good" != "bad"
# True
# >>> "good!" != "Good"
# True
# >>> 123 == '123'
# False
# >>>

# logical operators and, or, not
import sys

print(False and True == False and True)  # Returns False
print((False and True) == (False and True))  # Returns True. Key is grouping.
print((1 <= 1) and (1 != 1))  # Returns False
print(not (1 != 2))  # returns false
print(("good" != "bad") or False)  # returns true
print(("good" != "Good") and not (1 == 1))  # returns false

# All below should be true.
print(False == (not True))
print((True and False) == (True and False))
print(not (True and ("A" == "B")))
print(("B" and not "A") != "B")

# control flow of your program.
# if keyword
if 2 * 2 == 4:
    print(f"2 and 2 is 4")

# else keyword
grade = 70
if grade > 70:
    print("Congratulations! You passed.")
else:
    print("Sorry, you failed!")

# elif keyword
grade = 69
if grade > 90:
    print("You won a gold medal!")
elif 80 <= grade < 90:
    print("You won silver medal!")
elif 70 <= grade < 80:
    print("You won bronze medal!")
else:
    print("You failed!")
print("Thanks for attending!")

# nested if statements.
sport = input("Enter the sport name: ")
score1 = eval(input("Enter the player 1 score: "))
score2 = eval(input("Enter the player 2 score: "))
if sport.lower() == 'basketball':
    if score1 > score2:
        print(f"Player1 won the game {sport}.")
    elif score2 > score1:
        print(f"Player 2 won the game {sport}.")
    else:
        print(f"Game draw!")
elif sport.lower() == 'tabletennis':
    if score1 > score2:
        print(f"Player1 won the game {sport}.")
    elif score2 > score1:
        print(f"Player 2 won the game {sport}.")
    else:
        print(f"Game draw!")
else:
    print("unknown game")

# simplifying the program with compound conditional statements
sport = input("Enter the sport name: ")
if sport.lower() == 'basketball' or sport.lower() == 'golf':
    score1 = eval(input("Enter the player 1 score: "))
    score2 = eval(input("Enter the player 2 score: "))
    if score1 == score2:
        print("Game draw")
    elif sport.lower() == 'basketball' or sport.lower() == 'golf':
        p1_wins_bb = sport == 'basketball' and score1 > score2
        p1_wind_tt = sport == 'golf' and score1 > score2
        p1_wins = p1_wins_bb or p1_wind_tt

        if p1_wins:
            print("Player1 won")
        else:
            print("Player2 won")
else:
    print("unknown sport")

# Challenge
# print out factors of the given number.
num = eval(input('Enter a positive integer to calculate the factors: '))
# one if block will come here to evaluate negative and float
# d = 1
for i in range(1, num + 1):
    if num % i == 0:
        print(f"{i} is a factor of {num}")

# Break out the pattern.
for i in range(0, 4):
    if i == 2:
        break
    print(i)
print(f"Finished with i = {i}")

# Continue skips the occurrence and move forward. We can call it like skipping.
for i in range(0, 4):
    if i == 2:
        continue
    print(i)
print(f"Finished with i = {i}")

# for...else loops. Rare use case, but they exist.
word = "university"
for i in word:
    if i == 'x':
        print("Found it!")
        break
else:
    print("The selected word is not in the phrase.")

# A zoo of exceptions.

# >>> int('z')
# Traceback (most recent call last):
#   File "<pyshell#26>", line 1, in <module>
#     int('z')
# ValueError: invalid literal for int() with base 10: 'z'
# >>> "1" + 2
# Traceback (most recent call last):
#   File "<pyshell#27>", line 1, in <module>
#     "1" + 2
# TypeError: can only concatenate str (not "int") to str
# >>> print(string1)
# Traceback (most recent call last):
#   File "<pyshell#28>", line 1, in <module>
#     print(string1)
# NameError: name 'string1' is not defined
# >>> 1 / 0
# Traceback (most recent call last):
#   File "<pyshell#29>", line 1, in <module>
#     1 / 0
# ZeroDivisionError: division by zero
# >>> pow(2.0, 1_000_000)
# Traceback (most recent call last):
#   File "<pyshell#30>", line 1, in <module>
#     pow(2.0, 1_000_000)
# OverflowError: (34, 'Result too large')
# >>>

# Here comes the exception handling.
# The try and expect keywords.

try:
    print(1 / 0)
except ZeroDivisionError:
    print("I'm limited by the technology of my time.")


# one more example
def division(x, y):
    try:
        print(x / y)  # try to perform this operation
    except (ValueError, ZeroDivisionError):  # Defining the expected errors
        print("Nope! That's not possible here.")  # print the message if encountered


division(1, 0)


# Telling what is wrong with exceptions.
def division(x, y):
    """This function will divide the numbers and return the errors if any."""
    try:
        print(x / y)
    except ZeroDivisionError:
        print("You cannot the divide the number by 0")
    except TypeError:
        print("Both inputs should be numbers")


# help(division)  # To get help of the function.
division(1, 0)

# Bare except clause
# This is an extreme wrong practice.
try:
    print("1" + 1)
except:
    print("Something wrong happened")

# Exercises.
while True:
    try:
        x = input("Enter a letter: ")
        if x.isalpha():
            print(f'You entered a letter {x}')
            print("Program completed")
            break
        else:
            raise ValueError
    except ValueError:
        print("Try again!")

# exercise 2
x = input("Enter the string: ")
y = input("Enter the number to display the index of the string: ")
try:
    if not x.isalpha():
        raise TypeError
    elif len(x) < int(y):
        raise IndexError
except ValueError:
    print("ValueError occurred")
except IndexError:
    print("IndexError occurred")
    print("Far shot!")
except TypeError:
    print("Type error occurred")
    print("Enter a valid string.")
else:
    print(f"String in index entered is {x[int(y)]}")

# Simulate events and calculate probabilities.
import random

print(random.randint(1, 10))

# Flipping fair coins.
import random


def coin_flip():
    """Randomly returns heads or tails"""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


heads = 0
tails = 0
for i in range(100_00):
    if coin_flip() == "heads":
        heads = heads + 1
    else:
        tails = tails + 1
print(f"Heads = {heads}")
print(f"Tails = {tails}")
print(f"Ratio of heads and tails is {heads / tails}")

# Flipping unfair coin (based on probability theory)

import random


def unfair_coin_flip(probability_of_tails):
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "heads"


heads = 0
tails = 0
for i in range(10000):
    if unfair_coin_flip(0.9) == "heads":
        heads = heads + 1
    else:
        tails = tails + 1

print(f"Heads = {heads}")
print(f"Tails = {tails}")
print(f"Ratio of heads and tails is {heads / tails}")

# roll dice experiment (fair way). Don't tamper the random function.

import random


def roll():
    if random.randint(1, 6) == 1:
        return "one"
    elif random.randint(1, 6) == 2:
        return "two"
    elif random.randint(1, 6) == 3:
        return "three"
    elif random.randint(1, 6) == 4:
        return "four"
    elif random.randint(1, 6) == 5:
        return "five"
    elif random.randint(1, 6) == 6:
        return "six"
    else:
        return "NA"


one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
for i in range(0, 500):
    if roll() == "one":
        one += 1
    elif roll() == "two":
        two += 1
    elif roll() == "three":
        three += 1
    elif roll() == "four":
        four += 1
    elif roll() == "five":
        five += 1
    else:
        six += 1
print(f"one:{one}, two:{two}, three:{three}, four:{four}, five:{five}, six:{six}")