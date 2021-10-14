class Simplest():  # when empty, the braces are optional
    pass


print(type(Simplest))  # What type is this object. <class 'type'>
simp = Simplest()  # We create an instance of Simplest: simp. instantiation.
print(type(simp))  # What type is Simp? <class '__main__.Simplest'>
print(type(simp) == Simplest)  # There is a better way to do this. But this will return true.
