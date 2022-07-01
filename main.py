from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

register = MoneyMachine()
menu = Menu()
coffee_machine = CoffeeMaker()

prompt = 'on'
while prompt != 'off':
    prompt = input(f"What would you like? {menu.get_items()}: ").lower()

    if prompt == "report":
        coffee_machine.report()
        register.report()
    elif prompt != "off":
        drink = menu.find_drink(prompt)
        if drink != None and coffee_machine.is_resource_sufficient(drink) and register.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
