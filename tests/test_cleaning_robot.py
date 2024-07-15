import unittest
import os
import sys

# Add 'src' directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import the CleaningRobot class from robots package
from robots.cleaning_robot import CleaningRobot

class TestCleaningRobot(unittest.TestCase):

    def setUp(self):
        self.robot = CleaningRobot(name="Mr.Clean2", battery_level=100, status="idle", cleaningtool="vacuum")

    def test_initialization(self):
        # Test that the robot is initialized correctly
        self.assertEqual(self.robot.name, "Mr.Clean2")
        self.assertEqual(self.robot.battery_level, 100)
        self.assertEqual(self.robot.status, "idle")
        self.assertEqual(self.robot.cleaningtool, "vacuum")
    
    def test_cleaning_behavior(self):
        # Test that the robot can clean a room and deplete the battery
        self.robot.clean()
        self.assertEqual(self.robot.battery_level, 0)  # Battery will be depleted after one session
    
    def test_insufficient_battery(self):
        # Attempt to work with insufficient battery
        self.robot.clean()
        self.assertEqual(self.robot.status, "idle")  # Status should remain idle
        self.assertEqual(self.robot.battery_level, 0)  # Battery should not decrease further
    
    def test_report_status_method(self):
        # Test that the report_status() works properly
        expected_output = "Robot Mr.Clean2 is idle with 100% battery"  # Adjust based on your implementation
        self.assertEqual(self.robot.report_status(), expected_output)
    

if __name__ == '__main__':
    unittest.main()
