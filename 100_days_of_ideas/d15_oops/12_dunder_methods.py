"""
Dunder methods allow objects to interact with Python's built-in operations, such as arithmetic, comparison, and string representation.

Common Dunder Methods:
__init__: Initialize an object.
__str__: String representation (used in print()).
__repr__: Developer-friendly representation.
__add__: Define + operator behavior.
__eq__: Define equality (==).
__len__: Define behavior of len().
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    

p1 = Point(2, 3)
p2 = Point(4, 3)
p3 = p1 + p2  # Uses __add__
print(p3)
