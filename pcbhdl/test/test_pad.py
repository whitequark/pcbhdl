import unittest
from pcbhdl.device.pad import *


class TestSMTRectPad(unittest.TestCase):
    def test_basic(self):
        pad = SMTRectPad("1", 1.0, 2.0, center=(10.0, 10.0))
        self.assertEqual(pad.name, "1")
        self.assertEqual(pad.width, 1.0)
        self.assertEqual(pad.height, 2.0)
        self.assertEqual(pad.rotation, 0.0)
        self.assertEqual(pad.center, (10.0, 10.0))

    def test_rotation(self):
        pad = SMTRectPad("1", 1.0, 1.0, 45.0, center=(0.0, 0.0))
        self.assertEqual(pad.rotation, 45.0)

    def test_rotation_bad(self):
        with self.assertRaises(ValueError):
            SMTRectPad("1", 1.0, 1.0, -10.0, center=(0.0, 0.0))
        with self.assertRaises(ValueError):
            SMTRectPad("1", 1.0, 1.0, 120.0, center=(0.0, 0.0))

    def test_roundness(self):
        pad = SMTRectPad("1", 1.0, 1.0, roundness=30, center=(0.0, 0.0))
        self.assertEqual(pad.roundness, 30)

    def test_roundness_bad(self):
        with self.assertRaises(ValueError):
            SMTRectPad("1", 1.0, 1.0, roundness=-1, center=(0.0, 0.0))
        with self.assertRaises(ValueError):
            SMTRectPad("1", 1.0, 1.0, roundness=120, center=(0.0, 0.0))

    def test_locate_center(self):
        pad = SMTRectPad("1", 1.0, 1.0, center=(10.0, 10.0))
        self.assertEqual(pad.center, (10.0, 10.0))

    def test_locate_left_top(self):
        pad = SMTRectPad("1", 1.0, 1.0, left=10.0, top=10.0)
        self.assertEqual(pad.center, (10.5, 10.5))

    def test_locate_hcenter_top(self):
        pad = SMTRectPad("1", 1.0, 1.0, hcenter=10.0, top=10.0)
        self.assertEqual(pad.center, (10.0, 10.5))

    def test_locate_right_top(self):
        pad = SMTRectPad("1", 1.0, 1.0, right=10.0, top=10.0)
        self.assertEqual(pad.center, (9.5, 10.5))

    def test_locate_left_vcenter(self):
        pad = SMTRectPad("1", 1.0, 1.0, left=10.0, vcenter=10.0)
        self.assertEqual(pad.center, (10.5, 10.0))

    def test_locate_left_bottom(self):
        pad = SMTRectPad("1", 1.0, 1.0, left=10.0, bottom=10.0)
        self.assertEqual(pad.center, (10.5, 9.5))

    def test_locate_right_bottom(self):
        pad = SMTRectPad("1", 1.0, 1.0, right=10.0, bottom=10.0)
        self.assertEqual(pad.center, (9.5, 9.5))

    def test_locate_bad(self):
        with self.assertRaises(ValueError):
            SMTRectPad("1", 1.0, 1.0, center=(0.0, 0.0), left=1.0)
        with self.assertRaises(ValueError):
            SMTRectPad("1", 1.0, 1.0, center=(0.0, 0.0), top=1.0)
        with self.assertRaises(ValueError):
            SMTRectPad("1", 1.0, 1.0, left=1.0)
        with self.assertRaises(ValueError):
            SMTRectPad("1", 1.0, 1.0, top=1.0)


class TestSMTRoundPad(unittest.TestCase):
    def test_basic(self):
        pad = SMTRoundPad("1", diameter=1.0, center=(2.0, 3.0))
        self.assertEqual(pad.diameter, 1.0)
        self.assertEqual(pad.center, (2.0, 3.0))


class TestPTHPad(unittest.TestCase):
    def test_basic(self):
        pad = PTHPad("1", drill=1.0, center=(1.0, 1.0))
        self.assertEqual(pad.name, "1")
        self.assertEqual(pad.drill, 1.0)
        self.assertEqual(pad.center, (1.0, 1.0))
        self.assertEqual(pad.shape, "round")
        self.assertEqual(pad.rotation, 0.0)
