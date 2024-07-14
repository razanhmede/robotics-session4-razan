from abc import ABC, abstractmethod

class Robot(ABC):
    def __init__(self, name: str):
        self._name = name
        self._battery_level = 100
        self._status = "idle"
    def name(self) -> str:
        return self._name
    def battery_level(self) -> int:
        return self._battery_level
    def battery_level(self, level: int) -> None:
        if 0 <= level <= 100:
            self._battery_level = level
        else:
            raise ValueError("Battery level must be between 0 and 100.")
    def status(self) -> str:
        return self._status
    def status(self, status: str) -> None:
        if status in {"idle", "ABLE TO WORK", "charging"}:
            self._status = status
        else:
            raise ValueError("Status must be 'idle', 'ABLE TO WORK', or 'charging'.")
    def charge(self) -> None:
        self._battery_level = 100
        self._status = "charging"
    def work(self) -> None:
        pass
    def report_status(self) -> None:
        print(f"The current status of {self.name} is {self._status}. Battery level is {self._battery_level}%.")
    def self_diagnose(self) ->str:
        battery_diagnose = self.check_battery(self.battery_level)
        status_diagnose=self.check_status(self.status)
        return f"Robot Diagnosis: {battery_diagnose},{status_diagnose}"
    def check_battery(battery_level: int) ->str:
        if battery_level <20:
            return "Battery level is critical!Please recharge!"
        elif battery_level <50:
            return "Battery level is low "
        elif battery_level=100:
            return "Battery level is full!"
        else:
            return "Battery level is normal"

    def check_status(cls, status: str) ->str:
        if status == "idle":
            return "Robot is currently not performing any tasks"
        if status =="ABLE TO WORK":
            return "Robot is currently working"
        if status == "charging":
            return "Robot is currently charging"

if __name__ == "__main__":
    robot = Robot("BOB 2000")
    robot.charge()
    robot.report_status()
