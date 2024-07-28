# TODO 2 CHECK RESOURCES ARE SUFFICIENT TO ORDER

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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


#TODO 1 priint coffe machine resources

profits=0
def report(mc_resources, money):
    print(f"Water: {mc_resources["water"]}")
    print(f"Milk: {mc_resources["milk"]}")
    print(f"Coffee: {mc_resources["coffee"]}")
    print(f"Money: {money}")

def calculate_change(qua, dime, nickel, penny, drink_cost):
    qua = .25*qua
    dime = .1*dime
    nickel = .05*nickel
    penny = .01*penny
    money_received = qua+dime+nickel+penny
    if money_received > drink_cost:
        change = money_received-drink_cost
        print(f"Here's your change of {change}")
        global profits
        profits +=drink_cost
        return True
    else:
        print("Money is not sufficient. Money Refunded")
        return False
def make_coffee(drink_ordered, resources):
    for item in drink_ordered:
        resources[item] -= drink_ordered[item]



def sufficient_ingredients(drink_given, resources_given):
    for item in drink_given["ingredients"]:
        if resources_given[item]<drink_given["ingredients"][item]:
            print(f"Sorry there is not enough {item}!")




machine = True


while machine:
    drink_ordered= input("What will you like to have? (espresso/latte/cappuccino) ")
    if drink_ordered=="OFF":
        machine= False

    elif drink_ordered=="report":
        report(resources, profits)
    else:
        drink = MENU[drink_ordered]
        print("Please Insert coins: ")
        quarters = int(input("How many Quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickles? "))
        pennies = int(input("How many pennies? "))
        a= calculate_change(quarters, dimes, nickels, pennies, MENU[drink_ordered]["cost"])

        if a:
            make_coffee(drink["ingredients"], resources)
            print(f"Enjoy your {drink_ordered}!")

