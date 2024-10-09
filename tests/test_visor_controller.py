import unittest
from src.visor_controller import VisorController

class TestVisorController(unittest.TestCase):
    def setUp(self):
        self.visor = VisorController()

    def test_heating_enabled(self):
        self.visor.enable_heating()
        self.assertTrue(self.visor.heating_enabled)

    def test_auto_dimming_enabled(self):
        self.visor.enable_auto_dimming()
        self.assertTrue(self.visor.auto_dimming_enabled)

    def test_should_heat(self):
        self.assertTrue(self.visor.should_heat())

    def test_should_dim(self):
        self.assertTrue(self.visor.should_dim())

if __name__ == '__main__':
    unittest.main()
