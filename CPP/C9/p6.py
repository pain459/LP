# Function to check whether the number is prime or not.
from p5 import check_prime

# Generate prime number series
num = int(input("How many primes do you want? "))
i = 2  # start with i value 2
c = 1  # this counts the number of primes
while True:
    if check_prime(i) not in [-1, -2]:
        print(i)
        c += 1
    i += 1
    if c > num:
        break
