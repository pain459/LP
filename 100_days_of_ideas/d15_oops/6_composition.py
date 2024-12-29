'''
Composition is a design principle where a class contains an object of another class as an attribute.
'''

class Engine:
    def start(self):
        return "Engine started"
    
class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()  # composition

    def start(self):
        return f'{self.brand} car: {self.engine.start()}'
    

car = Car("Toyota")
print(car.start())