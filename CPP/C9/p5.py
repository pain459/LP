# Check if the number if prime or not using functions

def check_prime(n):
    x = 0
    for i in range(2, n):
        if n % i == 0:
            x = -1
            break
        else:
            x = 1
    return x


# Test if number is prime
num = int(input("Enter the number to check: "))
result = check_prime(num)

if result == -1:
    print(f'{num} is not prime.')
else:
    print(f'{num} is prime.')
