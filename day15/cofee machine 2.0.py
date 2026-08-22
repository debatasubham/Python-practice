"""
Coffee Machine 2.0 - OOP Version
Requirements:
1. Prompt "What would you like? (espresso/latte/cappuccino):" - loops after every action
2. "off"    -> turns off the machine
3. "report" -> prints Water, Milk, Coffee, Money
4. Check resources sufficient -> "Sorry there is not enough <resource>."
5. Process coins -> quarters/dimes/nickels/pennies
6. Check transaction -> "Sorry that's not enough money. Money refunded." OR add to profit
7. Make coffee -> "Here is your <drink>. Enjoy!"
"""


# ─────────────────────────────────────────────
#  Class 1: MenuItem
# ─────────────────────────────────────────────
class MenuItem:
    """Represents one item on the menu (name, cost, ingredients)."""

    def __init__(self, name, water, milk, coffee, cost):
        self.name        = name
        self.cost        = cost
        self.ingredients = {
            "water":  water,
            "milk":   milk,
            "coffee": coffee,
        }


# ─────────────────────────────────────────────
#  Class 2: Menu
# ─────────────────────────────────────────────
class Menu:
    """Holds all drinks and finds a drink by name."""

    def __init__(self):
        self.menu = [
            MenuItem(name="espresso",   water=50,  milk=0,   coffee=18, cost=1.5),
            MenuItem(name="latte",      water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=3.0),
        ]

    def get_items(self):
        """Returns 'espresso/latte/cappuccino' string for the prompt."""
        return "/".join(item.name for item in self.menu)

    def find_drink(self, order_name):
        """Returns the matching MenuItem or None."""
        for item in self.menu:
            if item.name == order_name:
                return item
        return None


# ─────────────────────────────────────────────
#  Class 3: CoffeeMaker
# ─────────────────────────────────────────────
class CoffeeMaker:
    """Manages resources and makes the coffee."""

    def __init__(self):
        self.resources = {
            "water":  300,   # ml
            "milk":   200,   # ml
            "coffee": 100,   # g
        }

    def report(self):
        """Prints resource levels exactly as required."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """
        Checks if enough resources exist for the drink.
        Prints "Sorry there is not enough <resource>." if not.
        Returns True if all resources are OK.
        """
        for ingredient, amount_needed in drink.ingredients.items():
            if self.resources[ingredient] < amount_needed:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return True

    def make_coffee(self, drink):
        """Deducts resources and serves the drink."""
        for ingredient, amount in drink.ingredients.items():
            self.resources[ingredient] -= amount
        print(f"Here is your {drink.name}. Enjoy!")


# ─────────────────────────────────────────────
#  Class 4: MoneyMachine
# ─────────────────────────────────────────────
class MoneyMachine:
    """Processes coins, validates payment, tracks profit."""

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes":    0.10,
        "nickels":  0.05,
        "pennies":  0.01,
    }

    def __init__(self):
        self.profit = 0.0

    def report(self):
        """Prints money earned."""
        print(f"Money: ${self.profit}")

    def process_coins(self):
        """Asks how many of each coin and returns the total amount inserted."""
        print("Please insert coins.")
        total = 0
        for coin, value in self.COIN_VALUES.items():
            try:
                count = int(input(f"How many {coin}?: "))
            except ValueError:
                count = 0
            total += count * value
        return round(total, 2)

    def make_payment(self, cost):
        """
        Collects coins and checks if payment >= cost.
        - If not enough: prints "Sorry that's not enough money. Money refunded."
        - If enough: gives change, adds cost to profit, returns True.
        """
        received = self.process_coins()
        if received < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        change = round(received - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        self.profit = round(self.profit + cost, 2)
        return True


# ─────────────────────────────────────────────
#  Main Program
# ─────────────────────────────────────────────
def main():
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    is_on = True

    while is_on:
        choice = input(f"What would you like? ({menu.get_items()}): ").lower()

        if choice == "off":
            # Secret word for maintainers – ends execution
            is_on = False

        elif choice == "report":
            # Print current resource levels + money
            coffee_maker.report()
            money_machine.report()

        else:
            drink = menu.find_drink(choice)
            if drink:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
