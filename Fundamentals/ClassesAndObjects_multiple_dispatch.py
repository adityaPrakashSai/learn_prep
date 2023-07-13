from multipledispatch import dispatch

class Shape:
    def __init(self):
        pass
    
    @dispatch(str, str)
    def color(self, red, blue):
        return 'green'
    
    @dispatch(str, str, str)
    def color(self, red, blue, green):
        return 'white'

    
obj = Shape()
print(obj.color('r', 'b'))
print(obj.color('r', 'b', 'g'))