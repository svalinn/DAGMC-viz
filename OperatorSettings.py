from visit import *


def OperatorSettings(OperatorSet):
    """Add operator and its settings."""

    if OperatorSet == "Clip0":

        Attribute = ClipAttributes()

        Attribute.quality = Attribute.Accurate

        Attribute.plane1Status = 1
        Attribute.plane2Status = 1
        Attribute.plane3Status = 1

        Attribute.plane1Origin = (0, 0, 1)
        Attribute.plane2Origin = (1, 0, 0)
        Attribute.plane3Origin = (0, 1, 0)

        Attribute.plane1Normal = (0, 0, 1)
        Attribute.plane2Normal = (1, 0, 0)
        Attribute.plane3Normal = (0, 1, 0)

        SetOperatorOptions(Attribute)

    if OperatorSet == "Slice0":

        Attribute = SliceAttributes()

        Attribute.originType = Attribute.Percent
        Attribute.originPercent = 40

        Attribute.axisType = Attribute.YAxis
        Attribute.project2d = 0

        SetOperatorOptions(Attribute)

    if OperatorSet == "Slice1":

        Attribute = SliceAttributes()

        Attribute.originType = Attribute.Percent
        Attribute.originPercent = 50

        Attribute.axisType = Attribute.YAxis
        Attribute.project2d = 0

        SetOperatorOptions(Attribute)

    if OperatorSet == "Slice2":

        Attribute = SliceAttributes()

        Attribute.originType = Attribute.Percent
        Attribute.originPercent = 60

        Attribute.axisType = Attribute.YAxis
        Attribute.project2d = 0

        SetOperatorOptions(Attribute)
