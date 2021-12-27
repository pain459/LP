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

    @classmethod  # decorator to access class variables.
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod  # Using class methods as alternative constructors.
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # Static methods
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('RRR', 'SSS', 50000)
emp_2 = Employee('QQQ', 'AAA', 60000)

Employee.set_raise_amt(1.05)  # This will set everyone's raise to 5%

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
#
#
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'
#
# # Alternative constructors long route
# # first, last, pay = emp_str_1.split('-')
# # new_emp_1 = Employee(first, last, pay)
#
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)

