# Composite is another structural design pattern that lets you compose objects
# into tree-like structure to allow client to treat individual objects and composition of objects uniformly


from typing import List
from abc import ABC, abstractmethod


# Composite interface:
class Employee(ABC):
    def __init__(self, name: str, salary: int) -> None:
        self.name = name
        self.salary = salary

    @abstractmethod
    def displayDetails(self):
        pass


# leaf individual employee
class IndividualEmployee(Employee):
    def displayDetails(self):
        print(f"{self.name} - Salary: ${self.salary}")


# composite Manager with subordinates
class Manager(Employee):
    def __init__(self, name: str, salary: int) -> None:
        super().__init__(name, salary)
        self.subordinates: List[Employee] = []

    def addSubordinates(self, employee: Employee):
        self.subordinates.append(employee)

    def removeSubordinates(self, employee: Employee):
        self.subordinates.remove(employee)

    def displayDetails(self):
        print(f"{self.name} (Manager) - Salary: ${self.salary}")
        print("Subordinates:")
        for subordinate in self.subordinates:
            subordinate.displayDetails()


if __name__ == "__main__":
    emp1 = IndividualEmployee("John Doe", 50000)
    emp2 = IndividualEmployee("Jane Smith", 45000)

    m1 = Manager("Mike Johnson", 80000)
    m2 = Manager("Emily James", 75000)

    m2.addSubordinates(emp1)
    m2.addSubordinates(emp2)
    m1.addSubordinates(m2)

    m1.displayDetails()
    print("--------------------")
    m2.displayDetails()
    print("---------------")
    emp1.displayDetails()
