from robots.cleaning_robot import CleaningRobot
from robots.cooking_robot import CookingRobot
#maitenance robot multitask between cooking and cleaning 
#has a multitask method which checks for enough battery level for the robot to work 2 tasks 
class MaintenanceRobot(CleaningRobot, CookingRobot):
    def __init__(self, name: str ,battery_level: int, status: str,cleaningtool: str, cooking_skill: str):
        # Initialize both parent classes
        CleaningRobot.__init__(self,name, battery_level,status,cleaningtool)
        CookingRobot.__init__(self,name,battery_level,status,cooking_skill)

    def multi_task(self) -> None:
        print(f"{self.name} is starting multi-tasking")

        # Check if enough battery is available for both tasks
        if self.battery_level < 60:
            print(f"{self.name} does not have enough battery to perform multi-tasking. Please recharge!")
            return

        try:
            # Perform cleaning task
            CleaningRobot.clean(self)
        except Exception as e:
            print(f"An error occurred during cleaning: {e}")
            return

        try:
            # Perform cooking task
            CookingRobot.cook(self)
        except Exception as e:
            print(f"An error occurred during cooking: {e}")
            return

        print(f"{self.name} has completed multi-tasking.")
