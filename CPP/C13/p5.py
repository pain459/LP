# Instance methods to process data of the objects\
class Student:
    # This is a constructor
    def __init__(self, n='', m=0):
        self.name = n
        self.marks = m

    # This is an instance method
    def display(self):
        print("Hi", self.name)
        print("Your marks", self.marks)

    # to calculate grades based on marks
    def calculate(self):
        if self.marks >= 600:
            print("You got first grade.")
        elif self.marks >= 500:
            print("You got second grade.")
        elif self.marks >= 350:
            print("You got third grade.")
        else:
            print("You are failed.")


# Create instances with some data from keyboard
n = int(input("Enter number of students: "))

i = 0
while i < n:
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    # Create student class instances and store data
    s = Student(name, marks)
    s.display()
    s.calculate()
    print('-' * 20)
    i += 1
