def soe(x):
    j = 0
    for i in range(x):
        if i % 2 == 0:
            j += i

    return j


if __name__ == "__main__":
    print(soe(4))
