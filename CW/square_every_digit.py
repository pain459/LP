def square_digits(num):
    d = [int(i )for i in str(num)]
    squared_d = [i ** 2 for i in d]
    x = ''
    for i in range(len(squared_d)):
        x = x + str(squared_d[i])

    return int(x)



print(square_digits(9119))