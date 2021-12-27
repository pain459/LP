class Employee:

    def __init__(self, first, last, pay):  # constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('RRR', 'SSS', 50000)
emp_2 = Employee('QQQ', 'AAA', 60000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())

# Employee.fullname(emp_1)