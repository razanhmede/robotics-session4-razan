from abc import ABC, abstractmethod

class ROBOT(ABC):
    #first we define the attributes of the robot classes 
    def__init__(self,name: str):
      self._name=name
      self._battery_level=100
      self._status="idle"
    def name(self) -> str:
        return self.name 
    def battery_level(self)-> init:
        return self._battery_level
    #checks if batterylevel is between 0 and 100 and gives an error message if it's not
    def battery_level(self, level: int) -> None:
        if 0 <= level <= 100:
            self._battery_level = level
        else:
            raise ValueError("Battery level must be between 0 and 100.")
    def _status(self) ->str
        return self._status 
    #Second we define the methods of the robot classes 
    def charge(self) -> NONE:
        self._battery_level=100
        self._status="Charging"
        print(f"{self.name} is now charging. The battery level is {self._battery_level} %)")
    def work(self) -> NONE:
        PASS 
    def report_status(self) -> NONE:
        print(f"The current satatus of {self.name} is {self._status},Battery level is {self._battery_level} %")
