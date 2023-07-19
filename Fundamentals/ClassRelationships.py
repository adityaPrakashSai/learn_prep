
# relationships between classes
# 1. IS A => Parent class and Child Class: Square is a shape, triangle is a polygon
# Part of => Composition: Car=> Engine, tyres, doors.
        # Car is owner of engine, tyres and doors. Lifetime of owner decides the lifetime of owned object

class Engine:
    pass

class Tyre:
    pass

class Door:
    pass

class Car:
    def __init__(self, engine, tyre, door):
        self.__engine = engine
        self.__tyre = tyre
        self.__door = door

# Has a (Aggregation)=> Country has people
# In Aggregation, the owned object can live even after owner dies. 