## Animal is-a object (sort of confusing) look at the extra credit
class Animal(object):
	pass

# Dog is-a animal
class Dog(Animal):
	
	def __init__ (self, name):
		# Dog has-a name. Fron self get the name attribute and assign it to name
		self.name = name

#	def Tail(self):
#		for wag in self.name
#			print name

#Cat is-a animal
class Cat(Animal):
	
	def __init__ (self, name):
		# Cat has-a name. From self get the name attribute and assign it to name
		self.name = name

# Person is-a object
class Person(object):
	
	def __init__ (self, name):
		# Person has-a name
		self.name = name
	
		# Person has-a pet of some kind
		self.pet = None

#		def Car(self):
#			if self.name = name
#				print "%s is their name" %s

# Employee is-a person
class Employee(Person):
	
	def __init__ (self, name, salary):
		# Employee has-a name. WTF IS THIS??
		super(Employee, self).__init__(name)
		# Employee has-a salary
		self.salary = salary

# Fish is-a object
class Fish(object):
	pass
#	def __init__(self):
#		self.scale = scale

#	def Gills:
#		for scale self.scale
#			print "Scaly bastard"

#Salmon is-a fish
class Salmon(Fish):
	pass

# Halibut is-a fish
class Halibut(Fish):
	pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# maru is-a person
mary = Person("Mary")

# mary has-a pet called satan. From mary get the pet attribute and call it satan
mary.pet = satan

# frank is-a Employee. Frank has-a name Frank and a salary of 120,000. "From Frank get the function called employee with parameters self, name and salary"
frank = Employee("Frank", 120000)

# Frank has-a pet called Rover. Rover is-a dog
frank.pet = rover

# flipper is-a Fish. Set flipper to an instance of Fish
flipper = Fish()

# crouse is-a Salmon. Set crouse to an instance of Salmon
crouse = Salmon()

# harry is-a Halibut. Set harry to an instace of Halibut
harry = Halibut()
