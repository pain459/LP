'''
Polymorphism means "many forms." It allows methods in different classes to have the same name but behave differently.
'''
class Bird:
    def fly(self):
        return "Bird can fly!"
    
class Penguin(Bird):
    def fly(self):
        return "Penguin can't fly"
    

# Polymorphism in action
animals = [Bird(), Penguin()]
for animal in animals:
    print(animal.fly())
