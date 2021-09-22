class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


square = Square(4)

print(square.area())