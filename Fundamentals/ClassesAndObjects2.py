# 7. demonstrate private properties and methods

class EmployeeTest1(object):
    def __init__(self, id, salary = 30, dept = None) -> None:
        self.__Id = id
    
    def setId(self, id):
        self.Id = id
    
    def getId(self):
        return self.Id
    
    def compareId(self):
        return self.__Id == self.Id

objEmpTest1 = EmployeeTest1('sai', 30, 'np')
# 8. below line will throw exception because it is private
# print(objEmpTest1.__Id)
# print(objEmpTest1.__displayId())

objEmpTest1.setId(5)
print(objEmpTest1.getId())
print(objEmpTest1.compareId())
print(objEmpTest1.Id)
print(objEmpTest1._EmployeeTest1__Id)


# IS A relationship

# square is a shape, python is a programming language

class Base:
    pass

class Derived(Base):
    pass

class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model
    
    def printVehicle(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)

class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        super.__init__(make=make, color = color, model = model)
        self.doors = doors
    
    def printVehicle(self):
        super().printVehicle()
        print("Doors:", self.doors)

https://stackoverflow.com/questions/42413670/whats-the-difference-between-super-and-parent-class-name
