from visit import *


def OperatorSettings(OperatorSet):
    """Add operator and its settings."""

    if OperatorSet == "Clip0":

        Attribute = ClipAttributes()

        Attribute.quality = Attribute.Accurate

        Attribute.plane1Status = 1
        Attribute.plane2Status = 1
        Attribute.plane3Status = 1

        Attribute.plane1Origin = (0, 0, 0)
        Attribute.plane2Origin = (0, 0, 0)
        Attribute.plane3Origin = (0, 0, 0)

        Attribute.plane1Normal = (1, 0, 1)
        Attribute.plane2Normal = (0, 1, 0)
        Attribute.plane3Normal = (0, 0, 1)

        SetOperatorOptions(Attribute)

    if OperatorSet == "Clip1":

        Attribute = ClipAttributes()

        Attribute.quality = Attribute.Accurate

        Attribute.plane1Status = 1
        Attribute.plane2Status = 1
        Attribute.plane3Status = 0

        Attribute.plane1Origin = (0, 0, 0)
        Attribute.plane2Origin = (0, 0, 0)
        Attribute.plane3Origin = (0, 0, 0)

        Attribute.plane1Normal = (1, 0, 1)
        Attribute.plane2Normal = (0, 1, 0)
        Attribute.plane3Normal = (0, 0, 1)

        SetOperatorOptions(Attribute)

    if OperatorSet == "Clip2":

        Attribute = ClipAttributes()

        Attribute.quality = Attribute.Accurate

        Attribute.plane1Status = 1
        Attribute.plane2Status = 0
        Attribute.plane3Status = 0

        Attribute.plane1Origin = (30, 30, 30)
        Attribute.plane2Origin = (0, 0, 0)
        Attribute.plane3Origin = (0, 0, 0)

        Attribute.plane1Normal = (-1, 0, 0)
        Attribute.plane2Normal = (0, 1, 0)
        Attribute.plane3Normal = (0, 0, 1)

        SetOperatorOptions(Attribute)

    if OperatorSet == "Slice0":

        Attribute = SliceAttributes()

        Attribute.originType = Attribute.Point
        Attribute.originPoint = (0, -5, 0)

        Attribute.axisType = Attribute.YAxis
        Attribute.project2d = 0

        SetOperatorOptions(Attribute)

    if OperatorSet == "Slice1":

        Attribute = SliceAttributes()

        Attribute.originType = Attribute.Point
        Attribute.originPoint = (0, 10, 0)

        Attribute.axisType = Attribute.YAxis
        Attribute.project2d = 0

        SetOperatorOptions(Attribute)

    if OperatorSet == "Slice2":

        Attribute = SliceAttributes()

        Attribute.originType = Attribute.Point
        Attribute.originPoint = (0, 20, 0)

        Attribute.axisType = Attribute.YAxis
        Attribute.project2d = 0

        SetOperatorOptions(Attribute)
