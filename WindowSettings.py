from visit import *


def WindowSettings():
    """Modify window settings."""

    Attribute = SaveWindowAttributes()

    Attribute.format = Attribute.BMP
    Attribute.fileName = "./Images/example"
    Attribute.width = 500
    Attribute.height = 500
    Attribute.screenCapture = 0

    SetSaveWindowAttributes(Attribute)
