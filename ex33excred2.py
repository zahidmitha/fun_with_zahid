
def append_all(n,j):
	i = 0
	numbers = []
	while i  < n:
		print "At the top is %d" % i
		print "j is %d" % j
		numbers.append(i)
		i = i + j 
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	
append_all(10, 2)