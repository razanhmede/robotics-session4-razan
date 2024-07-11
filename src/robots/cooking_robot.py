from .base_robot import ROBOT 
class CookingRobot(Robot):
    def __init__(self,name: str, cooking_skill: str) ->NONE:
        super().__init__(name)
        self._cooking_skill =cooking_skill
    #first we define the attributes here is cleaningtool
    def cooking_skill (self) ->str:
         return self._cooking_skill
    #Second we define the methods here is work
    def work(self)  -> NONE:
        #decrease battery level by 20 for each cleaning session but check first if battery level is above 20
        if self._battery_level>=30:
            self._status ="ABLE TO WORK"
            print(f"{self._name} is now cooking with {self._cooking_skill}")
            self._battery_level -=30
            self._status= "idle"
        else:
            print(f"{self._name} is not able to work now. Please recharge!")
            self.report_status()