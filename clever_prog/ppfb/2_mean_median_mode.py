# In this program we will calculate the mean median and mode of the given list.
# user will give the numbers, and they will be appended to the list.
# For simplicity’s sake we will take integers first. Later will expand the scope to float as well.

print("Welcome to mean, median and mode calculator.")
_trap = True
_user_list = []
while _trap:
    _user_input = int(input("Enter the element to input to list, press 0 to exit: "))
    if _user_input != 0:
        _user_list.append(_user_input)
    else:
        _trap = False
        # break
_list1 = [12, 34, 22, 34, 56, 78, 90, 32, 56, 32]  # Even count
_list2 = [78, 56, 89, 66, 88, 34, 42, 35, 12, 16, 76]  # Odd count

# _mean = sum(_list1) / len(_list1)
# print("Mean is list 1 is", _mean)

try:
    print("User input list is", _user_list)
    # mean calculation.
    _mean = sum(_user_list) / len(_user_list)
    print("Mean of the user provided list is", "%.2f" % round(_mean, 2))


except ZeroDivisionError:
    print("User input list empty. Program will now exit.")
