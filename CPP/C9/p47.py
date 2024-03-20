from CPP.C9 import p44


def addition(x, y):
    return p44.add(x, y)


def main():
    result = addition(100, 34)
    print(f'Result is {result}.')


if __name__ == "__main__":
    main()
