'''
Inheritance allows a class (child) to inherit attributes and methods from another class (parent).
'''

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some generic sound."
    
# Child class
class Cat(Animal):
    def sound(self):
        return f"{self.name} says Meow!"
    
my_cat = Cat("Orion")
print(my_cat.sound())