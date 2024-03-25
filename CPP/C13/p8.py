# Understanding static methods
class Myclass:
    # This is a class var or static var
    n = 0

    # constructor that increments n when an instance is created
    def __init__(self):
        Myclass.n = Myclass.n + 1

    # This is a static method to display number of classes
    @staticmethod
    def noObjects():
        print(f'No. of instances created: {Myclass.n}')


# Create two instances
obj1 = Myclass()
obj2 = Myclass()
obj3 = Myclass()
Myclass.noObjects()
