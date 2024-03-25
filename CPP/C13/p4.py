# Class vars or static vars example
class Sample:
    # This is a class var
    x = 10

    # This is a class method
    @classmethod
    def modify(cls):
        cls.x += 1


# Create 2 instances
s1 = Sample()
s2 = Sample()
print(f'x in s1 {s1.x}')
print(f'x in s2 {s2.x}')

# modify x in Sample
s1.modify()
print(f'x in s1 {s1.x}')
print(f'x in s2 {s2.x}')
