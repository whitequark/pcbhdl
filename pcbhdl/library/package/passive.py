from ...device import Footprint, SMTPad


__all__ = ["EIATwoTerminalSMT",
           "EIA_I_0402", "EIA_I_0603", "EIA_I_0805"]


class EIATwoTerminalSMT(Footprint):
    """Two-terminal EIA SMT package (0805, 0603, etc).

    Parameters
    ----------

    pad_width : float
        Dimension of pad across the long side of package, in mm.
    pad_height : float
        Dimension of pad across the short side of package, in mm.
    package_width : float
        Distance between outermost pad edges across the long side of the package, in mm.
    """

    def __init__(self, name, pad_width, pad_height, package_width):
        assert isinstance(pad_width, float)
        assert isinstance(pad_height, float)
        assert isinstance(package_width, float)

        pads = [
            SMTPad(name="1", width=pad_width, height=pad_height,
                   vcenter=0.0, left=-package_width / 2),
            SMTPad(name="2", width=pad_width, height=pad_height,
                   vcenter=0.0, right=package_width / 2)
        ]
        super().__init__(name, pads)


EIA_I_0402 = EIATwoTerminalSMT("EIA_I_0402", pad_width=0.5, pad_height=0.5, package_width=1.5)
"""EIA imperial 0402 SMT passive package."""

EIA_I_0603 = EIATwoTerminalSMT("EIA_I_0603", pad_width=0.8, pad_height=1.0, package_width=2.6)
"""EIA imperial 0603 SMT passive package."""

EIA_I_0805 = EIATwoTerminalSMT("EIA_I_0805", pad_width=1.2, pad_height=1.3, package_width=3.4)
"""EIA imperial 0805 SMT passive package."""
