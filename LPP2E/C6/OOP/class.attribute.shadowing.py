class Point:
    x = 10
    y = 7


p = Point()  # instantiation
print(p.x)  # from class attribute
print(p.y)  # from class attribute

p.x = 12  # p gets into its own x attribute
print(p.x)  # 12, now found on the instance
print(Point.x)  # 10, class attribute is still the same

del p.x   # We delete the instance attribute
print(p.x)  # 10, returns the class attribute

p.z = 3  #  p gets into its own z attribute. this is not found at class.
print(p.z)  # 3, returning from the instance.

print(Point.z)  # returns attribute error.
