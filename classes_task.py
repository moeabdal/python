import datetime
today = datetime.date.today()

class Employee(object):
	def __init__(self, name, age, salary, employment_date):
		self.name = name
		self.age = age
		self.salary = float(salary)
		self.employment_date = int(employment_date)
	def get_working_years(self):
		working_years = today.year - self.employment_date
		return working_years
	def __repr__(self):
		return "Name: %s, Age: %s, Salary: %.3fKD, Working years: %s" % (self.name.title(), self.age, self.salary, self.get_working_years())
	

class Manager(Employee):
	def __init__(self, name, age, salary, employment_date, bonus_percentage):
		Employee.__init__(self, name, age, salary, employment_date)
		self.bonus_percentage = bonus_percentage
	
	def get_bonus(self):
		bonus = float(self.bonus_percentage) * int(self.salary)
		return bonus
	def __repr__(self):
		return "Name: %s, Age: %s, Salary: %.3fKD, Working years: %s, Bonus: %.3fKD" % (self.name.title(), self.age, self.salary, self.get_working_years(), self.get_bonus())

emplist = []
manlist = []

print (" ")
print ("\tWelcome to HR pro 2019")


while True:
	print ("\tChoose one of the following options: \n\t\t 1. Show employees \n\t\t 2. Show managers \n\t\t 3. Add an employee \n\t\t 4. Add a manager \n\t\t 5. Exit")
	action = input("\n What would you like to do? ")
	
	if action == "1":
		if len(emplist) == 0:
			print ("\n\t Please add employee first.\n")
		else:
			print (" ")
			print (emplist)
			print(" ")
	
	elif action == "2":
		if len(manlist) == 0:
			print ("\n\tPlease add manager first.\n")
		else:
			print (" ")
			print (manlist)
			print (" ")
	
	elif action == "3":
		print (" ")
		name = input("Enter name: ")
		age = input("Enter age: ")
		salary = input("Enter salary: ")
		employment_date = input("Enter employment year: ")
		empinst = Employee(name, age, salary, employment_date)
		emplist.append(empinst)
		

		print ("\n\tEmployee added successfully.\n")
	
	elif action == "4":
		print (" ")
		name = input("Enter name: ")
		age = input("Enter age: ")
		salary = input("Enter salary: ")
		employment_date = input("Enter employment year: ")
		bonus_percentage = input("Enter bonus percentage: ")
		maninst = Manager(name, age, salary, employment_date, bonus_percentage)
		manlist.append(maninst)
		
		print ("\n\tManager added successfully.\n")
	
	elif action == "5":
		print ("\n\tThank you for using HR pro 2019.\n")
		break
	else:
		print ("\n\tInvalid input.\n")


