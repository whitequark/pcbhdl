__all__ = ["Pad", "SMTRectPad", "PTHPad"]


class Pad:
    """Generic package pad.

    Parameters
    ----------

    name : str
        Name of the pad, unique within a package.
    """

    def __init__(self, name):
        assert isinstance(name, str)

        self.name = name


class SMTRectPad(Pad):
    """Rectangular surface-mount package pad.

    Parameters
    ----------

    width : float
        Width of the pad, in mm.
    height : float
        Height of the pad, in mm.
    center : (float, float)
        Location of the center of the pad, in mm.
    one of left, hcenter, right : float
        Location of the horizontal center or edge of the pad, in mm; cannot be
        specified together with ``center``, and is normalized to center.
    one of top, vcenter, bottom : float
        Location of the vertical center or edge of the pad, in mm; cannot be
        specified together with ``center``, and is normalized to center.
    rotation : float
        Rotation of the pad, in degrees, from 0 to 90 degrees.
    roundness : float
        Roundness of the pad corners, in percents, where the diameter of the corner circular
        arc is the percentage of the smaller side.
    """

    _HORZ_KINDS = {"left", "hcenter", "right"}
    _VERT_KINDS = {"top",  "vcenter", "bottom"}
    _ALL_KINDS  = _HORZ_KINDS | _VERT_KINDS

    def __init__(self, name, width, height, rotation=0.0, roundness=0, **kwargs):
        super().__init__(name)

        assert isinstance(width, float)
        assert isinstance(height, float)
        assert isinstance(rotation, float)
        assert isinstance(roundness, int)
        if rotation < 0.0 or rotation > 90.0:
            raise ValueError("Rotation must be between 0 and 90 degrees")
        if "center" in kwargs:
            if len(kwargs.keys() & (self._ALL_KINDS)) != 0:
                raise ValueError("None of {} may be specified together with center".
                                 format(self._ALL_KINDS))
        else:
            if rotation not in {0.0, 90.0}:
                raise ValueError("Non-axis-parallel pads must be located via center")
            if len(kwargs.keys() & self._HORZ_KINDS) != 1:
                raise ValueError("Exactly one of {} must be specified".format(self._HORZ_KINDS))
            if len(kwargs.keys() & self._VERT_KINDS) != 1:
                raise ValueError("Exactly one of {} must be specified".format(self._VERT_KINDS))
        if roundness not in range(0, 100):
            raise ValueError("Roundness must be between 0 and 100%")

        self.width = width
        self.height = height
        self.rotation = rotation
        self.roundness = roundness

        if "center" in kwargs:
            x, y = kwargs["center"]
            assert isinstance(x, float)
            assert isinstance(y, float)
            self.center = x, y
        else:
            if rotation == 0.0:
                rot_width, rot_height = width, height
            elif rotation == 90.0:
                rot_width, rot_height = height, width

            if "left" in kwargs:
                hcenter = kwargs["left"] + rot_width / 2
            elif "hcenter" in kwargs:
                hcenter = kwargs["hcenter"]
            elif "right" in kwargs:
                hcenter = kwargs["right"] - rot_width / 2
            if "top" in kwargs:
                vcenter = kwargs["top"] + rot_height / 2
            elif "vcenter" in kwargs:
                vcenter = kwargs["vcenter"]
            elif "bottom" in kwargs:
                vcenter = kwargs["bottom"] - rot_height / 2
            assert isinstance(hcenter, float)
            assert isinstance(vcenter, float)
            self.center = hcenter, vcenter


class PTHPad(Pad):
    """Plated through-hole package pad.

    Parameters
    ----------

    drill : float
        Diameter of the drilled hole, in mm.
    center : (float, float)
        Location of the center of the drilled hole, in mm.
    shape : one of "square", "round", "octagon", "oblong"
        Shape of the pad.
    rotation : float
        Rotation of the pad, in degrees, from 0 to 90 degrees.
    """

    _SHAPES = {"square", "round", "octagon", "oblong"}

    def __init__(self, name, drill, center, shape="round", rotation=0.0, diameter=None):
        super().__init__(name)

        assert isinstance(drill, float)
        x, y = center
        assert isinstance(x, float)
        assert isinstance(y, float)
        assert shape in self._SHAPES
        if rotation < 0.0 or rotation > 90.0:
            raise ValueError("Rotation must be between 0 and 90 degrees")
        assert diameter is None or isinstance(diameter, float)

        self.drill = drill
        self.center = x, y
        self.shape = shape
        self.rotation = rotation
        self.diameter = diameter
