from robots.cleaning_robot import CleaningRobot
from robots.cooking_robot import CookingRobot 
from typing import List

def main():

    robots: List[Robot] =[
        CleaningRobot(name=" Mr.Clean 1 ", cleaningtool ="vaccum"),
        CookingRobot(name="Chef kisses 1",cooling_skill="intermediate")
    ]
for robot in robots:
    robot.report_status()
    robot.charge()
    robot.work()
if __name__ == "__main__":
    main()