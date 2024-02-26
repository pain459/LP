# program to print prime numbers up to a given number.

x = int(input("You want primes. Up to what number? "))

for i in range(2, x+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)