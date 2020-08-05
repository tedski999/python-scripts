# A fair blackjack game against several AI opponents.  #
# Instead of just giving the AI a random number at the #
# end of the round, there is a deck of cards that are  #
# randomly dealed out.                                 #
# Ted Johnson - 17/02/18                               #

# --- Libraries --- #

import os, random, sys

if sys.platform[:3] == "win":
	import msvcrt as m
	clearCmd = "cls"
elif sys.platform[:3] == "lin":
	import getch as m
	clearCmd = "clear"
else:
	raise OSError("I'm sorry but your operating system is not supported. Please use either Windows or Linux.")

# --- Variables --- #

CEND    = "\33[0m"
CRED    = "\33[31m"
CGREEN  = "\33[32m"
CYELLOW = "\33[33m"
CBLUE   = "\33[34m"
CVIOLET = "\33[35m"
CBEIGE  = "\33[36m"
CWHITE  = "\33[37m"

cards = []
aiPlayers = []
allHolding = False
tempNames = []
exiting = False

line = "       +------------------------------------------------------+"
gap =  "       |                                                      |"
leftMargin = "       | "
title =  (CRED + "             ___  _    ____ ____ _  _  _ ____ ____ _  _  \n" +
		 "             |__] |    |__| |    |_/   | |__| |    |_/   \n" +
		 "             |__] |___ |  | |___ | \_ _| |  | |___ | \_  \n" +
		 "             ==========================================    " + CEND)
credits = CRED + "                                     Ted Johnson - 2018\n\n" + CEND

numAIPlayers = 0
while numAIPlayers not in range(1, 9):
	os.system(clearCmd)
	print(title)
	print(credits)
	try:
		numAIPlayers = int(input("                  Number of AI opponents (1-8): "))
	except:
		pass

names = [
	"Harry ", "Frank ", "Mary  ", "John  ", "Sarah ", "Adam  ",
	"Liz   ", "James ", "Rob   ", "Daniel", "Joel  ", "Karen ",
	"Mark  ", "Kate  ", "Terry ", "Gary  ", "Alan  ", "Evan  "
]

wrongInputWarnings = [
	"...What?", "...Excuse me?", "...Could you repeat that?",
	"...Sorry?", "...Hmm?", "...Are you talking to me?",
	"...Was that you?", "...What did you say?", "...Huh?"
]

# --- Classes --- #

class Card(object):
	def __init__(self, _name, _value, _shortName):
		self.name = _name
		self.value = _value
		self.shortName = _shortName
		self.taken = False

class AIPlayer(object):
	def __init__(self, name):
		self.name = name
		self.totalValue = 0
		self.cardsInHand = []
		self.holding = False
		self.hasWon = False

	def Turn(self):
		chanceOfPicking = (21-self.totalValue) / 12

		print(leftMargin + CBLUE + self.name + CEND + " - ", end="")
		if self.holding or (random.randrange(0, 100) / 100) > chanceOfPicking:
			RepeatCharacter("?? ", len(self.cardsInHand))
			print("- "+CYELLOW+"Is holding."+CEND, end="")
			self.holding = True
		else:
			randCard = RandomCard()
			self.totalValue += randCard.value
			self.cardsInHand.append(randCard)
			RepeatCharacter("?? ", len(self.cardsInHand))
			print("- "+CGREEN+"Takes card."+CEND, end="")

		RepeatCharacter(" ", 30- (3 * len(self.cardsInHand)))
		print(" |")
	
	def PrintCards(self):
		print(leftMargin+ CBLUE + self.name + CEND + " - ", end="")
		for c in self.cardsInHand:
			print(c.shortName, end=" ")
		if self.hasWon:
			print("- "+CGREEN+"Winner!"+CEND, end="")
		else:
			print("- "+CRED+"Rubbish"+CEND, end="")
		RepeatCharacter(" ", 34 - (3 * len(self.cardsInHand)))
		print(" |")
		

class Player(object):
	def __init__(self):
		self.name = "You   "
		self.totalValue = 0
		self.cardsInHand = []
		self.holding = False

	def Turn(self):
		print(leftMargin+CBLUE+"Cards in hand"+CEND+" - ", end="")
		if (self.cardsInHand == []):
			print("None", end="")
			RepeatCharacter(" ", 32 - (3 * len(self.cardsInHand)))

		else:
			for c in self.cardsInHand:
				print(c.shortName, end=" ")
			RepeatCharacter(" ", 36 - (3 * len(self.cardsInHand)))
		
		print(" |")
		print(leftMargin+CBLUE+"Total value"+CEND+"   - " + str(self.totalValue) + "                                   ", end="")
		if self.totalValue < 10:
			print(" ", end="")

		print("|")
		print(gap)

		if self.totalValue > 21:
			self.holding = True
			print(leftMargin+CRED+"You have too many cards..."+CEND+"                           |")
			print(gap)
			print(line)

		elif self.holding:
			print(leftMargin+CYELLOW+"You're holding."+CEND+"                                      |")
			print(gap)
			print(line)
			m.getch()

		else:
			print(line)
			print("\n        (T)ake | (H)old")

			while True:
				command = input("         > ")
				command = command.lower()

				if command == "t":
					randCard = RandomCard()
					self.totalValue += randCard.value
					self.cardsInHand.append(randCard)
					break

				elif command == "h":
					self.holding = True
					break

				else:
					print(CRED+"       "+random.choice(wrongInputWarnings)+CEND)

# --- Functions --- #

def RepeatCharacter(char, repeats):
	for _ in range(repeats):
		print(char, end = "")

def SetupAIPlayers():
	aiPlayers.clear()
	tempNames = names.copy()
	for _ in range(numAIPlayers):
		aiPlayers.append(AIPlayer(random.choice(tempNames)))
		tempNames.remove(aiPlayers[-1].name)

def SetupDeck():
	roundOver = False
	cards.clear()
	tempCards = []

	tempCards.append(Card("2 of Hearts", 2, "H2"))
	tempCards.append(Card("3 of Hearts", 3, "H3"))
	tempCards.append(Card("4 of Hearts", 4, "H4"))
	tempCards.append(Card("5 of Hearts", 5, "H5"))
	tempCards.append(Card("6 of Hearts", 6, "H6"))
	tempCards.append(Card("7 of Hearts", 7, "H7"))
	tempCards.append(Card("8 of Hearts", 8, "H8"))
	tempCards.append(Card("9 of Hearts", 9, "H9"))
	tempCards.append(Card("10 of Hearts", 10, "H0"))
	tempCards.append(Card("Jack of Hearts", 11, "HJ"))
	tempCards.append(Card("Queen of Hearts", 11, "HQ"))
	tempCards.append(Card("King of Hearts", 11, "HK"))
	tempCards.append(Card("Ace of Hearts", 12, "HA"))

	tempCards.append(Card("2 of Clubs", 2, "C2"))
	tempCards.append(Card("3 of Clubs", 3, "C3"))
	tempCards.append(Card("4 of Clubs", 4, "C4"))
	tempCards.append(Card("5 of Clubs", 5, "C5"))
	tempCards.append(Card("6 of Clubs", 6, "C6"))
	tempCards.append(Card("7 of Clubs", 7, "C7"))
	tempCards.append(Card("8 of Clubs", 8, "C8"))
	tempCards.append(Card("9 of Clubs", 9, "C9"))
	tempCards.append(Card("10 of Clubs", 10, "C0"))
	tempCards.append(Card("Jack of Clubs", 11, "CJ"))
	tempCards.append(Card("Queen of Clubs", 11, "CQ"))
	tempCards.append(Card("King of Clubs", 11, "CK"))
	tempCards.append(Card("Ace of Clubs", 12, "CA"))

	tempCards.append(Card("2 of Diamonds", 2, "D2"))
	tempCards.append(Card("3 of Diamonds", 3, "D3"))
	tempCards.append(Card("4 of Diamonds", 4, "D4"))
	tempCards.append(Card("5 of Diamonds", 5, "D5"))
	tempCards.append(Card("6 of Diamonds", 6, "D6"))
	tempCards.append(Card("7 of Diamonds", 7, "D7"))
	tempCards.append(Card("8 of Diamonds", 8, "D8"))
	tempCards.append(Card("9 of Diamonds", 9, "D9"))
	tempCards.append(Card("10 of Diamonds", 10, "D0"))
	tempCards.append(Card("Jack of Diamonds", 11, "DJ"))
	tempCards.append(Card("Queen of Diamonds", 11, "DQ"))
	tempCards.append(Card("King of Diamonds", 11, "DK"))
	tempCards.append(Card("Ace of Diamonds", 12, "DA"))

	tempCards.append(Card("2 of Spades", 2, "S2"))
	tempCards.append(Card("3 of Spades", 3, "S3"))
	tempCards.append(Card("4 of Spades", 4, "S4"))
	tempCards.append(Card("5 of Spades", 5, "S5"))
	tempCards.append(Card("6 of Spades", 6, "S6"))
	tempCards.append(Card("7 of Spades", 7, "S7"))
	tempCards.append(Card("8 of Spades", 8, "S8"))
	tempCards.append(Card("9 of Spades", 9, "S9"))
	tempCards.append(Card("10 of Spades", 10, "S0"))
	tempCards.append(Card("Jack of Spades", 11, "SJ"))
	tempCards.append(Card("Queen of Spades", 11, "SQ"))
	tempCards.append(Card("King of Spades", 11, "SK"))
	tempCards.append(Card("Ace of Spades", 12, "SA"))

	for _ in range(len(tempCards)):
		randNum = random.randrange(0,len(tempCards))
		cards.append(tempCards[randNum])
		tempCards.pop(randNum)

def RandomCard():
	while True:
		randNum = random.randrange(0,len(cards))
		if not cards[randNum].taken:
			cards[randNum].taken = True
			return cards[randNum]

def EndRound():

	highestScore = 0

	for p in aiPlayers:
		curValue = p.totalValue

		if curValue > 21:
			pass
		else:
			if curValue > highestScore:
				highestScore = curValue

	curValue = player.totalValue

	if curValue > 21:
		pass
	else:
		if curValue > highestScore:
			highestScore = curValue

	for p in aiPlayers:
		if p.totalValue == highestScore:
			p.hasWon = True
		else:
			p.hasWon = False

	print(title)
	print(credits)

	print(line)
	print(gap)

	# AI players
	for p in range(len(aiPlayers)):
		aiPlayers[p].PrintCards()

	print(gap)
	print(leftMargin, end="")
	for c in range(52):
		if c % 13 == 0 and not c == 0:
			print("              |")
			print(leftMargin, end="")
		if cards[c].taken:
			print("   ", end="")
		else:
			print(cards[c].shortName, end=" ")

	print("              |")
	print(gap)

	# Results
	print(line)
	print(gap)
	print("       |  "+CYELLOW+"Results"+CEND+"                                             |")
	print(gap)
	
	aiPlayers.append(player)
	sortedPlayers = sorted(aiPlayers, key=lambda attrib: attrib.totalValue, reverse=False)
	leaderboard = []
	for i in sortedPlayers:
		if i.totalValue > 21:
			leaderboard.append(i)
		else:
			leaderboard.insert(0, i)

	rank = 0
	lastTotalValue = 0
	for i in leaderboard:

		if i.totalValue != lastTotalValue:
			rank += 1

		print(leftMargin, end='')
		if rank == 1:   print(CYELLOW, end='')
		elif rank == 2: print(CBEIGE, end='')
		elif rank == 3: print(CBLUE, end='')
		else:           print(CWHITE, end='')

		if i.totalValue != lastTotalValue:
			print(str(rank) + ". ", end='')
		else:
			print("-  ", end='')

		print(i.name + CEND + " - " + str(i.totalValue), end='')
		if (i.totalValue < 10): RepeatCharacter(" ", 40)
		else:                   RepeatCharacter(" ", 39)
		print("|")
		lastTotalValue = i.totalValue

	print(gap)
	print(line)

	print("\n       Do you want to exit?")
	while True:
		command = input("        > ")
		command = command.lower()

		if command == "y":
			print(CRED+"       I can't let you do that"+CEND)
			m.getch()
			global exiting
			exiting = True
			break

		elif command == "n":
			player.totalValue = 0
			player.holding = False
			player.cardsInHand.clear()
			SetupAIPlayers()
			SetupDeck()
			break

		else:
			print(CRED+"       "+random.choice(wrongInputWarnings)+CEND)

	os.system(clearCmd)

# --- Program --- #

os.system(clearCmd)
player = Player()
SetupAIPlayers()
SetupDeck()

while not exiting:
	allHolding = True

	print(title)
	print(credits)

	print(line)
	print(gap)

	# AI players
	for p in range(numAIPlayers):
		aiPlayers[p].Turn()

	print(gap)
	print(leftMargin, end="")
	for c in range(52):
		if c % 13 == 0 and not c == 0:
			print("              |")
			print(leftMargin, end="")
		if cards[c].taken:
			print("   ", end="")
		else:
			print("?? ", end="")
	print("              |")
	print(gap)
	print(line)
	print(gap)

	player.Turn()

	for p in aiPlayers:
		if not p.holding:
			allHolding = False

	if not player.holding:
		allHolding = False

	# Clear console
	os.system(clearCmd)

	# Ending round
	if allHolding:
		EndRound()

print(title)
print(credits)
print("\n\n                    Thanks for playing!\n\n\n\n")
