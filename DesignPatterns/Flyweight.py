# Structural pattern
# The problem is that if we have very large number of objects
# we can't fit them all in memory
# Solution : Flyweight
# Most of the objects are similar, only coordinates are different
# Extrinsic properties which is unique coordinate
# Intrisic properties: texture, color

class TextFormatting:
    def __init__(self, font, color, size):
        self.font = font
        self.color = color
        self.size = size

class TextFormattingFactory:
    _formattingCache = {}

    @classmethod
    def getFormatting(cls, font, size, color):
        key = (font, size, color)
        if key not in cls._formattingCache:
            cls._formattingCache[key] = TextFormatting(font, size, color)
        return cls._formattingCache[key]
    
class Character:
    def __init__(self, char, font, size, color) -> None:
        self.char = char
        self.formatting = TextFormattingFactory.getFormatting(font, size, color)

    def render(self):
        print(f'Character: {self.char}, Font: {self.formatting.font}, Size: {self.formatting.size}, Color: {self.formatting.color}')
    

if __name__ == "__main__":
    characters = []
    characters.append(Character('H', 'Arial', 12, 'Black'))
    characters.append(Character('e', 'Arial', 12, 'Black'))
    characters.append(Character('l', 'Arial', 12, 'Black'))
    characters.append(Character('l', 'Arial', 12, 'Black'))
    characters.append(Character('o', 'Arial', 12, 'Black'))
    
    for char in characters:
        char.render()