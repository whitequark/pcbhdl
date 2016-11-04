import unittest
from pcbhdl.device import *


class MockComponent(Component):
    name_prefix = "U"
    footprint = Footprint("SMD1", pads=[
        SMTPad("1", 1.0, 1.0, center=(0.0, 0.0)),
        SMTPad("2", 1.0, 1.0, center=(2.0, 0.0)),
        SMTPad("3", 1.0, 1.0, center=(4.0, 0.0)),
    ])
    signals = {
        "A": "1",
        "B": ["2", "3"]
    }


class TestComponent(unittest.TestCase):
    def test_basic(self):
        comp = MockComponent()
        self.assertEqual(comp.manufacturer, None)
        self.assertEqual(comp.part_number, None)
        self.assertEqual(comp.order_codes, None)

    def test_mfg(self):
        comp = MockComponent(manufacturer="ACME", part_number="123",
                             order_codes={"Quik-Ship": "123-456"})
        self.assertEqual(comp.manufacturer, "ACME")
        self.assertEqual(comp.part_number, "123")
        self.assertEqual(comp.order_codes, {"Quik-Ship": "123-456"})
