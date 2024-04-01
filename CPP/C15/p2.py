from abc import ABC, abstractmethod
import math


class MyClass(ABC):
    @abstractmethod
    def calculate(self, x):
        pass


# This is subclass in MyClass
class Sub1(MyClass):
    def calculate(self, x):
        print(f'Square value is {x * x}')


# This is another subclass for MyClass
class Sub2(MyClass):
    def calculate(self, x):
        print(f'Square root is {math.sqrt(x)}')


# Third subclass for MyClass
class Sub3(MyClass):
    def calculate(self, x):
        print(f'Cube value {x ** 3}')


# Create Sub1 class and call calculate() method
obj1 = Sub1()
obj1.calculate(16)
obj2 = Sub2()
obj2.calculate(16)
obj3 = Sub3()
obj3.calculate(16)
