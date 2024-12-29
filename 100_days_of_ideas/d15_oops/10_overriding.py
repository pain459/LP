# A subclass provides a specific implementation of a method already defined in the parent class.

class Parent:
    def greet(self):
        return "Hello from Parent"
    
class Child:
    def greet(self):
        return "Hello from child"
    
child = Child()
print(child.greet())