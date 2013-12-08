from sys import exit

def entrance():
	print "You enter the world's most pretentious dinner party."
	print "Cocktails, bowties, unfunny humour and excessive niceness abound."
	print "You've gonna get out of here! What should you do?"
	print "1. Pretend you've had one martinis too many, and insult the host."
	print "2. Take a laced napkin and hold it over your own mouth and nose until you pass out."
	print "3. Make a Nazi joke."
	print "4. Attempt to chat up the host's daughter."
	
	what = raw_input(">")
	
	if "1" in what:
		print"You're taken for a boisterous guest."
		next_try()
	elif what == "2":
		print "You're taken to the parlour, where you wake up to mindless chatter about the effect of antisocial behaviour on suburban house prices."
		next_try()
	elif what == "3":
		print "Success! Your Aryan hosts may agree with you, but they fear you'll blow their cover. You're out."
		exit(0)
	else:
		stay("After a passionate 15 minutes, you find out she's 15. You were her first, so she'll never let you leave. Ever.")
		
def stay (reason):
	print reason
	print "You're stuck there for the rest of the party. Enjoy the olives-they're responsably sourced."
	exit(0)
	
def next_try():
	print "So, your plan bombed. What's your next move?"
	print "1. Set off the fire alarm."
	print "2. Become excessively friendly with a homophobic guest."
	print "3. Take a massive shit in the bathroom."
	
	what = raw_input(">")
	
	if "1" in what:
		stay("Everyone rushes into the courtyard, where a marquee has already been put up.")
	elif what == "2":
		print "Surprisingly, accept your advances, and get you a new wine spritzzer at the bar. You wake up free of the horrendous party, but with a dildo taped into your ass."
		exit(0)
	else:
		stay ("As aristocrats don't suffer the need to excrete, your big job goes disappointingly unnoticed.")
		
entrance()
		
	
	
	