'''
Mixins are used to add functionality to classes without being a base class. They are not meant to be instantiated on their own but provide reusable methods.
'''

class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)
    
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class JSONUser(User, JSONMixin):
    pass

user = JSONUser("Alice", 30)
print(user.to_json())