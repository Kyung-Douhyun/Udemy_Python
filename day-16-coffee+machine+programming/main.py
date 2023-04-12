from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

# 2. Check resources sufficient.
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        # 1. Print report
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # 2. Check resources sufficient.
        if coffee_maker.is_resource_sufficient(drink):
            # 3. Process coins.
            # 4. Check transaction successful
            if money_machine.make_payment(drink.cost):
                # 5. Make coffee
                coffee_maker.make_coffee(drink)