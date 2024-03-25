# A static method to find square root value
import math


class Sample:

    def __init__(self):
        self.y = 10

    # Static method
    @staticmethod
    def calculate(y):
        result = math.sqrt(y)
        return result

    def display(self):
        print(self.y)


# Accept a number from keyboard
n = float(input("Enter a number: "))
res = Sample.calculate(n)
print(f'Square root of {n} is {res}')
