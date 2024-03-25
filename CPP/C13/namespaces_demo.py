class namespaces_demo:
    # this is a class var
    x = 10


# Access the class variable in the class namespace
print(namespaces_demo.x)
namespaces_demo.x += 1
print(namespaces_demo.x)


s1 = namespaces_demo()
s2 = namespaces_demo()
print(f'{s1.x} and {s2.x}')
s1.x += 1
print(f'{s1.x} and {s2.x}')  # only s1 value will be modified.
