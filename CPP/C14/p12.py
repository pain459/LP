# Multi inheritance
class A(object):
    def __init__(self):
        self.a = 'a'
        print(self.a)


class B(object):
    def __init__(self):
        self.b = 'b'
        print(self.b)


class C(A, B):
    def __init__(self):
        self.c = 'c'
        print(self.c)
        super().__init__()  # A is loaded as super as A is loaded first.


x = C()
