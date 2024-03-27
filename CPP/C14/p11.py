# multiple inheritance
class Father:
    def height(self):
        print('height is 6 foot')


class Mother:
    def color(self):
        print('color is white')


class Son(Father, Mother):
    pass


x = Son()
x.height()
x.color()