def tentimes(x, y):
	result = x + y
	times = result * 10
	return times

tentimes(5, 5)


def twentytimes (a, z):
	result = a * z
	return result

print twentytimes(tentimes(4,4), 20)

def add(x,y):
	return x + y

def multiply(x,y):
	return x * y

print multiply(add(2,3), add(7,10))
# (2 + 3) * (7 + 10)

def multiply(x,y):
	return x * y