from drinks import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 50,
}
strengths = ["normal", "strong"]
profit = 0
maintenance_password = "supersecretplaintext"

def login(password):
    if password == maintenance_password:
        return True
    else:
        return False
def enough_resources(ingredients, strength):
    """Checks if there are enough resources available, and returns either True or False"""
    if strength == "strong":
        if (ingredients["coffee"] * 1.5) > resources["coffee"]:
            print(f"Sorry there is not enough coffee.")
            return False
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False

    return True

def payment_transaction():
    """Processes payment and returns with total paid"""
    total = int(input("How many 2 euros?: ") or 0) * 2
    total += int(input("How many 1 euros?: ") or 0) * 1
    total += int(input("How many 50 cents?: ") or 0) * 0.50
    total += int(input("How many 20 cents?: ") or 0) * 0.20
    total += int(input("How many 10 cents?: ") or 0) * 0.10
    return total


def transaction_succesfull(strength, money, cost):
    """Returns True if enough money"""
    if strength == "strong":
        cost += 0.5
    if money > cost:
        change = round(money - cost, 2)
        print(f"Change: {change}")
        global profit
        profit += cost
        return True
    else:
        print("Not enough money.")
        return False



def create_drink(name, ingredients):
    """Creates the drink and deducts resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {name}, enjoy your drink!")

def fill_machine(name, amount):
    """Fills the machine"""
    if name in resources:
        resources[name] += amount
        print(f"Filled {name} with {amount}. Current amount: {resources[name]}")
    else:
        print("Invalid resource")


power_on = True
maintenance_mode = False
while power_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "maintenance":
        password = input("Enter password: ")
        if login(password):
            maintenance_mode = True
            while maintenance_mode:
                maintenance = input("Maintenance mode enabled. What would you like to do? (fill/report/exit):").lower()
                if maintenance == "fill":
                    fill = input("What would you like to fill? (water/milk/coffee)")
                    amount = int(input("How much would you like to add?"))
                    fill_machine(fill, amount)
                elif maintenance == "report":
                    print(f"Water: {resources['water']}ml")
                    print(f"Milk: {resources['milk']}ml")
                    print(f"Coffee: {resources['coffee']}g")
                    print(f"Money: €{resources['money']}")
                    print(f"Profit: €{profit}")
                elif maintenance == "exit":
                    maintenance_mode = False
        else:
            print("Wrong password.")
    elif choice == "off":
        power_on = False
    else:
        if choice in MENU:
            strength = input("What strength would you like? (normal/strong)").lower()
            if strength in strengths:
                beverage = MENU[choice]
                if enough_resources(beverage["ingredients"], strength):
                    money = payment_transaction()
                    if transaction_succesfull(strength, money, beverage["cost"]):
                        create_drink(choice, beverage["ingredients"])
            else:
                print("No such strength.")
        else:
            print("No such option.")