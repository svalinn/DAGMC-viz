from visit import *


def OperatorSettings():
    """Add operator and it's settings."""

    Attribute = SliceAttributes()

    Attribute.axisType = Attribute.YAxis

    SetOperatorOptions(Attribute)

    Attribute = ClipAttributes()

    Attribute.plane1Normal = (1, 0, 0)
    Attribute.plane2Normal = (0, 1, 0)
    Attribute.plane3Normal = (0, 0, 1)

    SetOperatorOptions(Attribute)
