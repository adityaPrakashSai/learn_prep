# Classes 

class MyClass:
    pass

# 1. init is not constructor and below code does not give exception
myClassObj = MyClass()
print(myClassObj)

class Employee:
    ID = 1
    salary = None
    department = None

obj = Employee()

# 2. Add property outside class but it will not be added to original class. It is only obj property
obj.title = 'Manager'
print(obj.title)
print(type(obj))


obj1 = Employee()
# 3. this will throw error as class does not have title property
# print(obj1.title)

# 4. above employee ID is class variable and every
print(obj1.ID)

# 5. initializers with optional parameters. Non-default args follow default args
class EmployeeTest:
    taxPercent = 0.3
    def __init__(self, id = None, salary = 30, dept = None):
        self.ID = id
        self.dept = dept
    
    def tax(self):
        return (self.salary * self.taxPercent)
    
    @classmethod
    def salaryPerDay(cls):
        return (cls.salary / 30)

employeeTest = EmployeeTest(salary = 2)
EmployeeTest.taxPercent = 0.4
print(employeeTest.tax())

# 6. class method to create factory methods. Factory methods return class objects ( similar to a constructor ) for different use cases


   



