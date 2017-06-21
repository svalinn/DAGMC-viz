import os

from visit import *


def WindowSettings(Coordinates = (0, 0, 0)):
    """Modify window settings."""

    x = 0
    y = 1
    z = 2

    xdeg = Coordinates[0]
    ydeg = Coordinates[1]
    zdeg = Coordinates[2]

    # Set view
    v = GetView3D()
    v.RotateAxis(x, xdeg)
    v.RotateAxis(y, ydeg)
    v.RotateAxis(z, zdeg)
    SetView3D(v)

    # Set window attributes for saving
    Attribute = SaveWindowAttributes()

    Attribute.format = Attribute.BMP

    Attribute.fileName = "./Images/sample"

    Attribute.width = 500
    Attribute.height = 2000

    SetSaveWindowAttributes(Attribute)
