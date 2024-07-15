import time
from abc import ABC, abstractmethod
#base robot class sets battery level to be valid  as well as status 
#has a charge method which charges 1% for each 1 sec made for testing purposes 
#has a report status method which returns the status of robot when changed 
#self diagnose method which checks for issues such as empty name,invalid battery level and and invalid status as well low and critical battery levels

class Robot(ABC):
    def __init__(name: str, battery_level: int, status: str = "idle"):
        Robot.set_name(name)
        Robot.set_battery_level(battery_level)
        Robot.set_status(status)
    
    def get_name(self)->str:
        return self.name

    def set_name(name2: str) -> None:
        Robot.name = name2

    def get_battery_level() -> int:
        return Robot.battery_level

    def set_battery_level(level: int) -> None:
        if 0 <= level <= 100:
            Robot.battery_level = level
            print(Robot.battery_level)
        else:
            raise ValueError("Battery level must be between 0 and 100.")

    def get_status() -> str:
        return Robot.status

    def set_status(status2: str) -> None:
        if status2 in {"idle", "ABLE TO WORK", "charging"}:
            Robot.status = status2
        else:
            raise ValueError("Status must be 'idle', 'ABLE TO WORK', or 'charging'.")

    def charge(self) -> None:
        if Robot.get_battery_level() == 100:
            print("Fully charged!")
            Robot.set_status("idle")
        else:
            Robot.set_status("charging")
            while Robot.get_battery_level() < 100:
                time.sleep(1)
                Robot.set_battery_level(Robot.get_battery_level() + 1)
                print(f"Battery level: {Robot.get_battery_level()}%")
            print("Robot has finished charging!")
            Robot.set_status("idle")

    def report_status(self) -> str:
        print(f"The current status of {Robot.name} is {Robot.status}. Battery level is {Robot.battery_level}%.")

    def self_diagnose(self) -> list:
        errors = []
        if not Robot.name:
            errors.append("Name is empty.")
        if not (0 <= Robot.battery_level <= 100):
            errors.append("Battery level is out of bounds.")
        if Robot.status not in {"idle", "ABLE TO WORK", "charging"}:
            errors.append("Status is invalid.")
        
        battery_diagnose = Robot.check_battery(Robot.battery_level)
        if "critical" in battery_diagnose.lower() or "low" in battery_diagnose.lower():
            errors.append(battery_diagnose)
        
        return errors

    @staticmethod
    def check_battery(battery_level: int) -> str:
        if battery_level < 20:
            return "Battery level is critical! Please recharge!"
        elif battery_level < 50:
            return "Battery level is low."
        elif battery_level == 100:
            return "Battery level is full!"
        else:
            return "Battery level is normal."
