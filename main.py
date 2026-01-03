from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
OFF = False

anskaf = Menu()

kaffen = CoffeeMaker()

espresso = MenuItem("espresso", 50, 0, 18, 1.5)

latte = MenuItem("latte", 200, 150, 24, 2.5)

cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

betaling = MoneyMachine()


while not OFF:
    svar = str(input(f"What would you like? ({anskaf.get_items()}): ").lower())

    if svar == "report":
        kaffen.report()
        betaling.report()
    elif svar == "espresso":
        if  kaffen.is_resource_sufficient(espresso) and betaling.make_payment(1.5):
            kaffen.make_coffee(espresso)
    elif svar == "latte":
        if kaffen.is_resource_sufficient(latte) and betaling.make_payment(2.5):
            kaffen.make_coffee(latte)
    elif svar == "cappuccino":
        if kaffen.is_resource_sufficient(cappuccino) and betaling.make_payment(3.0):
            kaffen.make_coffee(cappuccino)
    elif svar == "off":
        OFF = True
    else:
        anskaf.find_drink(latte)

