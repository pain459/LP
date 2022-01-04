# Write a function named first_non_repeating_letter that takes a string input, and returns the first character that
# is not repeated anywhere in the string.
#
# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in
# the string, and occurs first in the string.
#
# As an added challenge, upper- and lowercase letters are considered the same character, but the function should
# return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
#
# If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.

def first_non_repeating_letter(string):
    if len(string) == 0:
        return f"''"
    else:
        pass

    repeater = []
    for i in list(string):
        if string.upper().count(i) == 1 or string.lower().count(i) == 1:
            return i
        elif string.upper().count(i) > 1 or string.lower().count(i) > 1:
            repeater.append(i)
        else:
            pass
    if set(repeater) == set(list(string)):
        return f"''"



print(first_non_repeating_letter('sTress'))
print(first_non_repeating_letter('abba'))
print(first_non_repeating_letter('aa'))
print(first_non_repeating_letter(''))