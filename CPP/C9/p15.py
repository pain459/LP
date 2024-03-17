# Passing a list to a function
def modify(lst):
    lst = [1, 2, 3, 4]
    print(lst, id(lst))


lst = [5, 6, 7, 8]
modify(lst)
print(lst, id(lst))