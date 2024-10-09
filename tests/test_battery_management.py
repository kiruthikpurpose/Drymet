import unittest
from src.battery_management import BatteryManagement

class TestBatteryManagement(unittest.TestCase):
    def setUp(self):
        self.battery = BatteryManagement()

    def test_initial_battery_level(self):
        self.assertEqual(self.battery.battery_level, 100)

    def test_battery_warning_low(self):
        self.battery.battery_level = 15
        with self.assertLogs(level='INFO') as log:
            self.battery.check_battery()
            self.assertIn("Warning: Battery low", log.output[0])

if __name__ == '__main__':
    unittest.main()
