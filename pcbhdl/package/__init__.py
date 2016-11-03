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


class SMTPad(Pad):
    """Rectangular surface-mount package pad.

    Parameters
    ----------

    width : float
        Width of the pad, in mm.
    height : float
        Height of the pad, in mm.
    one of center, left_top, right_top, left_bottom, right_bottom : (float, float)
        Coordinates of the pad, in mm; if specified other than as center, coordinates
        are normalized to the center.
    rotation : float
        Rotation of the pad, in degrees, from 0 to 90 degrees.
    """

    _ORIGIN_KINDS = {"center", "left_top", "right_top", "left_bottom", "right_bottom"}

    def __init__(self, name, width, height, rotation=0.0, **kwargs):
        super().__init__(name)

        assert isinstance(width, float)
        assert isinstance(height, float)
        assert isinstance(rotation, float)
        if rotation < 0.0 or rotation > 90.0:
            raise ValueError("Rotation must be between 0 and 90 degrees")
        if len(kwargs.keys() & self._ORIGIN_KINDS) != 1:
            raise ValueError("Exactly one of {} must be specified".format(self._ORIGIN_KINDS))
        if "center" not in kwargs and rotation not in {0.0, 90.0}:
            raise ValueError("Non-axis-parallel pads must be located via center")

        self.width = width
        self.height = height
        self.rotation = rotation

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

            if "left_top" in kwargs:
                left, top = kwargs["left_top"]
                assert isinstance(left, float)
                assert isinstance(top, float)
                self.center = left + rot_width / 2, top + rot_height / 2
            elif "right_top" in kwargs:
                right, top = kwargs["right_top"]
                assert isinstance(right, float)
                assert isinstance(top, float)
                self.center = right - rot_width / 2, top + rot_height / 2
            elif "left_bottom" in kwargs:
                left, bottom = kwargs["left_bottom"]
                assert isinstance(left, float)
                assert isinstance(bottom, float)
                self.center = left + rot_width / 2, bottom - rot_height / 2
            elif "right_bottom" in kwargs:
                right, bottom = kwargs["right_bottom"]
                assert isinstance(right, float)
                assert isinstance(bottom, float)
                self.center = right - rot_width / 2, bottom - rot_height / 2


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
