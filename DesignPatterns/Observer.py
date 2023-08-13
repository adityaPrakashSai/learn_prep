# Observer is a behavioral design pattern
# it lets you define a subscription mechanism to notify
# multiple objects about any events that happen to the object they are observing


from __future__ import annotations
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class Subject:
    def __init__(self) -> None:
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)


class DeviceObserver(Observer):
    def __init__(self, name) -> None:
        self._name = name

    def update(self, message):
        print(f"Device {self._name} received message {message}")


class SlackApplication(Subject):
    def __init__(self) -> None:
        super().__init__()
        self.message = ""

    def sendMessage(self, message):
        self.message = message
        self.notify(self.message)


if __name__ == "__main__":
    laptop = DeviceObserver("Laptop")
    tablet = DeviceObserver("Tablet")
    phone = DeviceObserver("Phone")

    slackApp = SlackApplication()
    slackApp.attach(laptop)
    slackApp.attach(tablet)
    slackApp.attach(phone)

    slackApp.sendMessage("Hello!!! Important Notification ? Just spamming...")
