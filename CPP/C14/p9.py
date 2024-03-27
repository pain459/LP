# Accessing base class constructor and method in the sub class
class Square:
    def __init__(self, x):
        self.x = x

    def area(self):
        print(f'Area of square = {self.x * self.x}')


class Rectangle(Square):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def area(self):
        super().area()
        print(f'Area of rectangle = {self.x * self.y}')


# Find areas of square and rectangle
a, b = [float(x) for x in input("Enter two measurements: ").split()]
r = Rectangle(a, b)
r.area()
