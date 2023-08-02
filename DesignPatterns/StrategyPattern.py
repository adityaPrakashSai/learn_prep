
# Strategy Pattern

# Behavioural Design Pattern

# Problem Solver Class
    # problem solved by different algorithms.
    # Algo1, Algo2, Algo3
    # Cannot change original class.

# interface to implement an algorithm

# 1 class for 1 algorithm

from abc import ABC, abstractmethod

class TSPAlgorithm(ABC):

    @abstractmethod
    def executeAlgorithm(self, data):
        pass

class TSPDynProgAlgorithm(TSPAlgorithm):

    def executeAlgorithm(self, data):
        print("TSP solved by Dyn Prog approach")

class TSPHeuristicAlgorithm(TSPAlgorithm):

    def executeAlgorithm(self, data):
        print("TSP solved by Heuristic approach")

class TSPGreedyAlgorithm(TSPAlgorithm):

    def executeAlgorithm(self, data):
        print("TSP solved by Greedy approach")

class TSPSolver:

    def __init__(self, strategy):
        self.__strategy = strategy

    def findOptimumPath(self, data):
        self.__strategy.executeAlgorithm(data)


if __name__ == "__main__":

    data = [1] * 300000



    datasize = len(data)

    if datasize < 15:
        strategy = TSPDynProgAlgorithm()
    elif datasize < 1000:
        strategy = TSPHeuristicAlgorithm()
    else:
        strategy = TSPGreedyAlgorithm()    

    tspSolver = TSPSolver(strategy)

    tspSolver.findOptimumPath(data)
