# This program will have commands inbuilt to convert temperature from different units.

def f_to_c(x):
    c = round((x - 32) * (5 / 9), 2)
    print(f'Temperature conversion : {x}F is {c}C ')


def c_to_f(x):
    f = round(x * (9 / 5) + 32, 2)
    print(f'Temperature conversion : {x}C is {f}F ')


if __name__ == "__main__":
    print('Sample outputs of this function below.')
    f_to_c(10)
    c_to_f(10)
