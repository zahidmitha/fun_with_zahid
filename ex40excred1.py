
#Creates class

class Tune(object):
	
	def __init__(self, melody):
		self.jazz = melody
	
	def remix_dat(self):
		for line in self.jazz:
			print line

#Instantiates class- copies it and turns it into an object that we can now use

crazy = Tune(["We're never gonna survive..",
		"Unless we get a little",
		"CRAZY!"])

beyonce_crazy = Tune(["So crazy right now..",
			"Looking so crazy in love",
			"This song is a guilty pleasure"])



# Uses a function from within the object we've now created

crazy.remix_dat()

print "-" * 10

beyonce_crazy.remix_dat()

