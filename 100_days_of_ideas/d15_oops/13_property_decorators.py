# Control access to attributes using @property. This is a Pythonic way to implement getters and setters.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter 
    def salary(self, new_salary):
        if new_salary > 0:
            self._salary = new_salary


emp = Employee("John", 50000)
print(emp.salary)
emp.salary = 53000
print(emp.salary)