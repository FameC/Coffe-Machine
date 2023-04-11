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



def extract_resources():
    if choice == "latte" or choice == "cappuccino":
        water = MENU[choice]["ingredients"]["water"]
        milk = MENU[choice]["ingredients"]["milk"]
        coffee = MENU[choice]["ingredients"]["coffee"]
        cost = MENU[choice]["cost"]

        return water, milk, coffee, cost
    elif choice == "espresso":
        water = MENU[choice]["ingredients"]["water"]
        coffee = MENU[choice]["ingredients"]["coffee"]
        cost = MENU[choice]["cost"]

        return water, coffee, cost
    elif choice == "off":
        return False



def check_resources():
    if choice == "latte" or choice == "cappuccino":
        water, milk, coffee, cost = extract_resources()
    elif choice == "espresso":
        water, coffee, cost = extract_resources()

    if choice == "latte":
        if resources["water"] >= water:
            if resources["milk"] >= milk:
                if resources["coffee"] >= coffee:
                    return True
                else:
                    print(f"Sorry there is not enough coffee")
                    return False
            else:
                print(f"Sorry there is not enough milk ")
                return False
        else:
            print(f"Sorry there is not enough water")
            return False

    if choice == "cappuccino":
        if resources["water"] >= water:
            if resources["milk"] >= milk:
                if resources["coffee"] >= coffee:
                    return True
                else:
                    print(f"Sorry there is not enough coffee ")
                    return False
            else:
                print(f"Sorry there is not enough milk ")
                return False
        else:
            print(f"Sorry there is not enough water")
            return False

    if choice == "espresso":
        if resources["water"] >= water:
            if resources["coffee"] >= 24:
                return True
            else:
                print(f"Sorry there is not enough coffee ")
                return False
        else:
            print(f"Sorry there is not enough water")
            return False
    return False

# def process_coins(quarters, dimes, nickles, pennies):


cost_of_espresso = MENU["espresso"]["cost"]
cost_of_latte = MENU["latte"]["cost"]
cost_of_cappuccino = MENU["cappuccino"]["cost"]
resources["money"] = 0
tracker = True

while tracker:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    # print(extract_resources())
    if choice == "report":
        for item in resources:
            print(f"{str(item).upper()}: {resources[item]}")
        continue
    if check_resources():
        print("Please insert coins:")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        total_amount = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
        print(total_amount)

        if choice == "latte" and total_amount > cost_of_latte:
            water, milk, coffee, cost = extract_resources()
            resources["water"] -= water
            resources["milk"] -= milk
            resources["coffee"] -= coffee
            resources["money"] += cost
            balance = round(total_amount - cost_of_latte, 2)
            print(f"Here is your change {balance}")
            print("Here is your latte. Enjoy!")
        elif choice == "cappuccino" and total_amount > cost_of_cappuccino:
            water, milk, coffee, cost = extract_resources()
            resources["water"] -= water
            resources["milk"] -= milk
            resources["coffee"] -= coffee
            resources["money"] += cost
            balance = round(total_amount - cost_of_cappuccino, 2)
            print(f"Here is your change {balance}")
            print("Here is your cappuccino. Enjoy!")
        elif choice == "espresso" and total_amount > cost_of_espresso:
            water, coffee, cost = extract_resources()
            resources["water"] -= water
            resources["coffee"] -= coffee
            resources["money"] += cost
            balance = round(total_amount - cost_of_espresso, 2)
            print(f"Here is your change {balance}")
            print("Here is your espresso. Enjoy!")
        # elif choice == "report":
        #     for item in resources:
        #         print(f"{str(item).upper()}: {resources[item]}")
        #         continue
        elif choice == "off":
            tracker = False



    else:
        #print("Not enough resources ..")
        tracker = False













