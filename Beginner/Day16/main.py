from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
monet_machine = MoneyMachine()
coffe = CoffeeMaker()
menu = Menu()
is_on =True
while is_on:
	options = menu.get_items()
	choice = input(f"what would you like? {options}:")
	if choice == "off".lower():
		is_on = False
	elif choice == "report":
		coffe.report()
		monet_machine.report()
	else:
		drink = menu.find_drink(choice)
		if coffe.is_resource_sufficient(drink) and  monet_machine.make_payment(drink.cost):
			coffe.make_coffee(drink)