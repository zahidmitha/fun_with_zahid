from sys import argv

script, filename = argv

openfile = open(filename, 'r')

openfile.seek(-10,2)

# With seek (x, y)
# x is the position in letters/bytes away from where you start, and y is where you start (where 0 is the beginning, 1 is halfway, and 2 is the end).


print openfile.read()

print openfile.tell()

print openfile.readline()

# openfile.write("This should never be written")

# openfile.close()

