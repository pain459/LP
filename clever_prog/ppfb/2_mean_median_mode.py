# In this program we will calculate the mean median and mode of the given list.
# user will give the numbers, and they will be appended to the list.
# For simplicity’s sake we will take integers first. Later will expand the scope to float as well.

print("Welcome to mean, median and mode calculator.")
_trap = True
_user_list = []
_error_message = "Unsupported type entered. Please try again."
while _trap:
    try:
        _user_input = int(input("Enter an int number for list, press 0 to exit: "))
        if _user_input != 0:
            _user_list.append(_user_input)
        else:
            var = _trap = False
    except TypeError:
        print(_error_message)
        _trap = True
    except ValueError:
        print(_error_message)
        _trap = True

try:
    print("User input list is", _user_list)
    # mean calculation.
    _mean = sum(_user_list) / len(_user_list)
    print("Mean of the user provided list is", "%.2f" % round(_mean, 2))
    # median calculation.
    _user_list.sort()
    if len(_user_list) % 2 == 0:
        m1 = _user_list[len(_user_list) // 2]
        m2 = _user_list[len(_user_list) // 2 - 1]
        median = (m1 + m2) / 2
    else:
        median = _user_list[len(_user_list) // 2]
    print(median)
    # Mode calculation. Finding the most frequent number in the given list.
    list1 = []
    _user_list = list1
    frequency = {}
    for i in list1:
        frequency.setdefault(i, 0)
        frequency[i] += 1
    frequent = max(frequency.values())
    for i, j in frequency.items():
        if j == frequent:
            mode = i
        else:
            mode = 0
    print(mode)


except ZeroDivisionError:
    print("User input list empty. Program will now exit.")
