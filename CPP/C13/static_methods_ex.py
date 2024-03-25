import math


class MathUtility:

    @staticmethod
    def square(num):
        return math.pow(num, 2)

    @staticmethod
    def is_even(num):
        return num % 2 == 0

    @staticmethod
    def fibonacci(limit):
        fib_series = [0, 1]
        while fib_series[-1] + fib_series[-2] < limit:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * (9 / 5)


print(f'Square of 1234 is {MathUtility.square(1234)}')
print(f'2343 is an even number? {MathUtility.is_even(2343)}')
print(f'Fibonacci series upto 1234 is {MathUtility.fibonacci(1234)}')
print(f'100 degrees in fahrenheit is {MathUtility.celsius_to_fahrenheit(100)}')
