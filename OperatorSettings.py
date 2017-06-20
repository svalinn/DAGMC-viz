from visit import *


def OperatorSettings():
    """Add operator and its settings."""

    Attribute = SliceAttributes()

    Attribute.axisType = Attribute.YAxis

    SetOperatorOptions(Attribute)

    Attribute = TransformAttributes()

    Attribute.doRotate = 1
    Attribute.rotateOrigin = (0, 0, 0)
    Attribute.rotateAxis = (0, 1, 0)
    Attribute.rotateAmount = 30
    Attribute.rotateType = Attribute.Deg

    SetOperatorOptions(Attribute)

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
