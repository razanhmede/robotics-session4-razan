import unittest
from robots.base_robot import robots
from abc import ABC, abstractmethod 

class TestRobot(unittest.TestCase):
    def setUp(self):
        class Testable_robot(Robot):
            def work(self):
                pass
         self.robot= Testable_robot(BOB 2000)
    def test_initial_state(self):
        self.assertEqual(self.robot.name, "BOB 2000")
        self.assertEqual(self.robot.battery_level, 100)
        self.assertEqual(self.robot.status, "idle")

    def test_charge(self):
        self.robot.battery_level = 60
        self.robot.charge()
        self.assertEqual(self.robot.battery_level, 100)
        self.assertEqual(self.robot.status, "charging")

    def test_setters(self):
        self.robot.battery_level = 50
        self.assertEqual(self.robot.battery_level, 50)
        
        self.robot.status = "working"
        self.assertEqual(self.robot.status, "working")
        
        with self.assertRaises(ValueError):
            self.robot.battery_level = 150

        with self.assertRaises(ValueError):
            self.robot.status = "invalid_status"

    def test_report_ssstatus(self):
        self.robot.report_status()