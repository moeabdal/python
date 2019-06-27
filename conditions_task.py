print ("This is a calculator.")

num1 = input("Please enter a number: ")
num2 = input("Please enter another number: ")
op = input("Please enter an operation such as +, -, * or /: ")

if num1.isnumeric() and num2.isnumeric():
	if op == "+":
		print (int(num1) + int(num2))
	elif op == "-":
		print (int(num1) - int(num2))
	elif op == "*":
		print (int(num1) * int(num2))
	elif op == "/":
		print (int(num1) / int(num2))
	else:
		print ("Invalid operation")
else: print ("The numbers were invalid.")


