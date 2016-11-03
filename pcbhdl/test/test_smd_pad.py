import unittest
from pcbhdl.package import SMTPad


class TestSMTPad(unittest.TestCase):
    def test_basic(self):
        pad = SMTPad("1", 1.0, 2.0, origin=(0.0, 0.0))
        self.assertEqual(pad.name, "1")
        self.assertEqual(pad.width, 1.0)
        self.assertEqual(pad.height, 2.0)

    def test_rotation(self):
        with self.assertRaises(ValueError):
            SMTPad("1", 1.0, 1.0, -10.0, origin=(0.0, 0.0))
        with self.assertRaises(ValueError):
            SMTPad("1", 1.0, 1.0, 120.0, origin=(0.0, 0.0))
        pad = SMTPad("1", 1.0, 1.0, 45.0, origin=(0.0, 0.0))
        self.assertEqual(pad.rotation, 45.0)

    def test_origin_explicit(self):
        pad = SMTPad("1", 1.0, 1.0, origin=(10.0, 10.0))
        self.assertEqual(pad.origin, (10.0, 10.0))

    def test_origin_left_top(self):
        pad = SMTPad("1", 1.0, 1.0, left_top=(10.0, 10.0))
        self.assertEqual(pad.origin, (10.5, 10.5))

    def test_origin_right_top(self):
        pad = SMTPad("1", 1.0, 1.0, right_top=(10.0, 10.0))
        self.assertEqual(pad.origin, (9.5, 10.5))

    def test_origin_left_bottom(self):
        pad = SMTPad("1", 1.0, 1.0, left_bottom=(10.0, 10.0))
        self.assertEqual(pad.origin, (10.5, 9.5))

    def test_origin_right_bottom(self):
        pad = SMTPad("1", 1.0, 1.0, right_bottom=(10.0, 10.0))
        self.assertEqual(pad.origin, (9.5, 9.5))
