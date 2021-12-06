import math
def prime_checker(number):
    for i in range(2, math.ceil(number / 2) + 1):
        if number % i == 0:
            print("It's not a prime number.")
            break
    else:
        print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)