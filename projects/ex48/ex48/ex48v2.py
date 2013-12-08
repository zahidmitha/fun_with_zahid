
class lexicon(object):

	def scan(self, stuff):
		unsorted_words = stuff
		unsorted_words.lower()
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

		stop_words = { "the" : ('stop_words', 'the'),
		'in' : ('stop_words', 'in'),
		'from' : ('stop_words', 'from'),
		'of' : ('stop_words', 'of'),
		'at' : ('stop_words', 'at')
		}
		
		nouns = { 'door' : ('noun', 'door'),
		'bear' : ('noun', 'bear'),
		'princess' : ('noun', 'princess'),
		'cabinet' : ('noun', 'cabinet')}

		numbers = { '1234' : ('number', 1234),
		'3' : ('number', 3),
		'91234' : ('number', 91234),
		}

		errors = { 'ASDFADFASDF' : ('error', 'ASDFADFASDF'),
		'bear' : ('noun', 'bear'),
		'IAS' : ('error', 'IAS'),
		'princess' : ('error', 'princess')
		}



		germany = []
		#print "before loop"
		#print words
		#print "afer words"
		for word in words:
			#print word
			if word in direction:
				germany.append(direction[word])
				print direction[word]
			elif word in verbs:
				germany.append(verbs[word])
				print verbs[word]
			elif word in nouns:
				germany.append(nouns[word])
				print nouns[word]
			elif word in stop_words:
				print stop_words[word]
				germany.append(stop_words[word])
			elif word in numbers:
				print numbers[word]
				germany.append(numbers[word])
			elif word in errors:
				print errors[word]
				germany.append(errors[word])
			elif word.isdigit():
				print int(word)
			else:
				print "None"
			#else:
				# print word.isdigit() - this checks if the word is a digit and if it isn't it says false
				# print word
			#	print "None"
		#print "after the assignments"
		#germany.append([directio, ver, sto])
		return germany
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



#lexicon_asks = 1

#print "This script will ask you for four sentences. Choose wisely."

# for lexicon_asks in range (1, 5):
# 	lexicon.scan(raw_input(">"))
# 	lexicon_asks = lexicon_asks + 1

lexicon.scan(raw_input(">"))