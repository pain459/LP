# Accessor and mutator methods
class Student:

    # mutator method
    def setName(self, name):
        self.name = name

    # accessor method
    def getName(self):
        return self.name

    # mutator method
    def setMarks(self, marks):
        self.marks = marks

    # accessor method
    def getMarks(self):
        return self.marks


# Create instances with some data
n = int(input("Enter number of students: "))

i = 0
while i < n:
    # Create student class instance
    s = Student()
    name = input("Enter name: ")
    s.setName(name)
    marks = int(input("Enter marks: "))
    s.setMarks(marks)

    # Retrieve data from the Student class instance
    print(f'Hi, {s.getName()}')
    print(f'Your marks: {s.getMarks()}')

    i += 1
    print('-' * 20)
