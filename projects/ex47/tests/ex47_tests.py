from nose.tools import *
from ex47.game import Room

def test_room():
	gold = Room("GoldRoom",
		"""This room has gold in it you can grab. There's
		a door to the north.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})

def test_room_paths():
	#instantiates room and attributes it to center/north/south 
 	center = Room("Center", "Test room in the center.")
 	north = Room("North", "Test room in the north.")
 	south = Room("South", "test room in the south.")

 	#for center (Room), instantiate app_paths with arg dictionary north and south
 	center.add_paths({'north': north, 'south': south})
 	# instantiate go with arg north. Attribute it to center. Asserts whether from center I 'go' north. From center I go north if 'north' = north then pass test
 	assert_equal(center.go('north'), north)
 	# instantiates go-attributes it to center. From center I go south if 'south' = south then pass test
 	assert_equal(center.go('south'), south)

def test_map():
	# Instantiate room and attribute it to variables
 	start = Room("Start", "You can go west and down a hole")
 	west = Room("Trees", "There are trees here. You can go east")
 	down = Room("Dungeon", "It's dark down here. You can go up")

 	#Links rooms together. i.e. start leads to west room. west leads to start room

 	#instantiates add_paths and attributes it to start.
 	start.add_paths({'west': west, 'down': down})
 	west.add_paths({'east': start})
 	down.add_paths({'up': start})

 	# instantiates go with args west etc and asserts whether value for west key = west
 	assert_equal(start.go('west'), west)
 	assert_equal(start.go('west').go('east'), start)
 	assert_equal(start.go('down').go('up'), start)