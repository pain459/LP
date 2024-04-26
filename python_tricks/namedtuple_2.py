# Named tuple to create lightweight class
from collections import namedtuple

# named tuple declaration
Student = namedtuple('Student', ['name', 'age', 'dob'])

# Adding values
s = Student('RRR', 4, 1900)

print(s.name)