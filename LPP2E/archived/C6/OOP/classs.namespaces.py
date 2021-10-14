class Person:
    species = 'Human'


print(Person.species)  # Human
Person.alive = True  # Added dynamically
print(Person.alive)  # True

man = Person()  # instantiation
print(man.species)  # Human (Inherited)
print(man.alive)  # true (inherited)

Person.alive = False
print(man.alive)  # False (inherited)

man.name = 'Darth'
man.surname = 'Vader'
print(man.name, man.surname)
print(Person.name)  # returns Attribute error.
