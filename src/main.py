from robots.cleaning_robot import CleaningRobot
from robots.cooking_robot import CookingRobot
from robots.base_robot import Robot  # Import the base class if not imported already
from typing import List

def main():
    robots: List[Robot] = [
        CleaningRobot(name="Mr. Clean 1", cleaningtool="vacuum"),
        CookingRobot(name="Chef Kisses 1", cooking_skill="intermediate")
    ]

    for robot in robots:
        robot.report_status()
        robot.charge()
        robot.work()

if __name__ == "__main__":
    main()
