"""
Inheritance allows one class (child) to reuse attributes and methods from other class (parent)
"""

class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self):
        return f"A shape of color {self.color}"
    
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
# Usage
circle = Circle("Red", 5)
print(circle.describe())
print(circle.area())

rect = Rectangle("Blue", 4, 4)
print(rect.describe())
print(rect.area())