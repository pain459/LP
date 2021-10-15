# Mutable or Immutable
"""
age = 42
id(age)
Out[31]: 140725800042848
age = 32
id(age)
Out[33]: 140725800042528
"""

class Person():
    def __init__(self, age):
        self.age = age

fab = Person(age=45)

fab.age  # 45
id(fab)  # 2095442985864
id(fab.age)  # 140725800042944
fab.age = 25
id(fab)  # 2095442985864 Unchanged
id(fab.age)  # 140725800042304  Notice the change
