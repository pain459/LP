import argparse

DEFAULT_C = 10
DEFAULT_D = 1


def create_argument_parser():
    SYNOPSIS = """

        """
    parser = argparse.ArgumentParser(
        description=SYNOPSIS, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--a_value',
        '-a',
        dest='a',
        type=int,
        required=True,
        help='input for function 1'
    )

    parser.add_argument(
        '--b_value',
        '-b',
        dest='b',
        type=int,
        required=True,
        help='input for function 2'
    )

    parser.add_argument(
        '--c_value',
        '-c',
        dest='c',
        type=int,
        help='optional value for function 3'
    )

    parser.add_argument(
        '--d_value',
        '-d',
        dest='d',
        type=int,
        help='optional value for function 4'
    )

    parser.add_argument(
        '--e_value',
        '--e',
        help='without tails'
    )

    return parser


def func1(a):
    return a ** 2


def func2(b):
    return b ** 2


def func3(c):
    if c is None:
        c = DEFAULT_C
    return c * 100


def func4(d):
    if d is None:
        pass
    else:
        d = DEFAULT_D
        return d * 3.14


def func5():
    print("From optional function")


def main():
    parser = create_argument_parser()
    arguments = parser.parse_args()
    a = arguments.a
    b = arguments.b
    c = arguments.c
    d = arguments.d
    e = arguments.e
    print(func1(a))
    print(func2(b))
    print(func3(c))
    print(func4(d))


if __name__ == "__main__":
    main()
