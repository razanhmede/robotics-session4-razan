import unittest
import sys
import os
# So we can import from robots 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from src.robots.cooking_robot import CookingRobot

class TestCookingRobot(unittest.TestCase):

    def setUp(self):
        self.robot = CookingRobot(name="Test Chef 1", battery_level=100, status="idle", cooking_skill="beginner")

    def test_initialization(self):
        self.assertEqual(self.robot.name, "Test Chef 1")
        self.assertEqual(self.robot.battery_level, 100)
        self.assertEqual(self.robot.status, "idle")
        self.assertEqual(self.robot.cooking_skill, "beginner")
    
    def test_cooking_behavior(self):
        self.robot.cook()
        self.assertEqual(self.robot.battery_level, 0) 
    
    def test_insufficient_battery(self):
        self.robot.cook()
        self.assertEqual(self.robot.status, "idle")
        self.assertEqual(self.robot.battery_level, 0) 
    
    def test_report_status_method(self):
        expected_output = "Robot Test Chef 1 is idle with 30% battery"
        self.assertEqual(self.robot.report_status(), expected_output)
    

if __name__ == '__main__':
    unittest.main()
