import unittest
import os
import sys

# Add 'src' directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import the Robot class from robots package
from robots.base_robot import Robot

class TestRobot(unittest.TestCase):
    
    def setUp(self):
        # Initialize objects that will be used in the tests
        self.robot = Robot(name="BOB 2000", battery_level=50, status="idle")
    
    def test_initialization(self):
        # Test that the robot is initialized correctly
        self.assertEqual(self.robot.name, "BOB 2000")
        self.assertEqual(self.robot.battery_level, 50)
        self.assertEqual(self.robot.status, "idle")
    
    def test_charge_method(self):
        # Test that the charge method works correctly
        self.robot.charge()
        self.assertEqual(self.robot.battery_level, 100)
    
    def test_report_status_method(self):
        # Test that the report_status method works correctly
        expected_output = "Robot BOB 2000 is idle with 50% battery"
        self.assertEqual(self.robot.report_status(), expected_output)

if __name__ == '__main__':
    unittest.main()

