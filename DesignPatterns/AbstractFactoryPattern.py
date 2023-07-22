
"""
Abstract Factory Pattern

Eg: Furniture Factory --> Chair, Sofa, CoffeTable  (group of related products -- of Furniture family )
    MythoFurniture, Modern, Art

Eg: GUI  --> Button, CheckBox, NavigationBar (group of related products -- of GUI family)
    WinGUI, MacGUI, LinuxGUI 

"""

from abc import ABC, abstractmethod

# abstract class for Button
class Button(ABC):

    @abstractmethod
    def click(self):
        pass

# cocreate class of Button abstract class
class WinButton(Button):

    def click(self):
        return "Win Click"

# cocreate class of Button abstract class
class MacButton(Button):

    def click(self):
        return "Mac Click"
    
# abstract class for CheckBox
class CheckBox(ABC):

    @abstractmethod
    def tick(self):
        pass

# cocreate class of CheckBox abstract class
class WinCheckBox(CheckBox):

    def tick(self):
        return "Win Tick"
    
# cocreate class of CheckBox abstract class
class MacCheckBox(CheckBox):

    def tick(self):
        return "Mac Tick"




# Abstract Factory Class
class GUIFactory(ABC):

    @abstractmethod
    def createButton(self):
        pass

    @abstractmethod
    def createCheckBox(self):
        pass

# conctre Factory of Abstract Factory
class WinFactory(GUIFactory):

    def createButton(self):
        return WinButton()
    
    def createCheckBox(self):
        return WinCheckBox()
    
# conctre Factory of Abstract Factory
class MacFactory(GUIFactory):

    def createButton(self):
        return MacButton()
    
    def createCheckBox(self):
        return MacCheckBox()

# client doest not need to be edited if factory type changes
def clientCode(guiFactory):

    button = guiFactory.createButton()
    checkbox = guiFactory.createCheckBox()

    print(button.click())
    print(checkbox.tick())


if __name__ == "__main__":

    '''
    xxxxx code to infer the OS at **runtime** based on config paramter 
    '''

    clientCode(WinFactory())

    print("")

    clientCode(MacFactory())
