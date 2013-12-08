from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
nazis = raw_input("> ")

samurai = open(nazis)

print samurai.read()

# Still need to do more excred stuff like pydoc open and raw_input only
