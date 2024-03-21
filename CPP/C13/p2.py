# Instance vars and instance method -v 2.0
class Student:
    # this is constructor
    def __init__(self, n=' ', m=0):
        self.name = n
        self.marks = m

    # This is an instance method.
    def display(self):
        print('Hi', self.name)
        print('Your marks', self.marks)


# Constructor is called without any arguments
s = Student()
s.display()
print('-'*10)

# Constructor is called with 2 arguments
s1 = Student(n='Pain', m=101)
s1.display()
print('-'*10)
