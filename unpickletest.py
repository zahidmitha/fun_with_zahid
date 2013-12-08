### unpickle file

# import the pickle module
import pickle

# now open a file for reading-this is the file we just pickled using pickles.py
unpicklefile = open('pickletest.py', 'r')

# now load the list that we pickled into a new object
unpickledlist = pickle.load(unpicklefile)

# close file for safety
unpicklefile.close()

# try out items
for item in unpickledlist:
	print item
