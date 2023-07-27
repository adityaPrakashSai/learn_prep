

"""
Decorator Pattern

Example:
    Pizza (Base class)
    Peppy Paneer Pizza, Farm House Pizza, Margherita Pizza (Sub classes)

    - Toppings
        - fresh tomato, jalapeno, onion, corn, cheese, ...

    Pizzas with toppings
        PPP with FT, PPP with J, PPP with O, ...
        FHP with FT, FHP with J, FHP with O, ...
    Pizzas with topping combos
        PPP with FT & J, PPP with J & O & FT ...
        ...
        so many sub classes.
Example:
    simple word
    Italic(word)
    Italic-Bold(word)
    Bold-Underline-Italic(word)
"""
from abc import ABC, abstractmethod

class Text(ABC):

    @abstractmethod
    def render(self):
        pass

# simple undecorated
class Word(Text):

    def __init__(self, word):
        self.__word = word

    def render(self):
        return self.__word
    
class Decorator(Text):

    def __init__(self, decoratedText):
        self.__decoratedText = decoratedText

    def render(self):
        return self.__decoratedText.render()
    
# decorators (or wrappers)
class ItalicDecorator(Decorator):

    def render(self):
        return f"Italic({super().render()})"
    
class BoldDecorator(Decorator):

    def render(self):
        return f"Bold({super().render()})"
    
class UnderlineDecorator(Decorator):

    def render(self):
        return f"Underlined({super().render()})"

if __name__ == "__main__":

    word = Word('abcd')

    italicword = ItalicDecorator(word)
    boldword = BoldDecorator(italicword)
    underlinedword = UnderlineDecorator(boldword)

    print(underlinedword.render())