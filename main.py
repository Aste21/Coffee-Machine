MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {money}$")


def check_resources(coffee_type):
    if coffee_type == 'espresso':
        if resources['water'] > 50 and resources['coffee'] > 18:
            return True
        else:
            return False
    if coffee_type == 'latte':
        if resources['water'] > 200 and resources['coffee'] > 24 and resources['milk'] > 150:
            return True
        else:
            return False
    if coffee_type == 'cappuccino':
        if resources['water'] > 250 and resources['coffee'] > 24 and resources['milk'] > 100:
            return True
        else:
            return False
    else:
        return False


def coins(c):
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    user_money = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
    if user_money >= cost:
        change = round((user_money - cost), 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def resources_deduction(water, milk, coffee):
    resources['water'] -= water
    resources['milk'] -= milk
    resources['coffee'] -= coffee

def check_resorces(water, milk, coffee):
    if water>resources['water']:
        return 'water'
    elif milk>resources['milk']:
        return 'milk'
    elif coffee>resources['coffee']:
        return 'coffee'

again = True
while again:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        again = False
    elif choice == 'report':
        report()
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        water = MENU[choice]['ingredients']['water']
        coffee = MENU[choice]['ingredients']['coffee']
        milk = MENU[choice]['ingredients']['milk']
        cost = MENU[choice]['cost']
        if check_resources(choice):
            do_coins = coins(cost)
            if do_coins:
                money += cost
                resources_deduction(water, milk, coffee)
                print(f"Here is your {choice} ☕️. Enjoy!")
        else:
            print(f"Sorry the is not enough {check_resorces(water, milk, coffee)}.")
    else:
        print(f"Sorry '{choice}' is not a valid input.")

