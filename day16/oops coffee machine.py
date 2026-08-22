# ──────────────────────────────────────────────
#  OOP Coffee Machine
# ──────────────────────────────────────────────

class MenuItem:
    """Represents a single drink item on the menu."""

    def __init__(self, name, water, milk, coffee, cost):
        self.name   = name
        self.water  = water   # ml
        self.milk   = milk    # ml
        self.coffee = coffee  # g
        self.cost   = cost    # $


class Menu:
    """Holds all available drinks and provides lookup."""

    def __init__(self):
        self.drinks = {
            "espresso":   MenuItem("espresso",   50,   0,  18, 1.5),
            "latte":      MenuItem("latte",      200, 150,  24, 2.5),
            "cappuccino": MenuItem("cappuccino", 250, 100,  24, 3.0),
        }

    def get_items(self):
        """Return a slash-separated string of drink names."""
        return "/".join(self.drinks.keys())

    def find_drink(self, name):
        """Return the MenuItem if found, else None."""
        return self.drinks.get(name.lower())


class MoneyMachine:
    """Handles all coin processing and profit tracking."""

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes":    0.10,
        "nickles":  0.05,
        "pennies":  0.01,
    }

    def __init__(self):
        self.profit = 0.0   # total money earned by the machine

    def report(self):
        print(f"Money: ${self.profit:.2f}")

    def process_coins(self):
        """Ask the user to insert coins and return the total amount."""
        print("Please insert coins.")
        total = 0.0
        for coin, value in self.COIN_VALUES.items():
            count = int(input(f"  How many {coin}? "))
            total += count * value
        return round(total, 2)

    def make_payment(self, cost):
        """
        Ask for coins, check if payment is sufficient.
        Returns True on success (profit updated), False on failure.
        """
        received = self.process_coins()

        if received < cost:
            print(f"Sorry that's not enough money. Money refunded.")
            return False

        change = round(received - cost, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")

        self.profit += cost
        return True


class CoffeeMachine:
    """Manages machine resources and orchestrates the drink-making flow."""

    def __init__(self):
        self.resources = {
            "water":  300,  # ml
            "milk":   200,  # ml
            "coffee": 100,  # g
        }
        self.menu         = Menu()
        self.money_machine = MoneyMachine()
        self.is_on        = True

    def report(self):
        """Print current resource and money levels."""
        print(f"Water:  {self.resources['water']}ml")
        print(f"Milk:   {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        self.money_machine.report()

    def is_resource_sufficient(self, drink):
        """Check whether the machine has enough ingredients."""
        needs = {
            "water":  drink.water,
            "milk":   drink.milk,
            "coffee": drink.coffee,
        }
        for item, amount in needs.items():
            if self.resources[item] < amount:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_coffee(self, drink):
        """Deduct ingredients and serve the drink."""
        self.resources["water"]  -= drink.water
        self.resources["milk"]   -= drink.milk
        self.resources["coffee"] -= drink.coffee
        print(f"Here is your {drink.name}. Enjoy! ☕")

    def start(self):
        """Main loop — keeps prompting until turned off."""
        while self.is_on:
            choice = input(f"\nWhat would you like? ({self.menu.get_items()}): ").strip().lower()

            if choice == "off":
                print("Turning off the coffee machine. Goodbye!")
                self.is_on = False

            elif choice == "report":
                self.report()

            else:
                drink = self.menu.find_drink(choice)
                if drink is None:
                    print(f"'{choice}' is not on the menu. Please choose from: {self.menu.get_items()}")
                elif self.is_resource_sufficient(drink):
                    if self.money_machine.make_payment(drink.cost):
                        self.make_coffee(drink)


# ──────────────────────────────────────────────
#  Run the machine
# ──────────────────────────────────────────────
if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.start()
