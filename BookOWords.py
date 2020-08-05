# A Library of Babel clone.                    #
# Creates a pseudo-random page of text based   #
# on the characters page and character number. #
# Ted Johnson - 23/01/18                       #               

# Imports libraries
import os
import random
import math

# Sets search type
while True:
	os.system("cls")
	print("0 - Slower, but estimates line search is located.")
	print("1 - Faster (x2), no line estimate.")
	try:
		searchType = float(input("Search Type: ")) # 0 - Slow or 1 - Fast
		if searchType == 0 or searchType == 1:
			break
	except Exception as e:
		pass

# Sets book
while True:
	os.system("cls")
	
	try:
		bookNum = float(input("Book number: "))
		if bookNum >= 1:
			bookNum = math.floor(bookNum)
			break
	except Exception as e:
		pass

# Variables
page = 1
linesPerPage = 20
charsPerLine = 40
chars = [
'a','b','c','d','e','f','g','h','i','j',
'k','l','m','n','o','p','q','r','s','t',
'u','v','w','x','y','z','.',',',' ']

while True:
	os.system("cls")
	page = math.floor(page)
	if page < 1:
		page = 1

	random.seed(page+bookNum)

	print("Page ", end = '')
	print(page, end = '')
	print(" in Book ", end = '')
	print(bookNum)

	# Prints a page
	for l in range(linesPerPage):

		# Numbers lines
		if l < 9:
			print(math.floor(float(l))+1, end = ".  ")
		elif l < 99:
			print(math.floor(float(l))+1, end = ". ")
		else:
			print(math.floor(float(l))+1, end = ".")

		# Prints chars on this line
		for c in range(charsPerLine):
			print(chars[random.randrange(len(chars))], end = '')

		# Next line
		print()

	# Input
	search = input("\nSearch or Page Number: ")
	
	# Is it a search or a page number?
	try:
		# Sets page
		page = float(search)

	except Exception as e:

		# List of chars
		searchResults = []

		# Variables
		curPage = 1
		curChar = 0
		random.seed(curPage)

		print("Searching...")

		# Repeat till search found
		while True:

			# ---- SLOW SEARCH ----
			if searchType == 0:
				# Increment curChar
				curChar += 1

				# If curChar is past end of page
				if curChar > charsPerLine * linesPerPage:

					# Reset, move to next page
					curChar = 1
					curPage += 1
					searchResults = []
					random.seed(curPage+bookNum)

					# Informs user
					print("Searching for '", end = '')
					print(search, end = '')
					print("' on page ", end = '')
					print(curPage)

				# Adds char to list
				searchResults += chars[random.randrange(len(chars))]

				# Removes oldest char if needed
				if (len(searchResults) > len(search) + 1):
					searchResults.pop(0)

			if searchType == 1:
				searchResults = []
				for c in range(charsPerLine * linesPerPage):
					searchResults += chars[random.randrange(len(chars))]

		    # ---- COMMON ----
			# Is the search term in the list?
			if search in ''.join(searchResults):

				# Informs user
				os.system("cls")
				print("Found '", end = '')
				print(search, end = '')
				print("' on page ", end = '')
				print(curPage, end = '')

				# Estimates line
				if searchType == 0:
					print(", line ", end = '')
					print(math.floor((curChar) / charsPerLine))

				input()

				# Sets page and returns
				page = curPage
				break

			# ---- FAST SEARCH ----
			if searchType == 1:

				# Next page
				curPage += 1
				random.seed(curPage)