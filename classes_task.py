import datetime
today = datetime.date.today()

class Employee:
	def __init__(self, name, age, salary, employment_date):
		self.name = input("Enter name: ")
		self. age = input("Enter age: ")
		self.salary = input("Enter salary: ")
		self.employment_date = ("Enter employment year: ")
	def get_working_years(self):
		working_years = today.year - employment_date
		return working_years
	def __str__(self):
		return Employee("Name: %s, Age: %s, Salary: %s, Working years: %s" % (self.name, self.age, self.salary, working_years))

class Manager:
	def __init__(self, name, age, salary, employment_date, bonus_percentage):
		self.name = name
		self.age = age
		self.salary = salary
		self.employment_date = employment_date
		self.bonus_percentage = bonus_percentage
	def get_working_years(self):
		working_years = today.year - employment_date
		return working_years
	def get_bonus(self):
		bonus = bonus_percentage * salary
		return bonus

emplist = []
manlist = []


print ("Welcome to HR pro 2019")



while True:
	print ("Choose one of the following options: \n\t 1. Show employees \n\t 2. Show managers \n\t 3. Add an employee \n\t 4. Add a manager \n\t 5. Exit")
	action = input("\n What would you like to do? ")
	if action == "1":
		if len(emplist) == 0:
			print ("\n Please add employee first.\n")
		else:
			print (emplist)
	elif action == "2":
		if len(manlist) == 0:
			print ("\n Please add manager first.\n")
		else:
			print (manlist)
	elif action == "3":
		Employee()
		print ("Employee added successfully.")
	elif action == "4":
		input("Enter name: ").append(manlist)
		input("Enter age: ").append(manlist)
		input("Enter salary: ").append(manlist)
		input("Enter year: ").date.year.append(manlist)
		float(input("Enter bonus: ").append(manlist))
		print ("Manager added successfully.")
	elif action == "5":
		break
	else:
		print ("Invalid input.")


