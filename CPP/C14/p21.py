# Overloading > operator
class Fire:
    def __init__(self, pages):
        self.pages = pages

    def __gt__(self, other):
        return self.pages > other.pages


class Leaf:
    def __init__(self, pages):
        self.pages = pages


b1 = Fire(1500)
b2 = Leaf(3500)
if b1 > b2:
    print('Fire')
else:
    print('Leaf')
