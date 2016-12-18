import unittest
from pcbhdl.device.pad import *
from pcbhdl.device.footprint import *


class TestFootprint(unittest.TestCase):
    def test_basic(self):
        pad = SMTRectPad("1", 1.0, 2.0, center=(0.0, 0.0))
        fp = Footprint("SMD1", pads=[pad])
        self.assertEqual(fp.name, "SMD1")
        self.assertEqual(fp.pads, [pad])

    def test_pad(self):
        pad = SMTRectPad("1", 1.0, 2.0, center=(0.0, 0.0))
        fp = Footprint("SMD1", pads=[pad])
        self.assertEqual(fp.pad("1"), pad)
        with self.assertRaises(ValueError):
            fp.pad("2")
        self.assertEqual(fp.has_pad("1"), True)
        self.assertEqual(fp.has_pad("2"), False)
