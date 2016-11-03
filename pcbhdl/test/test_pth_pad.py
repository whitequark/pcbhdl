import unittest
from pcbhdl.package import PTHPad


class TestPTHPad(unittest.TestCase):
    def test_basic(self):
        pad = PTHPad("1", drill=1.0, center=(1.0, 1.0))
        self.assertEqual(pad.name, "1")
        self.assertEqual(pad.drill, 1.0)
        self.assertEqual(pad.center, (1.0, 1.0))
        self.assertEqual(pad.shape, "round")
        self.assertEqual(pad.rotation, 0.0)
