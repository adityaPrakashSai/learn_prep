"""
Adapter Pattern

Structural Pattern

Example:

Switch board (Power Provider)
Laptop (Power Receiver)
Interfaces are incompatible
Adapter (Laptop Charger)

Legacy Code
Wrapper code 

VBA Code --
Python Developer 
Python Wrapper -- sequencing..
"""

class RoundHole:

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
    def fit(self, roundPeg):
        return self._radius >= roundPeg.radius
    
class RoundPeg:

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius
    
class SquarePeg:

    def __init__(self, length):
        self._length = length

    @property
    def length(self):
        return self._length
    
# Adapter pattern using composition
class SquareToRoundAdapter1:

    def __init__(self, sqPeg):
        self._sqPeg = sqPeg

    @property
    def radius(self):
        return self._sqPeg.length/pow(2, 0.5)


# Adapter pattern using inheritance
class SquaretoRoundAdapter2(SquarePeg):

    @property
    def radius(self):
        return self.length/pow(2,0.5)

if __name__ == "__main__":

    hole = RoundHole(5)
    rPeg = RoundPeg(6)


    # composition
    sPeg = SquareToRoundAdapter1(SquarePeg(5))

    print(hole.fit(sPeg))

    # inheritance
    sPeg2 = SquaretoRoundAdapter2(5)
    print(hole.fit(sPeg2))
