# Instance variables and instance method.
class Student:
    # this is a special method called constructor
    def __init__(self):
        self.name = 'pain'
        self.age = 1009
        self.team = 'Akatsuki'

    # this is an instance method
    def bio(self):
        print("The name is", self.name)
        print(f'Age {self.age}')
        print('belongs to team', self.team)


# create an instance to student class
s1 = Student()
s1.bio()
