# Static method to calculate power of value of a number
class MyClass(object):
    @staticmethod
    def MyMethod(x, y):
        return x ** y


n = MyClass()
print(n.MyMethod(23, 22))