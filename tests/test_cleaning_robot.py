import unittest
from src.robots.cleaning_robot import CleaningRobot

class TestCleaningRobot(unittest.TestCase):
    def setUp(self):
        self.robot = CleaningRobot(name="Mr.Clean2", cleaningtool="vacuum")

    # Test the initial state of the robot
    def test_initial_state(self):
        self.assertEqual(self.robot.name, "Mr.Clean2")
        self.assertEqual(self.robot.cleaningtool, "vacuum")
        self.assertEqual(self.robot.battery_level, 100)
        self.assertEqual(self.robot.status, "idle")

    # Test the work status and battery level of the robot
    def test_work(self):
        self.robot.work()
        self.assertEqual(self.robot.battery_level, 80)
        self.assertEqual(self.robot.status, "idle")

    # Test the low battery status of the robot
    def test_low_battery_work(self):
        self.robot.battery_level = 10
        self.robot.work()
        self.assertEqual(self.robot.battery_level, 10)
        self.assertEqual(self.robot.status, "idle")

    # Test setting the exact cleaning tool for the robot
    def test_set_cleaningtool(self):
        self.robot.cleaningtool = "mop"
        self.assertEqual(self.robot.cleaningtool, "mop")

    # Test the robot's behavior when the battery level is at the exact threshold for working
    def test_exact_threshold_battery(self):
        self.robot.battery_level = 20
        self.robot.work()
        self.assertEqual(self.robot.battery_level, 0)
        self.assertEqual(self.robot.status, "idle")

    # Test the robot's behavior when the battery level is just below the threshold for working
    def test_battery_just_below_threshold(self):
        self.robot.battery_level = 19
        self.robot.work()
        self.assertEqual(self.robot.battery_level, 19)
        self.assertEqual(self.robot.status, "idle")

    # Test the case where the cleaning tool provided is invalid
    def test_invalid_cleaningtool(self):
        with self.assertRaises(ValueError):
            self.robot.cleaningtool = " "  # Assuming an empty string is invalid

    # Test updating the battery level and robot's status after charging
    def test_status_after_charge(self):
        self.robot.battery_level = 0
        self.robot.charge()
        self.assertEqual(self.robot.battery_level, 100)
        self.assertEqual(self.robot.status, "charging")

    # Test making sure the battery level of the robot during and after work is enough
    def test_status_during_work(self):
        self.robot.battery_level = 50
        self.robot.work()
        self.assertEqual(self.robot.status, "idle")
        self.assertEqual(self.robot.battery_level, 30)

    # Test invalid battery level in case > 100 or <0
    def test_invalid_battery_level(self):
        with self.assertRaises(ValueError):
            self.robot.battery_level = 150

    # Test invalid status of robot
    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            self.robot.status = "invalid_status"

if __name__ == '__main__':
    unittest.main()
