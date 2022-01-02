def narcissistic(value):
    l_value = [int(i) for i in str(value)]
    n_value = 0
    for i in l_value:
        n_value += i ** len(l_value)
    if n_value == value:
        print(f'{value} is narcissistic')
        return True
    else:
        print(f'{value} is not narcissistic')
        return False
    # return n_value


print(narcissistic(122))