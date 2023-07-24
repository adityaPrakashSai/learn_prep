
# we may have some non-playing characters in a game

from abc import ABC, abstractmethod
import time
import datetime
import copy

class NonPlayingCharacter(ABC):
    def __init__(self):
        time.sleep(3)
        self.height = None
        self.age = None
        self.defense = None
        self.attack = None
    
    @abstractmethod
    def clone(self):
        pass

class Shopkeeper(NonPlayingCharacter):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        time.sleep(3)
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
        self.charisma = 30

    def clone(self):
        return copy.deepcopy(self)

class Warrior(NonPlayingCharacter):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        time.sleep(3)
        self.stamina = 60
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
    
    def clone(self):
        return copy.deepcopy(self)

class Mage(NonPlayingCharacter):
    def __init__(self, height, age, defense, attack):
        super().__init__()
        time.sleep(3)
        self.mana = 100
        self.height = height
        self.age = age
        self.defense = defense
        self.attack = attack
    
    def clone(self):
        return copy.deepcopy(self)

print('Starting to create multiple shopkeepers at: ', datetime.datetime.now().time())
shopkeeper_prototype = Shopkeeper(180, 22, 5, 8)
warrior_template = Warrior(185, 22, 4, 21)
mage_template = Mage(150, 65, 8, 15)
for i in range(1000):
    shopkeeper_clone = shopkeeper_prototype.clone()
    warrior_clone = warrior_template.clone()
    mage_clone = mage_template.clone()
    print(f'Finished creating a 3 NPC {i} at: ', datetime.datetime.now().time())
print(f'Finished creating all shopkeeper NPCs at: ', datetime.datetime.now().time())
