

class lexicon(object):

	def scan(self):
		unsorted_words = "111 The door goes south to stopn at the west junction, where it will kill a crimean cat to the east"
		words = unsorted_words.split()

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
				print direction[word]
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

		
		# def integers(str):
		# 	try:
		# 		return int(s)
		# 	except ValueError:
		# 		return None

		# l = []

		# for word in words:
		# 	l.add(integers(word))

		# print l




		

lexicon = lexicon()
lexicon.scan()





		#[('noun': 'princess')
		#('noun': 'bear')