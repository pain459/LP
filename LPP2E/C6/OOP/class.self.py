class Square:
    side = 8

    def area(self):
        return self.side ** 2


sq = Square()
print(sq.area())
print(Square.area(sq))

sq.side = 10
print(sq.area())
