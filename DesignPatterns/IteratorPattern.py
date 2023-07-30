
"""
Iterator design pattern

Behavioural design pattern

Iterate over collection of elements
    collections (containers of group of objects) 
        -- lists, 2D arrays, stack, trees, graphs etc.
    traversal
        -- linear, reverse, bfs, dfs, random etc


Main idea: Extract out the traversal behaviour of a collection into 
  a separate object called an Iterator.
  
"""

# declare two interfaces
#   Iterator
#       __next__()
#       traversal algorithms
#       position, etc
#
#   Collection
#       # linearIterator
#       # reverseLinearIterator
#       # BFSIterator
#       __iter__()
#
#   client
#       collection
#       iterates through the collection  --- calls next() 

from collections.abc import Iterator, Iterable

class ConcreteIterator(Iterator):

    __position = None

    __reverse = False

    def __init__(self, collection, reverse = False):
        self.__collection = collection
        self.__reverse = reverse

        if self.__reverse:
            self.__position = -1
        else:
            self.__position = 0

    def __next__(self):

        try:
            value = self.__collection[self.__position]

            if self.__reverse:
                self.__position -= 1
            else:
                self.__position += 1

        except IndexError:
            raise StopIteration()

        return value
    
class ConcreteCollection(Iterable):

    def __init__(self, collection = []):
        self.__collection = collection

    def __iter__(self):
        return ConcreteIterator(self.__collection)
    
    def getReverseIterator(self):
        return ConcreteIterator(self.__collection, True)
    
    def addItem(self, item):
        self.__collection.append(item)

if __name__ == "__main__":

    collection = ConcreteCollection()
    collection.addItem("apple")
    collection.addItem("mango")
    collection.addItem("orange")
    collection.addItem("grapes")
    collection.addItem("banana")

    print(" --> ".join(collection))

    

    
