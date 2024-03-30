# Method overriding
import math
class Square:
    def area(self, x):
        print(f'Square area {x * x}')

class Circle:
    def area(self, x):
        print(f'Circle area {math.pi * x * x}')


x = Circle()
x.area(12)