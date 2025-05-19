import art

def add(n1,n2):
	return n1+n2
def substraction(n1,n2):
	return n1+n2
def multiply(n1,n2):
	return n1*n2
def divide(n1,n2):
	return n1 / n2
operations = {
    "+": add ,
	"-":substraction,
	"*": multiply,
	"/":divide
}
def calculator ():
	should_Accumulate = True
	print(art.logo)
	number1 = float(input("What's the first number?: "))
	while should_Accumulate:
		for symbol in operations:
			print(symbol)
		operator = input(" Pick an operation: ")
		number2 = float(input("What's the next number?:"))
		result = operations[operator](number1, number2)
		print(result)
		choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
		if choice == "y":
			number1 = result
		else:
			should_Accumulate = False
			print("\n "*20)
			calculator()
calculator()