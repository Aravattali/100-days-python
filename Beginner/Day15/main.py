from importlib.resources import is_resource

from astroid.brain.brain_builtin_inference import infer_getattr

MENU ={
	"Espresso":{
		'ingredients':{
			"water":50,
			"coffe": 18
		},
		"cost": 1.5
	},
	"latte":{
		"ingredients":{
			"water":200,
			"milk":150,
			"coffe":24
		},
		"cost":2.5
	},
	"capuccino":{
		'ingredients':{
			"water":250,
			"milk":100,
			"coffe":24
		},
		"cost": 3,
	}
}

profit = 0
resources = {
	 "water" :300,
     "milk":200,
     "coffe":100
 }

def is_resource_sufficient(order_ingredients):
	"""returns True when order can be made , False when ingredients are insufficient."""
	for item in order_ingredients:
		if order_ingredients[item]>= resources[item]:
			print(f"sorry , there is no enough  {item}.")
			return False
	return True

def process_coins():
	"""returns the total calculated from inserted coins"""
	print("please insert coins. ")
	total = int(input("how many quarters?:")) * 0.25
	total += int(input("how many dimes?:")) * 0.1
	total += int(input("how many nickles?:")) * 0.05
	total += int(input("how many pennies?:")) * 0.01
	return total

def is_transaction_succesfull (money_recieved , drink_cost):
	"""returns True if payment is accepted or False if money is insufficient."""
	if money_recieved >= drink_cost:
		change = round(money_recieved - drink_cost , 2)
		print(f"here is ${change}  in change.")
		global profit
		profit += drink_cost
		return True
	else:
		print("Sorry! , that's not enough money. money is refunded. ")
		return  False

def make_coffe (drink_name , order_ingredients):
	"""it deducts ingredients from resources."""
	for item in order_ingredients:
		resources[item]-= order_ingredients[item]
		print(f"here is your {drink_name} ")


is_on = True

while is_on :
	choice = input("what would like? Espresso / Latte / Capuccino ").lower()
	if choice == "off":
		is_on = False
	elif choice == 'report':
		print(f"water {resources['water']}ml ")
		print(f"milk {resources['milk']}ml")
		print(f"coffe {resources['coffe']}g")
		print(f"money ${profit}")
	else:
		drink = MENU[choice]
		if is_resource_sufficient(drink['ingredients']):
			payment = process_coins()
		if 	is_transaction_succesfull(payment , drink['cost']):
			make_coffe(choice, drink['ingredients'])


