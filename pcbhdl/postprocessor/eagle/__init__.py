import os
from lxml import etree
from lxml.builder import ElementMaker
from pcbhdl.device.pad import *


__all__ = ["EaglePostprocessor"]


eagle_dtd_path = os.path.join(os.path.dirname(__file__), "eagle-7.2.0.dtd")
with open(eagle_dtd_path, "r") as f:
    eagle_dtd = etree.DTD(f)


def add_as_str(elem, value):
    assert elem is None
    return str(value)
E = ElementMaker({
    int:   add_as_str,
    float: add_as_str
})


class EaglePostprocessor:
    """A post-processor that outputs Eagle 7.2.0+ board files."""

    def __init__(self):
        pass

    def validate(self, doc):
        return eagle_dtd.validate(doc)

    def visit_Pad(self, pad):
        if isinstance(pad, SMTRectPad):
            return self.visit_SMTRectPad(pad)
        elif isinstance(pad, PTHPad):
            return self.visit_PTHPad(pad)
        else:
            raise NotImplementedError("Cannot convert pad {}".format(pad))

    def visit_SMTRectPad(self, pad):
        return E.smd({
            "name": pad.name,
            "x": pad.center[0],
            "y": pad.center[1],
            "dx": pad.width,
            "dy": pad.height,
            "layer": 0, # FIXME?
            "rot": "R{:.1f}".format(pad.rotation)
        })

    _PTH_SHAPE_MAP = {
        "square":  "square",
        "round":   "round",
        "octagon": "octagon",
        "oblong":  "oblong"
    }

    def visit_PTHPad(self, pad):
        return E.pad({
            "name": pad.name,
            "x": pad.center[0],
            "y": pad.center[1],
            "drill": pad.drill,
            # "diameter": # FIXME
            "shape": self._PTH_SHAPE_MAP[pad.shape],
            "rot": "R{:.1f}".format(pad.rotation)
        })

    def visit_Footprint(self, footprint):
        return E.package({
            "name": footprint.name,
        }, *[self.visit_Pad(pad) for pad in footprint.pads])
