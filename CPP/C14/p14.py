# multiple inheritance with several classes
# Method Resolution Order
class A(object):
    def method(self):
        print('A class method')
        super().method()


class B(object):
    def method(self):
        print('B class method')
        super().method()


class C(object):
    def method(self):
        print('B class method')


class X(A, B):
    def method(self):
        print('C class method')
        super().method()


class Y(B, C):
    def method(self):
        print('D class method')
        super().method()


class P(X, Y, C):
    def method(self):
        print('P class method')
        super().method()


p = P()
p.method()


