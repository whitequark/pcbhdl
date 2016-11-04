import unittest
from pcbhdl.device.pad import *


class TestSMTPad(unittest.TestCase):
    def test_basic(self):
        pad = SMTPad("1", 1.0, 2.0, center=(10.0, 10.0))
        self.assertEqual(pad.name, "1")
        self.assertEqual(pad.width, 1.0)
        self.assertEqual(pad.height, 2.0)
        self.assertEqual(pad.rotation, 0.0)
        self.assertEqual(pad.center, (10.0, 10.0))

    def test_rotation(self):
        pad = SMTPad("1", 1.0, 1.0, 45.0, center=(0.0, 0.0))
        self.assertEqual(pad.rotation, 45.0)

    def test_rotation_bad(self):
        with self.assertRaises(ValueError):
            SMTPad("1", 1.0, 1.0, -10.0, center=(0.0, 0.0))
        with self.assertRaises(ValueError):
            SMTPad("1", 1.0, 1.0, 120.0, center=(0.0, 0.0))

    def test_locate_center(self):
        pad = SMTPad("1", 1.0, 1.0, center=(10.0, 10.0))
        self.assertEqual(pad.center, (10.0, 10.0))

    def test_locate_left_top(self):
        pad = SMTPad("1", 1.0, 1.0, left=10.0, top=10.0)
        self.assertEqual(pad.center, (10.5, 10.5))

    def test_locate_hcenter_top(self):
        pad = SMTPad("1", 1.0, 1.0, hcenter=10.0, top=10.0)
        self.assertEqual(pad.center, (10.0, 10.5))

    def test_locate_right_top(self):
        pad = SMTPad("1", 1.0, 1.0, right=10.0, top=10.0)
        self.assertEqual(pad.center, (9.5, 10.5))

    def test_locate_left_vcenter(self):
        pad = SMTPad("1", 1.0, 1.0, left=10.0, vcenter=10.0)
        self.assertEqual(pad.center, (10.5, 10.0))

    def test_locate_left_bottom(self):
        pad = SMTPad("1", 1.0, 1.0, left=10.0, bottom=10.0)
        self.assertEqual(pad.center, (10.5, 9.5))

    def test_locate_right_bottom(self):
        pad = SMTPad("1", 1.0, 1.0, right=10.0, bottom=10.0)
        self.assertEqual(pad.center, (9.5, 9.5))

    def test_locate_bad(self):
        with self.assertRaises(ValueError):
            SMTPad("1", 1.0, 1.0, center=(0.0, 0.0), left=1.0)
        with self.assertRaises(ValueError):
            SMTPad("1", 1.0, 1.0, center=(0.0, 0.0), top=1.0)
        with self.assertRaises(ValueError):
            SMTPad("1", 1.0, 1.0, left=1.0)
        with self.assertRaises(ValueError):
            SMTPad("1", 1.0, 1.0, top=1.0)


class TestPTHPad(unittest.TestCase):
    def test_basic(self):
        pad = PTHPad("1", drill=1.0, center=(1.0, 1.0))
        self.assertEqual(pad.name, "1")
        self.assertEqual(pad.drill, 1.0)
        self.assertEqual(pad.center, (1.0, 1.0))
        self.assertEqual(pad.shape, "round")
        self.assertEqual(pad.rotation, 0.0)
