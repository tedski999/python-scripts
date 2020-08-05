# A financal program to help deal with pizza #
# on a Saturday night in St. Columbas.       #

# Libraries
import os
import msvcrt as m

# Global variables
customers = []
total_price = 0
total_payed = 0
maxNameLength = 20

# Classes
class c:
	RED = '\033[0;31;40m'
	GREEN = '\033[0;32;40m'
	YELLOW = '\033[0;33;40m'
	BLUE = '\033[0;34;40m'
	PURPLE = '\033[0;35;40m'
	CYAN = '\033[0;36;40m'
	WHITE = '\033[0;37;40m'

class Customer(object):
	def __init__(self, new_name, new_total_price):
		self.name = new_name
		self.total_price = new_total_price
		self.payed = "0"

# Functions
def Color(color):
	print(color, end="")

def RepeatCharacter(char, repeats):
	for n in range(repeats):
		print(char, end = '')

def PrintCustomerNumbers():
	Color(c.YELLOW)
	for n in range(len(customers)):
		print(" " + str(n+1) + ". " + customers[n].name + " ", end = '')
		RepeatCharacter('.', maxNameLength - len(customers[n].name))
		print(" €" + customers[n].total_price + " ", end = '')
		RepeatCharacter('.', int(maxNameLength / 2) - len(customers[n].total_price))
		print(" €" + customers[n].payed, end = '')
		RepeatCharacter('.', int(maxNameLength / 2) - len(customers[n].payed))
		print(" €" + str(float(customers[n].total_price) - float(customers[n].payed)))

def Title():
	Color(c.WHITE)
	print("\n .------------------------------.")
	print(" | Pizza Night Money Calculator |")
	print(" '------------------------------'\n")

def NewCustomer():
	os.system("cls")
	Title()

	Color(c.WHITE)
	print(" New Customer Setup\n")

	Color(c.GREEN)
	name = input(" Name: ")
	costs = input(" Amount Owed: €")

	try:
		foo = float(costs)
		customers.append(Customer(name, costs))
	except Exception as e:
		Color(c.RED)
		print("\n Thats not a number!")
		m.getch()

def Payment():
	os.system("cls")
	Title()

	Color(c.WHITE)
	print(" Lodging Payment\n")
	PrintCustomerNumbers()

	Color(c.GREEN)
	num = input("\n Customer Number: ")
	try:
		num = int(num) - 1
		if (num >= len(customers)):
			raise ValueError("Bad Number")
		if (num < 0):
			raise ValueError("Bad Number")
		else:
			payment = input(" Amount Payed: €")
			foo = float(payment)
			customers[num].payed = str(float(customers[num].payed) + float(payment))

	except Exception as e:
		Color(c.RED)
		print("\n Thats not a valid number!")
		m.getch()

def EditCustomer():
	os.system("cls")
	Title()

	Color(c.WHITE)
	print(" Editing Customer\n")
	Color(c.YELLOW)
	PrintCustomerNumbers()
	
	Color(c.GREEN)
	num = input("\n Customer Number: ")
	try:
		num = int(float(num) - 1)
		if (num >= len(customers)):
			raise ValueError("Bad Number")
		if (num < 0):
			raise ValueError("Bad Number")
		else:
			customers[num].name = input(" New Name: ")
			new_total_price = input(" New Amount Owed: €")
			foo = float(new_total_price)
			customers[num].total_price = new_total_price

	except Exception as e:
		Color(c.RED)
		print("\n Thats not a valid number!")
		m.getch()

def DeleteCustomer():
	os.system("cls")
	Title()

	Color(c.WHITE)
	print(" Deleting Customer\n")
	Color(c.YELLOW)
	PrintCustomerNumbers()

	Color(c.GREEN)
	num = input("\n Customer Number: ")
	try:
		num = int(num) - 1
		if (num >= len(customers)):
			raise ValueError("Bad Number")
		if (num < 0):
			raise ValueError("Bad Number")
		else:
			customers.pop(num)

	except Exception as e:
		Color(c.RED)
		print("\n Thats not a valid number!")
		m.getch()

NewCustomer()
# Main Loop
while True:
	os.system("cls")
	Title()

	total_price = 0
	total_payed = 0

	Color(c.WHITE)
	print(" +- Name ---------------+- Paying ----+- Payed ----+- Balance -----+")
	Color(c.YELLOW)
	for n in range(len(customers)):
		print(" | " + customers[n].name + " ", end = '')
		RepeatCharacter('.', maxNameLength - len(customers[n].name))
		print("| €" + customers[n].total_price + " ", end = '')
		RepeatCharacter('.', int(maxNameLength / 2) - len(customers[n].total_price))
		print("| €" + customers[n].payed, end = '')
		RepeatCharacter('.', int(maxNameLength / 2) - len(customers[n].payed))
		print("| €" + str(float(customers[n].total_price) - float(customers[n].payed)), end = '')
		RepeatCharacter('.', int(maxNameLength / 2) - len(customers[n].payed))
		print("|")

		total_price += float(customers[n].total_price)
		total_payed += float(customers[n].payed)
	
	Color(c.WHITE)
	print(" +----------------------+-------------+------------+---------------+\n")

	Color(c.CYAN)
	print(" Amount Payed: €" + str(total_payed))
	print(" Total Price: €" + str(total_price))

	Color(c.PURPLE)
	print("\n N - New Customer")
	print(" P - Payment")
	print(" E - Edit Customer")
	print(" D - Delete Customer\n")

	Color(c.GREEN)
	newInput = input("> ")
	newInput = newInput.lower()

	if (newInput == "n"):
		NewCustomer()
	elif (newInput == "p"):
		Payment()
	elif (newInput == "e"):
		EditCustomer()
	elif (newInput == "d"):
		DeleteCustomer()
	else:
		Color(c.RED)
		print("\n Invalid Command!")
		m.getch()
