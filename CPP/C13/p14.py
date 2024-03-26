# Inner class example - v2.0
class Person(object):
    def __init__(self):
        self.name = 'RRR'

    def display(self):
        print(f'Name = {self.name}')

    class dob(object):
        def __init__(self):
            self.mm = 10
            self.dd = 10
            self.yyyy = 1010

        def display(self):
            print(f'DOB is {self.mm}-{self.dd}-{self.yyyy}')


x = Person()
x.display()
y = Person().dob()
y.display()
