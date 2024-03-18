# filter() function the returns even numbers from a list.
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def is_odd(n):
    if n % 2 != 0:
        return True
    else:
        return False


list1 = [1, 3, 2, 4, 5, 7, 9]
list2 = list(filter(is_even, list1))
print(list2)

list3 = list(filter(is_odd, list1))
print(list3)