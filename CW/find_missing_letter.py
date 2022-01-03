import string


def find_missing_letter(chars):
    alphabets_list = string.ascii_lowercase if chars[0] >= 'a' else string.ascii_uppercase
    for i in alphabets_list[alphabets_list.index(chars[0]):]:
        if i not in chars:
            return i[0]
    # return alphabets_list


print(find_missing_letter(['A', 'B', 'C', 'D', 'E']))
