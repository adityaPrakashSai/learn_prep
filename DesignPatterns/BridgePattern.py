
"""
Bridge
    - Structural

Example:
    Shape
        - Square, Circle

        - colour (red, blue)

        - RedSquare, RedCircle, BlueSquare, BlueCircle

        - Material (Iron, Sponge)

        - R I S, R I C, ...... 8 classes.

        {a, b} X {c, d} X {e, f}= {ab, ac, bc, bd}

    shape  ---  colour


    abstraction, implementation

    GUI (public user gui, admin gui)
    OS (Windows, Linux, MAC)

"""


class RemoteControl:

    def __init__(self, device):
        self._device = device

    def togglePower(self):
        self._device.togglePower()

    def volumeUp(self):
        self._device.setVolume(1)

    def volumeDown(self):
        self._device.setVolume(-1)

    def channelUp(self):
        self._device.setChannel(1)

    def channelDown(self):
        self._device.setChannel(-1)

class Device:

    _power = False
    def togglePower(self):
        if self._power == False:
            self._power = True
        else:
            self._power = False
        print(self._power)

    _volume = 0
    def setVolume(self, amount):
        self._volume += amount
        print(self._volume)

    _channel = 0
    def setChannel(self, channel):
        self._channel += channel
        print(self._channel)


class TV(Device):
    pass

class Radio(Device):
    pass

if __name__ == "__main__":

    tv = TV()
    remote = RemoteControl(tv)

    remote.togglePower()
    remote.volumeUp()
    remote.volumeDown()
    remote.channelUp()
    remote.channelDown()
    remote.togglePower()

    radio = Radio()
    remote = RemoteControl(radio)

