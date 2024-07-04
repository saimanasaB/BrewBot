# coffee_machine.py

from coffee_machine_data import MENU, RESOURCES, COIN_VALUES

resources = RESOURCES.copy()
money = 0.0

def is_resource_sufficient(order_ingredients):
    """Check if there are enough resources to make the coffee."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Process coins inserted by the user and return the total."""
    print("Please insert coins.")
    total = 0
    for coin, value in COIN_VALUES.items():
        while True:
            try:
                count = int(input(f"How many {coin}? "))
                if count < 0:
                    raise ValueError("Number of coins cannot be negative.")
                total += count * value
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid number.")
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True if the payment is accepted, or False if it is insufficient."""
    if money_received >= drink_cost:
        global money
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        money += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

def refill_resources():
    """Refill the resources."""
    for item in resources:
        while True:
            try:
                addition = int(input(f"How much {item} would you like to add? "))
                if addition < 0:
                    raise ValueError("Amount cannot be negative.")
                resources[item] += addition
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid number.")

def report():
    """Print the current resource values."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")

def coffee_machine():
    """Main function to run the coffee machine."""
    is_on = True

    while is_on:
        print("\nOptions: espresso, latte, cappuccino, report, refill, off")
        choice = input("What would you like? ").lower()
        if choice == "off":
            is_on = False
        elif choice == "report":
            report()
        elif choice == "refill":
            refill_resources()
        elif choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("Invalid choice, please choose again.")

if __name__ == "__main__":
    coffee_machine()
