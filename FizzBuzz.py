import os

replacementNumbers = []
replacementText = []

# ------ FUNCTIONS ------- #

def InputNewReplacements():
	os.system("cls")
	print("Enter number to replace and text to replace with.")
	print("Example - '3 Fizz'")
	print("Leave blank to perform operation.\n")
	PrintReplacements()
	print("\n----------")
	newInput = input("> ")

	if newInput != "":
		inputData = newInput.split()
		replacementNumbers.append(int(inputData[0]))
		replacementText.append(inputData[1])
		InputNewReplacements()

def PrintReplacements():
	print("Current Items:")
	for i in range(len(replacementNumbers)):
		print(str(replacementNumbers[i]) + " = " + replacementText[i])

# ------ START POINT -------- #

# Input start and end numbers #
startNumber = int(input("Start Number: "))
endNumber = int(input("End Number: "))

# Saftey Check #
if startNumber >= endNumber+1:
	input("Invalid start and end numbers entered.")
	exit()

# Input new items #
InputNewReplacements()

# -------- OPERATION -------- #

for i in range((endNumber+1)-startNumber):
	text = ""

	for d in range(len(replacementNumbers)):
		if (i+startNumber) % replacementNumbers[d] == 0:
			text += replacementText[d]

	if text == "":
		text = str(i+startNumber);

	print(text)

input("Complete!")