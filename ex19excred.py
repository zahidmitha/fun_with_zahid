def the_red_wave (olympics_2008, one_billion_consumers):
	print "There were %d perfomers at the 2008 Olympics." % olympics_2008
	print "China has over %d million consumers, but some are freaking old." % one_billion_consumers
	print "Conclusion: World Domination, baby!"
	print "But they claim a peaceful rise...?! \n"

	
	
print "The direct message."
the_red_wave(10000, 1200)

print "The indirect message (variables ftw)."

perfomers = 10000
population =  1200

the_red_wave(perfomers, population)

print "The numerical message."

the_red_wave(2000 + 8000, 1000 + 200)

print "The wrong message."

the_red_wave(perfomers + 2000, population * 1.2)