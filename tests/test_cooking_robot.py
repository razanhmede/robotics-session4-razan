import unittest
from src.robots.cooking_robot import CookingRobot
import sys
from io import StringIO
    

class TestCookingRobot(unittest.TestCase):
     #set up the cooking robot 
    def setUp(self):
        self.robot = CookingRobot(name="Test Chef 1", cooking_skill="beginner")
     #test the initial battery level
    def test_initial_battery_level(self):
        self.assertEqual(self.robot.battery_level, 100)
     
    def test_initial_status(self):
        self.assertEqual(self.robot.status, "idle")

    def test_charge(self):
        self.robot.battery_level = 50
        self.robot.charge()
        self.assertEqual(self.robot.battery_level, 100)
        self.assertEqual(self.robot.status, "charging")

    def test_work(self):
        self.robot.work()
        self.assertEqual(self.robot.battery_level, 70)  # Assuming work decreases battery by 30
        self.assertEqual(self.robot.status, "ABLE TO WORK")

    
    def test_report_status(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.robot.report_status()
        sys.stdout = sys.__stdout__  
        printed_output = captured_output.getvalue().strip()
        expected_status_message = f"The current status of Test Chef 1 is idle. Battery level is 100%"
        self.assertIn(expected_status_message, printed_output)

    
    def test_work_with_low_battery(self):
        self.robot.battery_level = 20
        self.robot.work()
        self.assertEqual(self.robot.battery_level, 0)
        self.assertEqual(self.robot.status, "idle")

    def test_work_with_zero_battery(self):
        self.robot.battery_level = 0
        with self.assertRaises(ValueError):
            self.robot.work()

    def test_invalid_battery_level(self):
        with self.assertRaises(ValueError):
            self.robot.battery_level = 110

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            self.robot.status = "flying"

if __name__ == '__main__':
    unittest.main()
