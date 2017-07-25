import os

from visit import *


def WindowSettings(Shading=False):
    """Modify window settings."""

    # Set window attributes for saving.
    Attribute = SaveWindowAttributes()

    Attribute.format = Attribute.PNG

    Attribute.fileName = "../Images/sample"

    Attribute.width = 1024
    Attribute.height = 1024

    SetSaveWindowAttributes(Attribute)

    # Set legend options.
    Attribute = AnnotationAttributes()

    Attribute.databaseInfoFlag = 0
    Attribute.legendInfoFlag = 1

    SetAnnotationAttributes(Attribute)

    # Set lighting attributes.
    if Shading is False:
        light = GetLight(0)
        light.type = light.Ambient
        SetLight(0, light)
    else:
        pass

    # Set Zoom.
    v = GetView3D()
    v.imageZoom = 0.75
    SetView3D(v)

    # Change legend options
    Attribute = AnnotationAttributes()

    Attribute.legendInfoFlag = 1
    Attribute.databaseInfoFlag = 0
    Attribute.timeInfoFlag = 0
    Attribute.userInfoFlag = 0

    SetAnnotationAttributes(Attribute)

