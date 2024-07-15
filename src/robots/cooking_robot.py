from .base_robot import Robot
#cooking robot has a set cooking skill method which checks for valid cooking skill 
#cook method which makes sure that the battery level is valid for the robot to cook
#self disgnose method to check the validity of the cooking skill
class CookingRobot(Robot):
    def __init__(self, name: str, battery_level: int, status: str , cooking_skill: str):
        Robot.__init__(name, battery_level,status)
        #self.set_cooking_skill(cooking_skill)
        self.cooking_skill=cooking_skill
    def get_cooking_skill(self) -> str:
        return self.cooking_skill

    def set_cooking_skill(self, cooking_skill: str) -> None:
        if cooking_skill in {"beginner", "intermediate", "expert"}:
            self.cooking_skill = cooking_skill
        else:
            raise ValueError("Cooking skill must be 'beginner', 'intermediate', or 'expert'.")

    def cook(self) -> None:
        if self.battery_level >= 30:
            self.status = "ABLE TO WORK"
            print(f"{self.name} is now cooking with {self.cooking_skill}")
            self.battery_level -= 30
            print(f"Battery level: {self.battery_level}%")
            self.status = "idle"
        else:
            print(f"{self.name} is not able to work now. Please recharge!")
            self.report_status()

    def self_diagnose(self) -> list:
        base_diagnosis = super().self_diagnose()
        if self.cooking_skill not in ["beginner", "intermediate", "expert"]:
            base_diagnosis.append("Invalid cooking skill!")
        return base_diagnosis

