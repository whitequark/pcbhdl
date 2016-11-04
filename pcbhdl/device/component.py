from .pad import Pad
from .footprint import Footprint


__all__ = ["Component"]


class Component:
    """Component with a specific footprint, name, value, and other attributes.

    Class attributes
    ----------------

    name_prefix : str
        Reference designator prefix (e.g. "R" for resistors).

    footprint : pcbhdl.device.Footprint
        Package footprint.

    signals : dict of str to (str or list of str)
        Mapping from logical signal names (e.g. "GND" or "!SHDN") to
        physical pad names (e.g. "1" or "A6"). Either a single pad name or a list
        of pad names can be specified.

    Attributes
    ----------

    name : str
        Full reference designator, starting with the prefix (e.g. "R1" for a resistor).

    manufacturer : None or str
        Manufacturer name, e.g. "Murata".

    part_number : None or str
        Manufacturer part number, e.g. "GRM155R71H103KA88D".

    order_codes : None or dict of str to str
        Mapping from supplier name to supplier order code, e.g. {"Digi-Key": "490-4516-2-ND"}.
    """

    name_prefix = None
    footprint = None
    signals = None

    def __init__(self, manufacturer=None, part_number=None, order_codes=None):
        assert isinstance(self.name_prefix, str)
        assert isinstance(self.footprint, Footprint)
        assert isinstance(self.signals, dict)
        for signal in self.signals:
            assert isinstance(signal, str)
            pad_names = self.signals[signal]
            assert isinstance(pad_names, (str, list))
            if isinstance(pad_names, list):
                for pad_name in pad_names:
                    assert isinstance(pad_name, str)
                    assert self.footprint.has_pad(pad_name)
            else:
                assert self.footprint.has_pad(pad_names)

        assert manufacturer is None or isinstance(manufacturer, str)
        assert part_number is None or isinstance(part_number, str)
        assert order_codes is None or isinstance(order_codes, dict)
        for supplier in order_codes or {}:
            assert isinstance(supplier, str)
            assert isinstance(order_codes[supplier], str)
        self.manufacturer = manufacturer
        self.part_number = part_number
        self.order_codes = order_codes
