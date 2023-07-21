# Creational design pattern
#  Builder
# BO (20-30) parameters 
# Airline (Airline name, IATA code, ...)
# lot of arguments 
# Builder is used one object is more complex
# House(door, window, walls, roof, floor, kitchen, bedroom)
# Kitchen (cooking platform, ro filter)
# Director, Builders and then actual objects
# Below example we want to actually build house
# Builder is house builder which creates the house
# Director is the one client code uses

# https://sbcode.net/python/builder/


from abc import ABC, abstractmethod

class Kitchen(ABC):
    pass

class VillaKitchen(Kitchen):
    pass

class ApartmentKitchen(Kitchen):
    pass

class Roof(ABC):
    pass

class VillaRoof(Roof):
    pass

class ApartmentRoof(Roof):
    pass

class House:
    def __init__(self, roof = None, kitchen = None) -> None:
        self.__roof = roof
        self.__kitchen = kitchen
    
    def setRoof(self, roof):
        self.__roof = roof

    def setKitchen(self, kitchen):
        self.__kitchen = kitchen
    
    def __str__(self) -> str:
        return f'Roof:{self.__roof}-Kitchen{self.__kitchen}'


class Builder(ABC):
    @abstractmethod
    def addRoof(self):
        pass

    @abstractmethod
    def addKitchen(self):
        pass

class VillaBuilder(Builder):
    def addRoof(self):
        return VillaRoof()
    
    def addKitchen(self):
        return VillaKitchen()

class ApartmentBuilder(Builder):
    def addKitchen(self):
        return ApartmentKitchen()
    
    def addRoof(self):
        return ApartmentRoof()

class Director:
    _builder = None

    def set_builder(self, builder):
        self._builder = builder
    
    def getHouse(self):
        house = House()
        house.setKitchen(self._builder.addKitchen())
        house.setRoof(self._builder.addRoof())
        return house

class Student:
    def __init__(self, rollNum = None, name = None, fatherName = None, motherName = None):
        self.__rollNum = rollNum
        self.__name = name
        self.__fatherName = fatherName
        self.__motherName = motherName

student = Student(name = 'ajit')


if __name__ == '__main__':
    director = Director()
    director.set_builder(VillaBuilder())
    house = director.getHouse()
    print(house)


