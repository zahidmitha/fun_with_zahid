from sys import argv

script, user_name, working = argv
prompt = '....TELL ME   '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I understand you work at %s." % (working)
print "I'd like to ask you a few questions."
print "Do you like me %s?" %user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "How old are you?"
old = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
You're %r years old. Shit, you're old!
And you have a %r computer. Dude, get a Lenovo.
""" %(likes, lives, old, computer)