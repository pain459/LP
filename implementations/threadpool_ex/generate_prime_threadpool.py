# Generate prime numbers using Fremats Little theorem.
# We will utilize the threadpool for executing these jobs.
# Fermats theorem a ** n-1 % n = 1
# If n is a prime number, then for every a, 1 ≤ a < n,

import random


def is_prime(n, k=5):
    # Test if number is prime using Fermats Little theorem
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    for _ in range(k):
        a = random.randint(2, n - 1) # The range can be from 1 as well.
        if pow(a, n - 1, n) != 1:
            return False
    return True


def generate_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


def main():
    # n = 133421334
    # result = is_prime(n)
    # if result:
    #     print(f'{n} is a prime number.')
    # else:
    #     print(f'{n} is not a prime number.')

    generated_primes = generate_primes(2, 331)
    print(generated_primes)


if __name__ == "__main__":
    main()
