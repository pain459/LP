# Overloading + operator to act on objects
class Bookx:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

class Booky:
    def __init__(self, pages):
        self.pages = pages


b1 = Bookx(100)
b2 = Booky(250)
print('Total pages = ', b1+b2)