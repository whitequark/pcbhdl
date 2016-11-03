import unittest
from lxml import etree
from lxml_asserts.testcase import LxmlTestCaseMixin
from pcbhdl.package.pad import *
from pcbhdl.postprocessor.eagle import *


class TestEaglePostprocessor(unittest.TestCase, LxmlTestCaseMixin):
    def setUp(self):
        self.post = EaglePostprocessor()

    def assertValid(self, doc):
        self.assertTrue(self.post.validate(doc))

    def test_smt_pad(self):
        pad = SMTPad("1", width=1.0, height=2.0, center=(10.0, 10.0), rotation=45.0)
        doc = self.post.visit_SMTPad(pad)
        self.assertValid(doc)
        self.assertXmlEqual(doc, etree.XML("""
            <smd name="1" x="10.0" y="10.0" dx="1.0" dy="2.0" layer="0" rot="R45.0"/>
        """))
        print()

    def test_pth_pad(self):
        pad = PTHPad("1", drill=1.0, center=(10.0, 10.0), rotation=45.0)
        doc = self.post.visit_PTHPad(pad)
        self.assertValid(doc)
        self.assertXmlEqual(doc, etree.XML("""
            <pad name="1" x="10.0" y="10.0" drill="1.0" rot="R45.0" shape="round"/>
        """))
