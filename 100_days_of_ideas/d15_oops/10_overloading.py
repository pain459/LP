'''
Python does not support true method overloading (like Java/C++).
Instead, it achieves similar behavior using default arguments or *args and **kwargs.
'''

class Math:
    def add(self, a, b=0):
        return a + b
    
math = Math()
print(math.add(5))
print(math.add(5, 10))  # overloaded
