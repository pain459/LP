# inheritance call to p3
from p3 import Student

s = Student()
s.setid(11)
s.setname('Nagato')
s.setaddress('Konahu')
s.setmarks(3)


print(f'ID = {s.getid()}')
print(f'Name = {s.getname()}')
print(f'Address = {s.getaddress()}')
print(f'Marks = {s.getmarks()}')