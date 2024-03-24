
from art import logo
menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5
    },

    "latte": {
        "ingredients": {
            "water": 50,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },

    "cappuccino": {
        "ingredients": {
            "water": 50,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_is_sufficient(order_ingredients):
    for key in order_ingredients:
        if resources[key] < order_ingredients[key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True


def transaction_is_successful(cost):
    print(f"The total cost of your coffee is: {cost}")
    payment = float(input("Make a payment: "))
    if payment == cost:
        print("Your payment is successful....")
        return True
    elif payment > cost:
        print(f"Take this change: {payment - cost}")
        return True
    else:
        print("insufficient Money")
        return False


def make_a_coffee(choice, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {choice} ☕️. Enjoy!")

print("Welcome to the Coffee Machine......")
print(logo)
is_on = True
while is_on:
    user_choice = input("what would you like? (latte/espresso/cappuccino): ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}gm")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = menu[user_choice]
        if resources_is_sufficient(drink["ingredients"]):
            if transaction_is_successful(drink["cost"]):
                profit += drink["cost"]
                make_a_coffee(user_choice, drink["ingredients"])
