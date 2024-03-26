# Making inheritance calls example
from p1 import Teacher
# Create instance of the teacher
t = Teacher()

# Store the data into instance
t.setid(10)
t.setname('Pain')
t.setaddress("Village hidden in the leaf")
t.setsalary(10)

# retrieve the data from the instance
print(f'ID = {t.getid()}')
print(f'Name = {t.getid()}')
print(f'Address = {t.getaddress()}')
print(f'Salary = {t.getsalary()}')
