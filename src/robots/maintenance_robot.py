from robots.cleaning_robot import CleaningRobot
from robots.cooking_robot import CookingRobot

class MaintenanceRobot(CleaningRobot, CookingRobot):
    def __init__(self, name: str, cleaningtool: str, cooking_skill: str) -> None:
        # Initialize both parent classes
        CleaningRobot.__init__(self, name, cleaningtool)
        CookingRobot.__init__(self, name, cooking_skill)

    def multi_task(self) -> None:
        print(f"{self.name} is starting multi-tasking")

        # Check if enough battery is available for both tasks
        if self.battery_level < 60:
            print(f"{self.name} does not have enough battery to perform multi-tasking. Please recharge!")
            return

        try:
            # Perform cleaning task
            CleaningRobot.work(self)
        except Exception as e:
            print(f"An error occurred during cleaning: {e}")
            return

        try:
            # Perform cooking task
            CookingRobot.work(self)
        except Exception as e:
            print(f"An error occurred during cooking: {e}")
            return

        print(f"{self.name} has completed multi-tasking.")
