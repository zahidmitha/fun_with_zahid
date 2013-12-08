#Creates class

class Song(object):
	
	def __init__(self, verse):
		self.melody = verse

	def elrond_of_rivendell (self):
		for script in self.melody:
			print script

#Instantiates class- copies it and turns it into an object that we can now use

lemon_tree = Song(["All that I can see",
			"Is just another lemon tree"])

print "The best song of all"

print "-" * 10

# Uses a function from within the object we've now created

lemon_tree.elrond_of_rivendell()



		
