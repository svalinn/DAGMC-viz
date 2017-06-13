from visit import *


def OperatorSettings():
    """Add operator and it's settings."""

    Attribute = SliceAttributes()

    Attribute.axisType = Attribute.YAxis

    SetOperatorOptions(Attribute)
