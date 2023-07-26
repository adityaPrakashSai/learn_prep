# Visitor pattern is a behavioral pattern
# stable class structure
# want to add new behaviors or operations to them

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def doEmployeeThing(self):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass

class Manager(Employee):
    def __init__(self, name, numberOfSubordinates) -> None:
        self.name = name
        self.numberOfSubordinates = numberOfSubordinates
    
    def doEmployeeThing(self):
        print("I am the Manager")
    
    def accept(self, visitor):
        visitor.visit_manager(self)

class Engineer(Employee):
    def __init__(self, name, technology) -> None:
        self.name = name
        self.technology = technology
    
    def doEmployeeThing(self):
        print("I am engineerah")
    
    def accept(self, visitor):
        visitor.visit_engineer(self)

class Intern(Employee):
    def __init__(self, name, durationInWeeks) -> None:
        self.name = name
        self.durationInWeeks = durationInWeeks

    def doEmployeeThing(self):
        print("Yai yam Yintern")
    
    def accept(self, visitor):
        visitor.visit_intern(self)


class Visitor(ABC):
    @abstractmethod
    def visit_manager(self, manager):
        pass

    @abstractmethod
    def visit_engineer(self, engineer):
        pass

    @abstractmethod
    def visit_intern(self, intern):
        pass

class BonusCalculator(Visitor):
    def visit_manager(self, manager):
        bonus = manager.numberOfSubordinates * 1000
        print(f'{manager.name} - Manager bonus: ${bonus}')
    
    def visit_engineer(self, engineer):
        bonus = 1000 + len(engineer.technology) * 200
        print(f'{engineer.name} - Engineer bonus: ${bonus}')
    
    def visit_intern(self, intern):
        bonus = intern.durationInWeeks * 100
        print(f'{intern.name} - Intern bonus: ${bonus}')


if __name__ == "__main__":
    employees = [
        Manager("Sairam Menon", 5),
        Engineer("David", "C#"),
        Intern("Alice", 10)
    ]

    bonusCalculator = BonusCalculator()
    for employee in employees:
        employee.accept(bonusCalculator)




