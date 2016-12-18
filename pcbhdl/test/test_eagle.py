import unittest
from lxml import etree
from lxml_asserts.testcase import LxmlTestCaseMixin
from pcbhdl.device.pad import *
from pcbhdl.device.footprint import *
from pcbhdl.postprocessor.eagle import *


class TestEaglePostprocessor(unittest.TestCase, LxmlTestCaseMixin):
    def setUp(self):
        self.post = EaglePostprocessor()

    def assertValid(self, doc):
        self.assertTrue(self.post.validate(doc))

    def test_smt_rect_pad(self):
        pad = SMTRectPad("1", width=1.0, height=2.0, center=(10.0, 15.0),
                         rotation=45.0, roundness=30)
        doc = self.post.visit_Pad(pad)
        self.assertValid(doc)
        self.assertXmlEqual(doc, etree.XML("""
            <smd name="1" x="10.0" y="15.0" dx="1.0" dy="2.0" layer="0"
                 rot="R45.0" roundness="30"/>
        """))

    def test_smt_round_pad(self):
        pad = SMTRoundPad("1", diameter=1.0, center=(10.0, 15.0))
        doc = self.post.visit_Pad(pad)
        self.assertValid(doc)
        self.assertXmlEqual(doc, etree.XML("""
            <smd name="1" x="10.0" y="15.0" dx="1.0" dy="1.0" layer="0"
                 roundness="100"/>
        """))

    def test_pth_pad(self):
        pad = PTHPad("1", drill=1.0, center=(10.0, 10.0), rotation=45.0)
        doc = self.post.visit_Pad(pad)
        self.assertValid(doc)
        self.assertXmlEqual(doc, etree.XML("""
            <pad name="1" x="10.0" y="10.0" drill="1.0" rot="R45.0" shape="round"/>
        """))

    def test_footprint(self):
        pad = SMTRectPad("1", width=1.0, height=2.0, center=(0.0, 0.0))
        fp  = Footprint("SMD1", pads=[pad])
        doc = self.post.visit_Footprint(fp)
        self.assertValid(doc)
        self.assertXmlEqual(doc, etree.XML("""
            <package name="SMD1">
                <smd name="1" x="0.0" y="0.0" dx="1.0" dy="2.0" layer="0"
                     rot="R0.0" roundness="0"/>
            </package>
        """))
