import unittest
from src.robots.base_robot import Robot  # Assuming Robot class is defined in base_robot.py

class TestRobot(unittest.TestCase):
    def setUp(self):
        class TestableRobot(Robot):
            def work(self):
                pass
        self.robot = TestableRobot("BOB 2000")

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
        
        self.robot.status = "ABLE TO WORK"
        self.assertEqual(self.robot.status, "ABLE TO WORK")
        
        with self.assertRaises(ValueError):
            self.robot.battery_level = 150

        with self.assertRaises(ValueError):
            self.robot.status = "invalid_status"

    def test_report_status(self):
        # Assuming report_status() prints to stdout or logs
        # You can capture the output and assert on it if needed
        pass  # Implement your test logic here

if __name__ == "__main__":
    unittest.main()
