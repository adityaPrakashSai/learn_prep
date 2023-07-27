# Mediator Behavioral design pattern 
# C# library - Mediatr
# Remove dependencies 
# Objects which are independent, Mediator which knows which handler is applicable for 
# object request and then it will call that handler for that request

from collections import defaultdict
from abc import ABC, abstractmethod

class Mediator:
    def __init__(self) -> None:
        self.handlers = defaultdict(list)
    
    def susbcribe(self, requestType, handler):
        self.handlers[requestType].append(handler)
    
    def publish(self, requestType, *args, **kwargs):
        for handler in self.handlers[requestType]:
            handler(*args, **kwargs)
    
class Aircraft:
    def __init__(self, name, altitude, mediator) -> None:
        self.name = name
        self.altitude = altitude
        self.mediator = mediator
    
    def sendMessage(self, message):
        self.mediator.publish(type(message), self, message)
    
    def updateAltitude(self, newAltitude):
        self.altitude = newAltitude

class ChangeAltitudeRequest:
    def __init__(self, oldAltitude, newAltitude) -> None:
        self.oldAltitude = oldAltitude
        self.newAltitude = newAltitude

class ChangeAltitudeRequestHandler:
    def __init__(self) -> None:
        self.altitudeMapping = {}
    
    def handleAltitudeUpdate(self, aircraft, changeAltitudeRequest):
        if changeAltitudeRequest.newAltitude not in self.altitudeMapping:
            self.altitudeMapping[changeAltitudeRequest.newAltitude] = aircraft
            aircraft.updateAltitude(changeAltitudeRequest.newAltitude)
        
            if changeAltitudeRequest.oldAltitude in self.altitudeMapping:
                del self.altitudeMapping[changeAltitudeRequest.oldAltitude]
    

if __name__ == "__main__":
    controlTower = Mediator()
    aircraft1 = Aircraft("Boeing 747", 2000, controlTower)
    aircraft2 = Aircraft("Airbus A380", 4000, controlTower)
    request = ChangeAltitudeRequest(2000, 8000)
    handler = ChangeAltitudeRequestHandler()
    controlTower.susbcribe(ChangeAltitudeRequest, handler.handleAltitudeUpdate)

    aircraft1.sendMessage(request)
    aircraft2.sendMessage(request)

    print(aircraft1.altitude)
    print(aircraft2.altitude)

