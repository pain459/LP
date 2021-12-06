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
available_operators = """
Supported operations:
+
-
/
*
"""

def initialization():
    """This function will print the logo and ask for the first number, operation and second number."""
    print(logo)
    num1 = eval(input('Enter the first number: '))
    print(available_operators)
    selected_correct_operator = False
    while not selected_correct_operator:
        operation = input('Enter the operation you want to perform: ')
        if operation in ['+', '-', '/', '*']:
            num2 = eval(input('Enter second number: '))
            selected_correct_operator = True
        else:
            print('Please select correct operator!')
            print(available_operators)
    return num1, num2, operation

def operation_selector():
    """This function will print the available operations and store the selected operation."""
    print(available_operators)
    selected_correct_operator = False
    while not selected_correct_operator:
        operation = input('Enter the operation you want to perform: ')
        if operation in ['+', '-', '/', '*']:
            num2 = eval(input('Enter second number: '))
            selected_correct_operator = True
        else:
            print('Please select correct operator!')
            print(available_operators)
    return num2, operation

def operation_performer(num1, num2, operation):
    """This function will perform the requested operation."""
    if operation == '+':
        result = addition(num1, num2)
        return result
    elif operation == '-':
        result = subtraction(num1, num2)
        return result
    elif operation == '/':
        result = division(num1, num2)
        return result
    elif operation == '*':
        result = multiplication(num1, num2)
        return result
    else:
        print('Invalid operation requested.')

def redo_operation(result):
    """This function will redo the calculaton with existing result or start again."""
    redo = True
    while redo:
        user_choice = str(input(f'Current result is {result}. Enter "y" to perform operation with existing result. Enter "n" to restart the program. Enter stop to break the loop: ')).lower()
        if user_choice == 'y':
            num1 = result
            num2, operation = operation_selector()
            operation_performer(num1, num2, operation)
        elif user_choice == 'n':
            redo = False    
            initialization()
        elif user_choice == 'stop':
            redo = False
        elif user_choice not in ['y', 'n', 'stop']:
            print('Invalid option entered. Starting the program again.')
            redo = False
            initialization()

calculate_again = True
while calculate_again:
    num1, num2, operation = initialization()
    result = operation_performer(num1, num2, operation)
    redo_operation(result)
    user_choice = str(input('Do you want to continue? y/n '))
    if user_choice in ['y', 'n']:
        if user_choice == 'y':
            print('Starting the program again.')
            calculate_again = True
        else:
            print('Program will terminate now.')
            calculate_again = False

    else:
        print('Invalid entry! Try again.')
        calculate_again = True