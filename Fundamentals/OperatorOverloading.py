
class ComplexNumber:
    def __init__(self, real = 0, img = 0):
        self.real = real
        self.img = img

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img)
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.img - other.img)
    
    def __str__(self):
        return f'Real:{self.real}, Img:{self.img}'
    
obj1 = ComplexNumber(3, 7)
obj2 = ComplexNumber(2, 4)

obj3 = obj1 + obj2
obj4 = obj1 - obj2
print(obj3)
print(obj4)
