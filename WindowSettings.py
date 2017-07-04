import os

from visit import *


def WindowSettings():
    """Modify window settings."""

    # Set window attributes for saving.
    Attribute = SaveWindowAttributes()

    Attribute.format = Attribute.PNG

    Attribute.fileName = "./Images/sample"

    Attribute.width = 1000
    Attribute.height = 1000

    SetSaveWindowAttributes(Attribute)

    # Set lighting attributes.
    light = GetLight(0)
    light.type = light.Ambient
    SetLight(0, light)

    # Set legend options.
    Attribute = AnnotationAttributes()

    Attribute.databaseInfoFlag = 0
    Attribute.legendInfoFlag = 1

    SetAnnotationAttributes(Attribute)
