# Method overloading
class MyClass:
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print('Sum of three =', a+b+c)
        elif a!=None and b!=None:
            print('Sum of two =', a+b)
        else:
            print('Please enter at least two arguments')


m = MyClass()
m.sum(10, 20)