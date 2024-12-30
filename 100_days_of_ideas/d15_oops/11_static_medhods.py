# A method that does not depend on the instance or class. Use @staticmethod
class Utility:
    @staticmethod
    def add(a, b):
        return a + b
    

print(Utility.add(3, 4))