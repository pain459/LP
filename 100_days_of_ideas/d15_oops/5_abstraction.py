'''
Abstraction hides the complexity and only exposes the essential features of an object. Python uses abstract base classes (ABCs) to achieve this.
'''
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass


# Concrete class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.15 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    

# Using the subclasses
shapes = [Rectangle(5, 10), Circle(7)]
for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")


class Triangle(Shape):  # Forget to implement area and perimeter
    def __init__(self, base, height):
        self.base = base
        self.height = height

# Create an instance of Triangle
triangle = Triangle(10, 5)  # No error at this point
print(triangle.area())  # This will raise an AttributeError at runtime
