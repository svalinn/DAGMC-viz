from visit import *


def WindowSettings():
    """Modify window settings."""

    v = GetView3D()
    v.RotateAxis(0, 30.0)
    SetView3D(v)

    Attribute = SaveWindowAttributes()

    Attribute.format = Attribute.BMP
    Attribute.fileName = "./Images/sample"
    Attribute.width = 500
    Attribute.height = 2000
    Attribute.screenCapture = 0

    SetSaveWindowAttributes(Attribute)
