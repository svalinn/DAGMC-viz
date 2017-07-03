import os

from visit import *


def WindowSettings():
    """Modify window settings."""

    # Set window attributes for saving
    Attribute = SaveWindowAttributes()

    Attribute.format = Attribute.PNG

    Attribute.fileName = "./Images/sample"

    Attribute.width = 500
    Attribute.height = 2000

    SetSaveWindowAttributes(Attribute)

    light = GetLight(0)
    light.type = light.Ambient
    SetLight(0, light)
