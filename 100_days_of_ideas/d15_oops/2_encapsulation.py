class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.__age = age  # Private attribute


    def get_age(self):  # Public method to access private attribute
        return self.__age
    

    def set_age(self, new_age):  # Public method to modify private attribute
        if new_age > 0:
            self.__age = new_age  


person = Person("Barber", 39)
print(f"Person name is {person.name}")
print(f"{person.name} is {person.get_age()}\n")
print(f"Setting age to 49")
person.set_age(49)
print(f"\n{person.name} new age is {person.get_age()}")