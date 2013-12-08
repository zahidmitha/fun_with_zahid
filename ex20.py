#imports modules from python lib

from sys import argv

# creates arguments that we need to input when reading the file. so, the file we need to read is script

script, input_file = argv

#creates a frunction that reads the file (read is a python function)

def print_all(f):
	print f.read()

#function that rewinds the file by taking it to pint zero

def rewind(f):
	f.seek(0)
	
#prints finds the line you choose (according to the arg you pass in) and reads it

def print_a_line(line_count, f):
	print line_count, f.readline()

#open is a python function-this creates a variable current_file and attributes it to opeining the input_file argument
	
current_file = open(input_file)

print "First let's print the whole file:\n"

#executes print_all function

print_all(current_file)

print "Now let's rewind, kind of like a tape."

#executes rewind function

rewind(current_file)

print "Let's print three lines:"

#attributes current line, and passes it into function

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)