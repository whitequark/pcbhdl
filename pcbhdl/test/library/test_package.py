import unittest
from pcbhdl.library.package.passive import *


class TestPackage(unittest.TestCase):
    def test_eia_two_terminal(self):
        pkg = EIA_I_0603
        self.assertEqual(pkg.name, "EIA_I_0603")
        self.assertEqual(pkg.pads[0].name,   "1")
        self.assertEqual(pkg.pads[0].center, (-0.9, 0.0))
        self.assertEqual(pkg.pads[0].width,  0.8)
        self.assertEqual(pkg.pads[0].height, 1.0)
        self.assertEqual(pkg.pads[1].name,   "2")
        self.assertEqual(pkg.pads[1].center, (0.9, 0.0))
        self.assertEqual(pkg.pads[1].width,  0.8)
        self.assertEqual(pkg.pads[1].height, 1.0)
