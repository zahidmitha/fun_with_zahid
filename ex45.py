from sys import *
from random import *

class Player (object):

	money = 1000
	place = 0
	deeds = []

	# This could go in rules-it applies to what they board does, not what the player does or has
	def costs(self):
		cost = randint(1,101)
		return cost

	def buy(self, deed):
		self.deeds.append(deed)
		self.costs()

	def move(self):
		place += 1

	def assets(self):
		value = 0
		for deed in self.deeds:
			value += deed['cost']
		return value

class Board(object):


	#each of these tiles could be an object, descended from board

	tiles_list = [
	{"name" : "Start", "cost" : 0, "income" : 0},
	{"name" : "Old Kent Road", "cost" : 100, "income" : 25},
	{"name" : "Angel", "cost" : 200, "income" : 50},
	{"name" : "Trafalgar Square", "cost" : 300, "income" : 75},
	{"name" : "Mayfair", "cost" : 400, "income" : 100},
	{"name" : "Go", "cost" : -100, "income" : 0},

	]

	# Could go in its own class, or if tiles are descended from object this will stay in Board()
	def random_income(self, income):
		if randint(0,101) < 51:
			return income
		else: 
			return 0


class Rules(object):

	def main(self):
		print "You are the famous Monoply Shoe, destined for greatness and riches."
		print "Your aim is to get from the start all the way back to Go, buying properties along the way. You start with $1000 and can choose to buy properties on each tile. A random number is added to your total depending on the number of properties you own. If you end the game with more than $1000 in assets and are cash flow positive, you win."
		print "If you run out of dolla along the way, you lose. Good luck!"

		b = Board()
		p = Player()

		for tile in b.tiles_list:
			print "You are on %s" % tile["name"]

			income = 0
			for deed in p.deeds:
				income = b.random_income(deed['income'])
				p.money += income

			cost = p.costs()				
			p.money = p.money - cost
			print "You spent %d on living costs" % cost
			print "You made %d in income from your properties" % income
			print "You have %d in cash" % p.money
			print "You can buy this deed for %d" % tile['cost']
			
			# Buy deed class could be a descendant of rules

			print "Do you want to?"
			answer = raw_input(">")
			while (answer!="yes" and answer!="no"):
				print "I didn't understand that"
				answer = raw_input(">")

			if answer == "yes":
				p.buy(tile)
				p.money = p.money - tile["cost"]
			elif answer == "no":
				pass
			else:
				print "I didn't understand that"

			# Could be bankruptcy class

			if p.money < 0:
				print "Oh, no, you ran out of cash"
				print "You have %d in cash" % p.money
				print "The bank seizes %d in assets" % p.assets() 
				print "You go bankrupt: The bank seizes your assets and the repo guys fuck you up the sole"
				print "Good luck walking straight (pun intended)"
				return exit(0)					

		# Could be winner class/finish class

		if p.money + p.assets > 1000:
			print "You survived the game. Now go fuck the Monopoly dog...or the Iron"
			print "You have ", p.money, " in cash and ", p.assets() ," in assets" 
			# print "You own %s"
		else:
			print "You have ", p.money, " in cash and ", p.assets() ," in assets"
			print "You survived, but with less money than you started with. Not exactly Warren Buffet, are you?"
			return exit(0)

r = Rules()
r.main()















#class Board(object):

# 	def __init__ (self):
# 		pas


# class Start(Board):

# 	def enter(self):
# 		print "Welcome to Zahid's Monopoly: Where everyone is a loser."
# 		print "The rules:"
# 		print "You start with $1,000 in cash"
# 		print "On each tile you can buy the named property, which has a 50/50 chance of making the stated revenue on each subsequent move."
# 		print "In addition, a random number between 1 and 100 is deducted every go."
# 		print "To win, your assets have to exceed $1000 by the end, without running out of cash in the process."
# 		print "Good luck"
		
# 		Player.self()


# class OldKentRoad(Board):

# 	if Player.money >= 0

# 		def enter(self):
# 			print "You spent %d dollars" %d(Player.costs())
# 			print "You also received x income"
# 			print "Do you want to buy Old Kent Road for $100?"

# 			action = raw_input(">")

# 			if action == "yes":
# 				Player.money - 100
# 			else:
# 				Player.money = Player.money
# 		def buy():

# 			Player.deeds.add("Old Kent Road")

# 	else: 
# 		Bankruptcy()


# class Angel(Board):

# 		if Player.money >= 0

# 		def enter(self):
# 			print "You spent %d dollars" %d(Player.costs())
# 			print "You also received x income"
# 			print "Do you want to buy Old Kent Road for $100?"

# 			action = raw_input(">")

# 			if action == "yes":
# 				Player.money - 100
# 			else:
# 				Player.money = Player.money

# 		else: 
# 		Bankruptcy()

# class TrafalgarSquare(Board):

# 		if Player.money >= 0

# 		def enter(self):
# 			print "You spent %d dollars" %d(Player.costs())
# 			print "You also received x income"
# 			print "Do you want to buy Old Kent Road for $100?"

# 			action = raw_input(">")

# 			if action == "yes":
# 				Player.money - 100
# 			else:
# 				Player.money = Player.money

# 		else: 
# 			Bankruptcy()

# class Mayfair(Board):

# 		if Player.money >= 0

# 		def enter(self):
# 			print "You spent %d dollars" %d(Player.costs())
# 			print "You also received x income"
# 			print "Do you want to buy Old Kent Road for $100?"

# 			action = raw_input(">")

# 			if action == "yes":
# 				Player.money - 100
# 			else:
# 				Player.money = Player.money

# 		else: 
# 			Bankruptcy()

# class Go(Board):

# 	if Player.money >= 0

# 		def enter(self):
# 			Player.money + 50
# 			print "You made $50"
# 			print "You also received x income"
# 			print "You win!"
# 			print "You have $%d in cash" %d(Player.money)
# 			print "You have x in assets"
# 			return exit(0)

# 		else: 
# 			Bankruptcy()

# class Bankruptcy(Board):

# 	def enter(self):
# 		print "Too bad-you ran out of cash."
# 		print "The Bak seized your assets and sent you to jail."
# 		exit(0)


