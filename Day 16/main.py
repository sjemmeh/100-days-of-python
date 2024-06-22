from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

power_on = True
maintenance_mode = False


while power_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})").lower()
    if choice == "off":
        power_on = False
    elif choice == "maintenance":
        maintenance_mode = True
        while maintenance_mode:
            maintenance_options = menu.get_commands()
            maintenance_choice = input(f"What would you like to do? ({maintenance_options})")
            if menu.find_command(maintenance_choice):
                if maintenance_choice == "exit":
                    maintenance_mode = False
                elif maintenance_choice == "report":
                    coffee_maker.report()
                    money_machine.report()
                else:
                    add_resource_name = input("What would you like to add? (water/milk/coffee): ")
                    add_resource_amount = int(input("How much would you like to add?: "))
                    coffee_maker.add_resources(add_resource_name, add_resource_amount)
    else:
        if menu.find_drink(choice):
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)