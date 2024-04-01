# example for two exceptions
# a function to find total and average of list elements
def avg(list):
    total = 0
    for i in list:
        total += i
    average = total / len(list)
    return total, average


# call the avg() and pass a list
try:
    t, a = avg([1, 2, 3, 4, '5l'])
    print(f'Total is {t} and average is {a}')
except TypeError:
    print('List should contain numbers only')
except ZeroDivisionError:
    print('Please don\'t give an empty list.')
