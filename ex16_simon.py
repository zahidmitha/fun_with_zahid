from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CRTL-C (^C)."
print "If you do want that, hit RETURN."

raw_input ("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to as you for three lines."

lines = []
for i in range(1,5):
	lines.append(raw_input("line %i: " % i))

print "I'm going to write these to the file."

for line in lines:
	target.write(line + "\n");

print "And finally, we close it."
target.close()