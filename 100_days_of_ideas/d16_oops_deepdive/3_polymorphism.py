"""
Polymorphism allows differnt classes to implement methods with the same name but behave differently.
"""
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"
    
class Cat(Animal):
    def sound(self):
        return "Meow!"
    
def make_sound(animal):
    print(animal.sound())


# Usage
animals = [Dog(), Cat()]
for animal in animals:
    make_sound(animal)