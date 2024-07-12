from abc import ABC, abstractmethod

class Robot(ABC):
    def __init__(self, name: str):
        self._name = name
        self._battery_level = 100
        self._status = "idle"
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def battery_level(self) -> int:
        return self._battery_level
    
    @battery_level.setter
    def battery_level(self, level: int) -> None:
        if 0 <= level <= 100:
            self._battery_level = level
        else:
            raise ValueError("Battery level must be between 0 and 100.")
    
    @property
    def status(self) -> str:
        return self._status
    
    @status.setter
    def status(self, status: str) -> None:
        if status in {"idle", "ABLE TO WORK", "charging"}:
            self._status = status
        else:
            raise ValueError("Status must be 'idle', 'ABLE TO WORK', or 'charging'.")
    
    def charge(self) -> None:
        self._battery_level = 100
        self._status = "charging"
        print(f"{self.name} is now charging. The battery level is {self._battery_level}%.")
    
    @abstractmethod
    def work(self) -> None:
        pass
    
    def report_status(self) -> None:
        print(f"The current status of {self.name} is {self._status}. Battery level is {self._battery_level}%.")


if __name__ == "__main__":
    robot = Robot("BOB 2000")
    robot.charge()
    robot.report_status()
