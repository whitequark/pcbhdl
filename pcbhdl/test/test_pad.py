import unittest
from pcbhdl.package.pad import *


class TestSMTPad(unittest.TestCase):
    def test_basic(self):
        pad = SMTPad("1", 1.0, 2.0, center=(10.0, 10.0))
        self.assertEqual(pad.name, "1")
        self.assertEqual(pad.width, 1.0)
        self.assertEqual(pad.height, 2.0)
        self.assertEqual(pad.rotation, 0.0)
        self.assertEqual(pad.center, (10.0, 10.0))

    def test_rotation(self):
        with self.assertRaises(ValueError):
            SMTPad("1", 1.0, 1.0, -10.0, center=(0.0, 0.0))
        with self.assertRaises(ValueError):
            SMTPad("1", 1.0, 1.0, 120.0, center=(0.0, 0.0))
        pad = SMTPad("1", 1.0, 1.0, 45.0, center=(0.0, 0.0))
        self.assertEqual(pad.rotation, 45.0)

    def test_locate_center(self):
        pad = SMTPad("1", 1.0, 1.0, center=(10.0, 10.0))
        self.assertEqual(pad.center, (10.0, 10.0))

    def test_locate_left_top(self):
        pad = SMTPad("1", 1.0, 1.0, left_top=(10.0, 10.0))
        self.assertEqual(pad.center, (10.5, 10.5))

    def test_locate_right_top(self):
        pad = SMTPad("1", 1.0, 1.0, right_top=(10.0, 10.0))
        self.assertEqual(pad.center, (9.5, 10.5))

    def test_locate_left_bottom(self):
        pad = SMTPad("1", 1.0, 1.0, left_bottom=(10.0, 10.0))
        self.assertEqual(pad.center, (10.5, 9.5))

    def test_locate_right_bottom(self):
        pad = SMTPad("1", 1.0, 1.0, right_bottom=(10.0, 10.0))
        self.assertEqual(pad.center, (9.5, 9.5))


class TestPTHPad(unittest.TestCase):
    def test_basic(self):
        pad = PTHPad("1", drill=1.0, center=(1.0, 1.0))
        self.assertEqual(pad.name, "1")
        self.assertEqual(pad.drill, 1.0)
        self.assertEqual(pad.center, (1.0, 1.0))
        self.assertEqual(pad.shape, "round")
        self.assertEqual(pad.rotation, 0.0)
