# A class with a method
class MyClass(object):
    def calculate_square(self, x):
        print(f'Square is {x * x}')


# all objects share the same calculate method
a = MyClass()
a.calculate_square(12)
b = MyClass()
b.calculate_square(13)