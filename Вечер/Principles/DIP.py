from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable): # high level
    def turn_on(self):
        print("LightBulb turned on...")
    
    def turn_off(self):
        print("LightBulb turned off...")


class Fan(Switchable): # high level
    def turn_on(self):
        print("Fan turned on...")
    
    def turn_off(self):
        print("Fan turned off...")


class ElectricPowerSwitch: # low level
    def __init__(self, c: Switchable):
        self.client = c
        self.on = False

    def press(self):
        if self.on:
            self.client.turn_off()
            self.on = False
        else:
            self.client.turn_on()
            self.on = True


l = LightBulb()
switch = ElectricPowerSwitch(l)
switch.press()
switch.press()


c = Fan()
switch = ElectricPowerSwitch(c)
switch.press()
switch.press()
