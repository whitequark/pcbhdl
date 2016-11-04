import unittest
from pcbhdl.library.iec60063 import *


class TestNearest(unittest.TestCase):
    def test_e6(self):
        self.assertEqual(iec60063_nearest(E6, 100), 100.0)
        self.assertEqual(iec60063_nearest(E6, 110), 100.0)
        self.assertEqual(iec60063_nearest(E6, 124), 100.0)
        self.assertEqual(iec60063_nearest(E6, 126), 150.0)
        self.assertEqual(iec60063_nearest(E6, 140), 150.0)
        self.assertEqual(iec60063_nearest(E6, 170), 150.0)

    def test_e12(self):
        self.assertEqual(iec60063_nearest(E12, 121), 120.0)
        self.assertEqual(iec60063_nearest(E12, 133), 120.0)
        self.assertEqual(iec60063_nearest(E12, 135), 150.0)
        self.assertEqual(iec60063_nearest(E12, 210), 220.0)
        self.assertEqual(iec60063_nearest(E12, 250), 270.0)

    def test_e24(self):
        self.assertEqual(iec60063_nearest(E24, 310), 300.0)
        self.assertEqual(iec60063_nearest(E24, 325), 330.0)

    def test_e48(self):
        self.assertEqual(iec60063_nearest(E48, 310), 316.0)
