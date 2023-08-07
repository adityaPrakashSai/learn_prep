"""
State Pattern

Behavioural Design Pattern

object
    - set of states

    Eg: Water 
        - Solid, Liquid, Vapour

    Eg: Employee, Son, Husband

1. create classes for each state
2. Reference to state object
    
"""

from abc import ABC, abstractmethod

class Man:

    _state = None

    def __init__(self, state):
        self.changeState(state)

    def changeState(self, state):
        print(f'State changed from {type(self._state).__name__} to {type(state).__name__}')
        self._state = state
        self._state.Man = self

    def wakeup(self):
        self._state.wakeup()

    def eat(self):
        self._state.eat()

    def think(self):
        self._state.think()

    def sleep(self):
        self._state.sleep()

    def dream(self):
        self._state.dream()

class State(ABC):

    @property
    def Man(self):
        return self._Man
    
    @Man.setter
    def Man(self, man):
        self._Man = man

    @abstractmethod
    def wakeup(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def think(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    @abstractmethod
    def dream(self):
        pass

class ActiveState(State):

    def wakeup(self):
        print("Active State: Man already awake")

    def eat(self):
        print("Active State: Man is eating")

    def think(self):
        print("Active State: Man is thinking")

    def sleep(self):
        self.Man.changeState(SleepState())
        print("Man started sleeping")

    def dream(self):
        print("Active State: Man can't dream")

class DrousyState(State):

    def wakeup(self):
        self.Man.changeState(ActiveState())
        
    def eat(self):
        print("Drousy State: Man may spill food")

    def think(self):
        print("Drousy State: Man may think")

    def sleep(self):
        self.Man.changeState(SleepState())
        print("Man started sleeping")

    def dream(self):
        print("Drousy State: Man can day dream")

class SleepState(State):

    def wakeup(self):
        self.Man.changeState(ActiveState())
        print("Man woke up just now. Yawwn!")

    def eat(self):
        print("Sleep State: Man can not eat")

    def think(self):
        print("Sleep State: Man can not think")

    def sleep(self):
        print("Sleep State: Man is already sleeping")

    def dream(self):
        print("Sleep State: Man can dream")


if __name__ == "__main__":

    man = Man(DrousyState())

    man.sleep()
    man.dream()
    man.eat()
    man.think()
    man.wakeup()

    man.wakeup()
    man.dream()
    man.eat()
    man.think()
    man.sleep()