import unittest
from src.robots.cleaning_robot import CleaningRobot

class TestCleaningRobot(unittest.TestCase):
    def setUp(self):
        self.robot = CleaningRobot(name="Mr.Clean2 ", cleaningtool="vaccum")

    def test_initial_state(self):
        self.assertEqual(self.robot.name, "Mr.Clean2")
        self.assertEqual(self.robot.cleaningtool, "vaccum")
        self.assertEqual(self.robot.battery_level, 100)
        self.assertEqual(self.robot.status, "idle")

    def test_work(self):
        self.robot.work()
        self.assertEqual(self.robot.battery_level, 80)
        self.assertEqual(self.robot.status, "idle")

    def test_low_battery_work(self):
        self.robot.battery_level = 10
        self.robot.work()
        self.assertEqual(self.robot.battery_level, 10)
        self.assertEqual(self.robot.status, "idle")

    def test_set_cleaningtool(self):
        self.robot.cleaningtool = "mop"
        self.assertEqual(self.robot.cleaningtool, "mop")

if __name__ == '__main__':
    unittest.main()
