# base class constructor is available to sub class
class Father:
    def __init__(self):
        self.property = 100000

    def display_property(self):
        print(f'Fathers property = {self.property}')


class Son(Father):
    pass


# Create a sub class instance and display fathers property
x = Son()
x.display_property()