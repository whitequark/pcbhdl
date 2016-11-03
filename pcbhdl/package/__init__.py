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
    one of origin, left_top, right_top, left_bottom, right_bottom : (float, float)
        Coordinates of the pad, in mm; if specified other than as origin, coordinates
        are normalized to the origin.
    rotation : float
        Rotation of the pad, in degrees, from 0 to 90 degrees.
    """

    _ORIGIN_ARGS = {"origin", "left_top", "right_top", "left_bottom", "right_bottom"}

    def __init__(self, name, width, height, rotation=0.0, **kwargs):
        super().__init__(name)

        assert isinstance(width, float)
        assert isinstance(height, float)
        assert isinstance(rotation, float)
        if rotation < 0.0 or rotation > 90.0:
            raise ValueError("Rotation must be between 0 and 90 degrees")
        if len(kwargs.keys() & self._ORIGIN_ARGS) != 1:
            raise ValueError("Exactly one of {} must be specified".format(self._ORIGIN_ARGS))
        if "origin" not in kwargs and rotation not in {0.0, 90.0}:
            raise ValueError("Non-axis-parallel pads must be located via origin")

        self.width = width
        self.height = height
        self.rotation = rotation

        if "origin" in kwargs:
            self.origin = kwargs["origin"]
        else:
            if rotation == 0.0:
                rot_width, rot_height = width, height
            elif rotation == 90.0:
                rot_width, rot_height = height, width

            if "left_top" in kwargs:
                left, top = kwargs["left_top"]
                assert isinstance(left, float)
                assert isinstance(top, float)
                self.origin = left + rot_width / 2, top + rot_height / 2
            elif "right_top" in kwargs:
                right, top = kwargs["right_top"]
                assert isinstance(right, float)
                assert isinstance(top, float)
                self.origin = right - rot_width / 2, top + rot_height / 2
            elif "left_bottom" in kwargs:
                left, bottom = kwargs["left_bottom"]
                assert isinstance(left, float)
                assert isinstance(bottom, float)
                self.origin = left + rot_width / 2, bottom - rot_height / 2
            elif "right_bottom" in kwargs:
                right, bottom = kwargs["right_bottom"]
                assert isinstance(right, float)
                assert isinstance(bottom, float)
                self.origin = right - rot_width / 2, bottom - rot_height / 2
