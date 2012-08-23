#The awesome-o-meter

print "What is your name?",
name = raw_input()
print "How awesome are you",
awesome = raw_input()
print "What is your net worth?",
banks = raw_input()

print "So, your name is %r, you're clearly NOT %r awesome, and you owe the banks %r USD" % (
	name, awesome, banks)