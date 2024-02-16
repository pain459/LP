# Program to calculate if given number is in between 1 and 10 using if else

try:
    x = int(input("Enter an integer between 1 and 10: "))
    if 1 <= x <= 10:
        print("Entered value is in between 1 and 10.")
    else:
        print("So you are testing me. The entered number is not between 1 and 10.")

except ValueError:
    print("Invalid entry detected.")