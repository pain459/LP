# Using a base class constructor in sub class.
class Father:
    def __init__(self, property=0):
        self.property = property

    def display_property(self):
        print(f'Father\'s property = {self.property}')

class Son(Father):
    def __init__(self, property1 = 0, property = 0):
        super().__init__(property)
        self.property1 = property1

    def display_property(self):
        print(f'Son\'s property = {self.property  + self.property1}')


# Create sub class instance and display father's property
s = Son(200000, 800000)
s.display_property()