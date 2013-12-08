from sys import argv
from os.path import exists



print "Copying from %s to %s"% (argv[1], argv[2])



#print "The input file is %d bytes long" %len(indata)

print "Does the output file exist?%r" %exists(argv[2])
print "Ready, hit RETURN to continue, CTRL-C to abort."




raw_input(), open(argv[2], 'w').write(open(argv[1]).read())