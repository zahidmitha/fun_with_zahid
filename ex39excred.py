# Mapping of Manufacturers and Consoles

maker = {
	 'Gamecube': 'Nintendo',
	 'Xbox': 'Microsoft',
	 'Playstation 2': 'Sony',
	'Wonder Swan': 'Gunpei Yokoi',
	'Dreamcast': 'Sega' 
}

# creates a set of Consoles and some Games attached

games = {
	'Gamecube': 'Metroid',
	'Xbox': 'Halo',
	'Playstation 2': 'GTAIII'
}

# Add some more games

games['Dreamcast'] = 'Shenmue'
games['Wonder Swan'] = 'Gunpey'

# print out consoles and games
print '-' * 10
for console, game in games.items(): 
	print "The %s, manufactured by %s, had %s as its flagship game" % (console, maker[console], game)
print '-' * 10
