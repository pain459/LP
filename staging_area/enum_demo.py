from enum import Enum


# Define enum called color
class COLOR(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3


for i in COLOR:
    print(i)
print()
print(COLOR.RED)
print(COLOR.RED.value)
# Convert from value to enum number
color_value = 2
print(COLOR(color_value))