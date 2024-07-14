from .base_robot import Robot

class CookingRobot(Robot):
    def __init__(self, name: str, cooking_skill: str) -> None:
        super().__init__(name)
        self._cooking_skill = cooking_skill
    def cooking_skill(self) -> str:
        return self._cooking_skill
    def cooking_skill(self, skill: str) -> None:
        if not skill:
            raise ValueError("Invalid cooking skill!!")
        self._cooking_skill = skill
    def work(self) -> None:
        if self._battery_level >= 30:
            self._status = "ABLE TO WORK"
            print(f"{self._name} is now cooking with {self._cooking_skill}")
            self._battery_level -= 30
            
        else:
            print(f"{self._name} is not able to work now. Please recharge!")
            self.report_status()
    def self_diagnose(self) -> str:
        base_diagnosis = super().self_diagnose()
        return f"{base_diagnosis}, Cooking skill: {self.cooking_skill}"
