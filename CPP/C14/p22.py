# overloading with * operator
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, other):
        return self.salary * other.days


class Attendance:
    def __init__(self, name, days):
        self.name = name
        self.days = days


x1 = Employee('Pain', 50000)
x2 = Attendance('Pain', 29)
print('This month salary =', x1 * x2)
