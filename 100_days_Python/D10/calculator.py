from calc_art import logo

# Calculator functions
def addition(a, b):
    print(f'{a} + {b} = {a+b}')
    result = a + b
    return result
    #return a + b
def subtraction(a, b):
    print(f'{a} - {b} = {a-b}')
    result = a - b
    return result
    #return a - b
def division(a, b):
    print(f'{a} / {b} = {a/b}')
    result = a / b
    return result
    #return a / b
def multiplication(a, b):
    print(f'{a} * {b} = {a*b}')
    result = a * b
    return result
    #return a * b

def addition_ext(num1):
    redo = True
    while redo:
        num2 = eval(input('Enter second number: '))
        result = addition(num1, num2)
        num1 = result  # making the result as num1
        choice_post_calc = input(f'Do you want to continue calculating with {num1}? y to start new operation, n to start a new calculation: ')
        if choice_post_calc == 'y':
            first_step()
            operation_picker(operation, num1)
            redo = True
        elif choice_post_calc == 'n':
            print('Proceeding to main loop.')
            initiate()
            redo = False

def operation_picker(operation, num1):
    if operation == '+':
        addition_ext(num1)
    elif operation == '-':
        num2 = eval(input('Enter second number: '))
        result = subtraction(num1, num2)
        num1 = result  # making the result as num1
        print(result)
    elif operation == '/':
        num2 = eval(input('Enter second number: '))
        result = division(num1, num2)
        num1 = result  # making the result as num1
        print(result)
    elif operation == '*':
        num2 = eval(input('Enter second number: '))
        result = multiplication(num1, num2)
        num1 = result  # making the result as num1
        print(result)
    else:
        print('Invalid operation requested.')

def first_step():
    # num1 = eval(input('Enter the first number: '))
    print("""Supported operations:
             +
             -
             /
             *""")
    operation = input('Enter the operation you want to perform: ')
    return operation

def initiate():
    print(logo)
    num1 = eval(input('Enter the first number: '))
    return num1



calculate_again = True
while calculate_again:
    num1 = initiate()
    operation = first_step()
    operation_picker(operation, num1)
    user_choice = str(input('Do you want to continue? y/n '))
    if user_choice in ['y', 'n']:
        if user_choice == 'y':
            print('Returning to loop')
            calculate_again = True
        else:
            print('Program will terminate now.')
            calculate_again = False

    else:
        print('Invalid entry! Try again.')
        calculate_again = True