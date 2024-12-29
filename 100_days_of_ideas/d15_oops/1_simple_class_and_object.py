# Define a class
class Dog:
    # Method to initialize attributes (constructor)
    def __init__(self, name, breed):
        self.name = name  # Attribute
        self.breed = breed  # Attribute

    # Method (behaviour)
    def bark(self):
        return f"{self.name} says woof!"
    

# create an object (instance of the class)
my_dog = Dog("Buddy", "Doberman")
my_dog2 = Dog("Labrador", "Jackie")



# Access attributes and methods
print(my_dog.name)
print(my_dog.bark())
print(my_dog.breed)

# Access in reverse. Testing positional arguments
print(my_dog2.name)  # Should print Labrador
print(my_dog2.breed)  # Should print Jackie