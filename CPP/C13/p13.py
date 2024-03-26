# Inner class example
class Person(object):
    def __init__(self):
        self.name = 'Charles'
        self.db = self.dob()  # Creating inner class object.

    def display(self):
        print(f'Name = {self.name}')

    class dob(object):
        def __init__(self):
            self.dd = 10
            self.mm = 10
            self.yyyy = 1010

        def display(self):
            print(f'DOB is {self.dd}-{self.mm}-{self.yyyy}')


x = Person()
x.display()

y = x.db  # Inner class object creation with keyword db
y.display()
