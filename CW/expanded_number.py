def expanded_form(num):
    result = []
    for index, digit in enumerate(str(num)[::-1]):
        # print(i, j)
        if int(digit) != 0:
            result.append(digit + ('0' * index))
    return ' + '.join(result[::-1])
    # return num



print(expanded_form(512))