import unittest
from src.display_controller import DisplayController

class TestDisplayController(unittest.TestCase):
    def setUp(self):
        self.display = DisplayController()

    def test_alerts_are_added(self):
        self.display.check_alerts()
        self.assertGreater(len(self.display.alerts), 0)

    def test_show_alerts(self):
        self.display.check_alerts()
        self.display.show_alerts()
        self.assertEqual(len(self.display.alerts), 0)

if __name__ == '__main__':
    unittest.main()
