# Create Student class by deriving it from Teacher class.
from p1 import Teacher
class Student(Teacher):  # class SubClass(BaseClass)
    def setmarks(self, marks):  # adding new methods along with existing ones.
        self.marks = marks
    def getmarks(self):
        return self.marks


s = Student()
s.setmarks(100)
print(f'Marks = {s.getmarks()}')