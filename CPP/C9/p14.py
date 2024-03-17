# Passing list to the function and modify it
def modify(x):
    x.append(9)
    print(x, id(x))


lst = [1, 2, 3, 4]
modify(lst)
print(lst, id(lst))