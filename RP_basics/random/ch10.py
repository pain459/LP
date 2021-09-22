# OOP
# Lets crack the classes.
class Dog:
    # Class Attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} year old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound='Arf'):
        return super().speak(sound)
        # return f"{self.name} says {sound}"


class Dachshund(Dog):
    pass


class BullDog(Dog):
    pass


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 4)
jack = BullDog("Jack", 3)
jim = BullDog("Jim", 5)
jacky = GoldenRetriever("Jacky", 1)


print(miles.speak())
print(jim.speak("Woof"))
print(jacky)
print(jacky.speak())