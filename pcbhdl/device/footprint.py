from .pad import Pad


__all__ = ["Footprint"]


class Footprint:
    """Footprint of a single package.

    Parameters
    ----------

    name : str
        Human-readable, reference name of the package.
    pads : list of pcbhdl.device.Pad
        List of pads defined by the package.
    """

    def __init__(self, name, pads=[]):
        assert isinstance(name, str)
        assert isinstance(pads, list)
        for pad in pads:
            assert isinstance(pad, Pad)

        self.name = name
        self.pads = pads

    def pad(self, name):
        for pad in self.pads:
            if pad.name == name:
                return pad
        raise ValueError("Undefined pad {}".format(pad))

    def has_pad(self, name):
        try:
            self.pad(name)
            return True
        except ValueError:
            return False
