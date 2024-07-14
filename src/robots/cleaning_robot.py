from .base_robot import Robot

class CleaningRobot(Robot):
    def __init__(self, name: str, cleaningtool: str) -> None:
        super().__init__(name)
        self.cleaningtool = cleaningtool 
    def cleaningtool(self) -> str:
        return self._cleaningtool
    def cleaningtool(self, tool: str) -> None:
        if tool not in ["vacuum", "mop"]:
            raise ValueError("Invalid cleaning tool!!")
        self._cleaningtool = tool
    def work(self) -> None:
        if self.battery_level >= 20:
            self.status = "ABLE TO WORK"
            print(f"{self.name} is now cleaning with {self.cleaningtool}")
            self.battery_level -= 20
            self.status = "idle"
        else:
            print(f"{self.name} is not able to work now. Please recharge!")
            self.report_status()
    def self_diagnose(self) -> str:
        base_diagnosis = super().self_diagnose()
        return f"{base_diagnosis}, Cleaning tool: {self.cleaningtool}"

