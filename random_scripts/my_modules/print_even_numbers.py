def print_even(start, end):
    """ This will print including the last digit """
    for i in range(start, end + 1):
        if i % 2 == 0:
            return i
        else:
            pass


if __name__ == "__main__":
    print_even(1, 4)
