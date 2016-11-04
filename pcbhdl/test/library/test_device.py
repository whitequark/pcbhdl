import unittest
from pcbhdl.library.device.passive import *


class TestResistor(unittest.TestCase):
    def test_basic(self):
        res = R_I_0805(150.0, tolerance=10.0)
        self.assertEqual(res.value, 150.0)
        self.assertEqual(res.tolerance, 10.0)
        self.assertEqual(res.series, None)

    def test_series(self):
        res = R_I_0805(151.0, series="E12")
        self.assertEqual(res.value, 150.0)
        self.assertEqual(res.tolerance, 10.0)
        self.assertEqual(res.series, "E12")
