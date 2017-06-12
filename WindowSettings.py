from visit import *


def WindowSettings():
    """Modify window settings."""

    Attribute = SaveWindowAttributes()

    Attribute.format = Attribute.BMP
    Attribute.fileName = "./Images/sample"
    Attribute.width = 500
    Attribute.height = 2000
    Attribute.screenCapture = 0

    SetSaveWindowAttributes(Attribute)
