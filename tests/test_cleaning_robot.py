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
        self.robot.clean()
        self.assertEqual(self.robot.battery_level, 0)  
    
    def test_insufficient_battery(self):
        self.robot.clean()
        self.assertEqual(self.robot.status, "idle") 
        self.assertEqual(self.robot.battery_level, 0)  
    
    def test_report_status_method(self):
        expected_output = "Robot Mr.Clean2 is idle with 100% battery" 
        self.assertEqual(self.robot.report_status(), expected_output)
    

if __name__ == '__main__':
    unittest.main()
