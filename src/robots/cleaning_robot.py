from .base_robot import Robot
class CleaningRobot(Robot):
    def __init__(self,name: str, cleaningtool: str) ->None:
        super().__init__(name)
        self._cleaningtool =cleaningtool
    #first we define the attributes here is cleaningtool
    def cleaningtool(self) ->str:
         return self._cleaningtool
    #Second we define the methods here is work
    def work(self)  -> None:
        #decrease battery level by 20 for each cleaning session but check first if battery level is above 20
        if self._battery_level>=20:
            self._status ="ABLE TO WORK"
            print(f"{self._name} is now cleaning with {self._cleaningtool}")
            self._battery_level -=20
            self._status= "idle"
        else:
            print(f"{self._name} is not able to work now. Please recharge!")
            self.report_status()