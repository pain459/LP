# Overriding base class constructor and method in sub class
class Father:
    def __init__(self):
        self.property = 8000000

    def display_property(self):
        print(f'Fathers property is {self.property}')


class Son(Father):
    def __init__(self):
        self.property = 1000000

    def display_property(self):
        print(f'Sons property is {self.property}')


s = Son()
s.display_property()
