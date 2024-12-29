# MRO determines the order in which python looks for a method in the inheritance heirarchy. Python follows the C3 Linearization algorithm (used in super() function)


class A:
    def show(self):
        return "Class A"
    
class B(A):
    def show(self):
        return "Class B"
    
class C(A):
    def show(self):
        return "Class C"
    
class D(B, C):
    pass

obj = D()
print(obj.show())
print(D.mro())  # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]