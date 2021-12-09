# Writing an employee class
class Employee:

    raise_amount = 1.04
    number_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.number_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount  # or I can access as Employee.raise_amount


emp_1 = Employee('RRR', 'SSS', 50000)
emp_2 = Employee('RRR1', 'SSS1', 60000)
print(Employee.number_of_employees)  # This will be 2. As init method executes everytime when you create an instance.

print(emp_1.fullname())

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# Accessing namespaces of instances
print(emp_1.__dict__)

# Accessing raise amount for different instances and class itself.
print(Employee.raise_amount)  # Accessing from the class.
print(emp_1.raise_amount)  # from emp_1
print(emp_2.raise_amount)  # from emp_2

# Now everyone will have the raise amount as 1.05
Employee.raise_amount = 1.05
print(Employee.raise_amount)  # Accessing from the class.
print(emp_1.raise_amount)  # from emp_1
print(emp_2.raise_amount)  # from emp_2

# Only emp_1 raise amount will be changed, rest is unchanged. This is ability to change for single instance.
emp_1.raise_amount = 2.01
print(Employee.raise_amount)  # Accessing from the class.
print(emp_1.raise_amount)  # from emp_1
print(emp_2.raise_amount)  # from emp_2

