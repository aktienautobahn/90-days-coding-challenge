from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
#menu_item = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


machine_on = True
while machine_on:
    choice = input(f"Please choose a drink: {menu.get_items()}: ")
    #if user wants to switch off the machine
    if choice == "off":
        machine_on = False
    #if user wants to get a report
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    #processing order 
    elif menu.find_drink(choice):

        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

    