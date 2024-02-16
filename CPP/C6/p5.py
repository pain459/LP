# check if given number os even or odd

try:
    x = int(input("Enter an integer: "))
    if x % 2 == 0:
        print(f"{x} is even number.")
    else:
        print(f"{x} is odd number.")

except ValueError:
    print("Entered number is not an integer.")