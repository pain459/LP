from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

latte = MenuItem('latte', 1.5, 100, 16, 20)
espresso = MenuItem('espresso', 1.5, 50, 0, 18)
cappuccino = MenuItem('cappuccino', 3.0, 250, 100, 24)

menu = Menu()
print(menu.get_items())
print(menu.find_drink(order_name='latte').ingredients)