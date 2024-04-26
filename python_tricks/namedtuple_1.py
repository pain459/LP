# Python program to create simple classes with named tuple.
from collections import namedtuple

# Create a point class using named tuple
Point = namedtuple('Point', ['x', 'y'])

# Create a point instances
p = Point(3, 4)

# Access fields by name
print(f"X coordinate is {p.x}")
print(f"Y coordinate is {p.y}")
