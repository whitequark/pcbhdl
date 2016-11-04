from .pad import Pad


class Footprint:
    """Footprint of a single package.

    Parameters
    ----------

    name : str
        Human-readable, reference name of the package.
    pads : list of pcbhdl.package.Pad
        List of pads defined by the package.
    """

    def __init__(self, name, pads=[]):
        assert isinstance(name, str)
        assert isinstance(pads, list)
        for pad in pads:
            assert isinstance(pad, Pad)

        self.name = name
        self.pads = pads
