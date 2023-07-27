
"""
Singleton - Single object creation
Examples:  DB connection, Config file, Govt
"""

# 1. using static method
class Singleton:

    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance is None:
            Singleton.__instance = Singleton()

        return Singleton.__instance

s1 = Singleton.getInstance()
s2 = Singleton.getInstance()

print(s1)
print(s2)

# creates a new object if getInstance not used.
s3 = Singleton()
print(s3)

#----------------------------------------------------------------------------

# 2. overriding __new__ method
class Singleton:
    
    # private attribute to store the instance of singleton class
    __instance = None

    def __new__(cls):
            
        # create instance for the first time & save it in private attribute.
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

s1 = Singleton()
s2 = Singleton()

print(s1)
print(s2)

class SingletonChild(Singleton):
    pass

s3 = SingletonChild()
print(s3)

#---------------------------------------------------------------------

# Thread safe implementation
from threading import Thread, Lock

class Singleton:
    
    __instance = None

    __lock = Lock()

    def __new__(cls):

        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)

        return cls.__instance

def test():
    obj = Singleton()
    print(obj)

threads = []
for i in range(10000):
    p1 = Thread(target=test)        
    threads.append(p1)
    p1.start()

for t in threads:
    t.join()

# ------------------------------------------------------------------

"""
meta classes
    - everything in Python is an object
    -   int, str, function, class
    -   x = 5 --> x is an object of integer class.
   
    - class is an object of 'type' class. 
     - type is meta class -- the class that creates classes.
     - type(int) = type, type(str) = type, type(type) = type

    what happens when we define a class?
    class A:
        x = 5 
    the above code is same as:  A = type('A',(),{'x':5})

callable()
    callable(int) returns true
    every class is callable. that is why we can call a class as a function obj = A()

    type class has __call__ method.
    when we write obj = A() then, type.__call__ method gets called.

    so when we want to create singleton object by writing s = Singleton() then type.__call__ gets called.
    if we can override __call__ method in type class we will be able to create only single object.

    To achieve tihs, we create our own meta class by inheriting type class. 
    From within the meta class if we override __call__ method to create only one instance, then Singleton is achieved.    
"""
"""
Ref Links:
    - what does it mean by everything is an object --> https://stackoverflow.com/questions/40478536/in-python-what-does-it-mean-by-everything-is-an-object
    - Meta classes & how classes really work --> https://www.youtube.com/watch?v=NAQEj-c2CI8
    - callable() & __call__() --> https://www.youtube.com/watch?v=CSXTeMrw9Lg
"""

class SingletonMeta(type): #SingletonMeta becomes a meta class.

    __instance = None

    def __call__(cls, *args, **kwargs):

        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)

        return cls.__instance


class Singleton(metaclass = SingletonMeta):
    pass

s1 = Singleton()
s2 = Singleton()

print(s1)
print(s2)

#   C#
#services.addSingleton('Singleton')