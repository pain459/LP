# This class contains employee details.
class Emp(object):
    # This is a constructor
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    # This is an instance method
    def display(self):
        print(f'Id = {self.id}')
        print(f'Name = {self.name}')
        print(f'Salary = {self.salary}')

    @staticmethod
    def calculate_increment(salary):
        new_salary = salary + (salary * 0.25)
        return new_salary


# Traditional way to access the details and calculate
# salary = 1000
# e = Emp(1234, 'RRR', salary)
# e.display()
# updated_salary = e.calculate_increment(salary)
# print(f'New Salary is {updated_salary}')

# This class displays employee details
class MyClass(object):
    # Method to receive employee class instance
    # and display employee details
    @staticmethod
    def MyMethod(e):
        # Increment salary of e by 100
        e.salary += 1000
        e.display()


e = Emp(1234, 'RRR', 1000)
MyClass.MyMethod(e)