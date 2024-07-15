import time
from .base_robot import Robot
#cleaning robot has as set cleaning tool which checks for the validity of the cleaning tool provided 
#clean method (to not override if same work method is used for cooking and cleaning)
#clean method checks if if the robot is able to clean through battery level and decreases the battery level by 1 % for each 1 min of working (only for testing purposes)
#self diagnosis method which checks for valid c tool
class CleaningRobot(Robot):
    def __init__(self,name: str, battery_level: int, status: str, cleaningtool: str):
        Robot.__init__(name, battery_level, status)
        #self.set_cleaningtool(cleaningtool)
        CleaningRobot.set_cleaningtool(cleaningtool)

    def get_cleaningtool() -> str:
        return CleaningRobot.cleaningtool

    
    def set_cleaningtool(cleaningtool: str) -> None:
        if cleaningtool not in ["vacuum", "mop", "brush", "sponge"]:
            raise ValueError("Invalid cleaning tool!!")
        CleaningRobot.cleaningtool = cleaningtool

    def clean(self) -> None:
        if CleaningRobot.battery_level >= 20:
            CleaningRobot.status = "ABLE TO WORK"
            print(f"{CleaningRobot.name} is now cleaning with {CleaningRobot.cleaningtool}")
            for _ in range(20): 
                time.sleep(1)  # Sleep for 1 minute
                CleaningRobot.battery_level -= 1
                print(f"Battery level: {CleaningRobot.battery_level}%")
                if CleaningRobot.battery_level < 20:
                    print(f"{CleaningRobot.name} does not have enough battery to continue cleaning. Please recharge!")
                    break
            CleaningRobot.status = "idle"
        else:
            print(f"{CleaningRobot.name} is not able to work now. Please recharge!")
            CleaningRobot.report_status()

    def self_diagnose(self) -> list:
        base_diagnosis = super().self_diagnose()
        if CleaningRobot.cleaningtool not in ["vacuum", "mop", "brush", "sponge"]:
            base_diagnosis.append("Invalid cleaning tool!")
        return base_diagnosis
