from sys import exit
# from ex48v2 import * 

def gold_room():
	print "This room is full of gold. How much do you take?"
	
	next = raw_input(">")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else: 
		dead("You greedy bastard!")
	
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		next = raw_input(">")
		
		if next == "take honey":
			dead("The bear looks at you and slaps your face off")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your legs off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else: 
			print "I got no idea what that means."
			
def cthulu_room():
	print "Here you see the great evil Cthulu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input(">")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well, that was tasty!")
	else:
		cthulu_room()

def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	next = scan(raw_input((">"))
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulu_room()
	else: 
		dead("You stumble around the room until you starve.")

#class lexicon(object):

def scan(self, var):
	print "wank"
	unsorted_words = var
	print unsorted_words
	words = unsorted_words.split()
	print words

	direction = {"north" : ('direction', 'north'),
	"south" : ('direction', 'south'),
	"east" : ('direction', 'east'),
	"west" : ('direction', 'west')
		}

	verbs = {"go" : ('verb', 'go'),
	"stop" : ('verb', 'stop'),
	"kill" : ( 'verb', 'kill'),
		"eat" : ('verb', 'eat')
		}

	stop_words = { 'the' : ('stop_word', 'the'),
	'in' : ('stop_words', 'in'),
	'from' : ('stop_words', 'from'),
	'of' : ('stop_words', 'of'),
	'at' : ('stop_words', 'at')
	}
		
	nouns = { 'door' : ('noun', 'door')



		}


	for word in words:
		if word in direction:
			return direction[word]
		elif word in verbs:
			print verbs[word]
		elif word in stop_words:
			print stop_words[word]
		elif word.isdigit():
			print int(word)
		else:
				# print word.isdigit() - this checks if the word is a digit and if it isn't it says false
				# print word
			print "None"

	exit(0)	

start()
#lexicon = ex48v2.lexicon()
#lexicon.scan() 
