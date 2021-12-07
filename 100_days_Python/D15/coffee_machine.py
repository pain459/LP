from resources_menu import MENU, resources

# menu is printed as dict{dict{dict}} and resources are printed as {dict}
cash_balance_in_machine = 0
MENU = MENU  # copying the entire menu into a new object
resources = resources


def device_report():
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}ml")
    print(f"Money : ${cash_balance_in_machine}")


def check_user_choice():
    """returns selected drink if the drink is in the list. Else return 1"""
    user_choice = str(input("What would you like? (espresso/latte/cappuccino) "))
    if user_choice in ['espresso', 'latte', 'cappuccino', 'off', 'report']:
        return user_choice
    else:
        return 1


def check_resources(selected_drink):
    milk_required = True
    if selected_drink == 'espresso':
        milk_required = False
    if resources['water'] < MENU[selected_drink]['ingredients']['water'] and milk_required:
        return "Sorry, there is not enough water"
    elif milk_required and resources['milk'] < MENU[selected_drink]['ingredients']['milk']:
        return "Sorry, there is not enough milk"
    elif resources['coffee'] < MENU[selected_drink]['ingredients']['coffee'] and milk_required:
        return "Sorry, there is not enough coffee"
    else:
        return 0


def process_coins(selected_drink):
    print("Insert coins now")
    quarters = eval(input('Quarters: '))
    dimes = eval(input('Dimes: '))
    nickles = eval(input('Nickles: '))
    pennies = eval(input('Pennies: '))
    total_processed_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return round(total_processed_money, 2)


def check_transaction(entered_money, selected_drink):
    if MENU[selected_drink]['cost'] < entered_money or MENU[selected_drink]['cost'] == entered_money:
        cash_dispensed = entered_money - MENU[selected_drink]['cost']
        # cash_balance_in_machine += round(cash_dispensed, 2)
        return round(cash_dispensed, 2)
    elif MENU[selected_drink]['cost'] > entered_money:
        # cash_dispensed = f"Sorry, that's not enough money. Money refunded."
        return -1


def make_coffee(selected_drink):  # removed ingredients as we are accessing from global list.
    milk_required = False
    resources['water'] = resources['water'] - MENU[selected_drink]['ingredients']['water']
    if milk_required:
        resources['milk'] = resources['milk'] - MENU[selected_drink]['ingredients']['milk']
    else:
        pass
    resources['coffee'] = resources['coffee'] - MENU[selected_drink]['ingredients']['coffee']
    print(f"Here is your {selected_drink}. Enjoy!")


# User selection evaluator
selected_correct_drink = False
while not selected_correct_drink:
    choice = check_user_choice()
    if choice == 1:
        print('Invalid Entry!')
        selected_correct_drink = False
    elif choice == 'off':
        print('Turning off the machine for maintenance!')
        selected_correct_drink = True
    elif choice == 'report':
        device_report()
    else:
        # print(f'{choice} is available')
        resource_output = check_resources(selected_drink=choice)
        # print(resource_output)
        if resource_output == 0:
            print(f'{choice} is available')
            total = process_coins(selected_drink=choice)
            # print(total)
            cash_dispensed_by_machine = check_transaction(entered_money=total, selected_drink=choice)
            if cash_dispensed_by_machine == -1:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                cash_balance_in_machine += total - cash_dispensed_by_machine
                print(f'Please collect change {cash_dispensed_by_machine}')
                make_coffee(selected_drink=choice)
        else:
            print(resource_output)
        selected_correct_drink = False
