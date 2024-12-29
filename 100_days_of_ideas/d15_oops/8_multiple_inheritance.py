'''
Python allows a class to inherit from multiple classes, but it can lead to ambiguity. The MRO ensures consistency.
'''

class Engine:
    def start(self):
        return "Engine started"
    
class Wheels:
    def start(self):  # Added to test mro.
        return "Engine failed"
    def roll(self):
        return "Wheels rolling"
    
class Car(Engine, Wheels):
    pass

car = Car()
print(car.start())
print(car.roll())