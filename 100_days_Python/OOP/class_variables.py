class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):  # constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1  # will update the number of employees as soon as instance is created.

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('RRR', 'SSS', 50000)
emp_2 = Employee('QQQ', 'AAA', 60000)

# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.fullname())
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

print(emp_1.__dict__)  # To see the name space.
# Employee.fullname(emp_1)
Employee.raise_amount = 1.05
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print(Employee.raise_amount)
