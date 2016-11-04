import math
from ...device import Component
from ..iec60063 import IEC60063_SERIES, iec60063_nearest
from ..package.passive import *


__all__ = ["Resistor", "R_I_0402", "R_I_0603", "R_I_0805"]


class Resistor(Component):
    """Two-terminal resistor.

    Footprint of the resistor must define pads named "1" and "2".

    Parameters
    ----------

    value : float
        Resistance, in ohms.

    tolerance : float
        Tolerance, in percents. Tolerance value of 10.0 corresponds to a ±10% resistor.
        Cannot be specified together with ``series``.

    series : one of "E6", "E12", "E24", "E48", "E96"
        EIA "E" series, specifying the number of logarithmic steps per decade. If specified,
        ``value`` is rounded to the nearest value present in the series, and ``tolerance``
        is set to the value corresponding to the decade.

        The "E12" series is used by default.
    """

    name_prefix = "R"
    signals = {"1": "1", "2": "2"}

    def __init__(self, value, **kwargs):
        tolerance = kwargs.pop("tolerance", None)
        series = kwargs.pop("series", None)
        assert isinstance(value, float)
        assert tolerance is None or isinstance(tolerance, float)
        assert series is None or series in IEC60063_SERIES

        if tolerance is None and series is None:
            series = "E12"
        if tolerance is not None and series is not None:
            raise ValueError("Only one of tolerance and series must be specified")

        if series is not None:
            if series == "E6":
                tolerance = 20.0
            elif series == "E12":
                tolerance = 10.0
            elif series == "E24":
                tolerance =  5.0
            elif series == "E48":
                tolerance =  2.0
            elif series == "E96":
                tolerance =  1.0
            value = iec60063_nearest(IEC60063_SERIES[series], value)

        super().__init__(**kwargs)
        self.value = value
        self.tolerance = tolerance
        self.series = series


class R_I_0402(Resistor):
    """A resistor in EIA imperial 0402 SMT passive package."""
    footprint = EIA_I_0402


class R_I_0603(Resistor):
    """A resistor in EIA imperial 0603 SMT passive package."""
    footprint = EIA_I_0603


class R_I_0805(Resistor):
    """A resistor in EIA imperial 0805 SMT passive package."""
    footprint = EIA_I_0805
