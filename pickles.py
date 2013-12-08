### pickletest.py
### PICKLE AN OBJECT

# import the pickle
import pickle

# let's create a list to be pickled
picklelist = ['one', 2, 'three', 'four', 5, 'can you count?']

#now create a file
file = open('pickletest.py', 'w')

# pickle the picklelist
pickle.dump(picklelist, file)

# close the file to finish your picklelist
file.close()
