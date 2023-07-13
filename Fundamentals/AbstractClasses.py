

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, length = 0):
        self.__length = length

    def area(self):
        return super().area()
        
    def perimeter(self):
        return 4*self.__length
    
    
obj = Square()
# print(obj.perimeter())
print(obj.area())


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('bark')
