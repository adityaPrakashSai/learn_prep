# Multi level inheritance

class Vehicle:
    pass

class Car(Vehicle):
    pass

class Hybrid(Car):
    pass

# Hierarchical inheritance

class Truck(Vehicle):
    pass

# hybrid inheritance
class SUV(Car, Truck):
    pass

# advantages: reuse, data hiding, extensibility, maintainability, testing

obj = SUV()

# method overriding
class Shape:
    def getArea():
        pass

class Square(Shape):
    def getArea():
        return 2

# Python programs to demonstrate polymorphism

# Poly 1. duck typing

class Bird:
	def fly(self):
		print("fly with wings")

class Airplane:
	def fly(self):
		print("fly with fuel")

class Fish:
	def swim(self):
		print("fish swim in sea")

# Attributes having same name are
# considered as duck typing
for obj in Bird(), Airplane(), Fish():
	obj.fly()

# Poly 2. method overloading
print(len([1, 2, 3]))
print(len("geeks"))

# Poly 3 is through inheritance
class Bird:
	def intro(self):
		print("There are many types of birds.")
	def flight(self):
	    print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
   def flight(self):
   	print("Sparrows can fly.")
   	
class ostrich(Bird):
   def flight(self):
   	print("Ostriches cannot fly.")
   	
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
   